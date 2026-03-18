/*
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   Description: libnet tests
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
# ~~~
*/
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <netinet/in.h>
#include <setjmp.h>
#include <inttypes.h>
#include <cmocka.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <errno.h>
#include <unistd.h>
#include <libnet.h>
#include <netinet/if_ether.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <netinet/if_ether.h>
#include <pcap.h>
#include <pthread.h>
#include <sys/time.h>

#define PCAP_FILE "/var/run/libnet-test.pcap"

pcap_t *handle;

struct UDP_hdr {
        u_short uh_sport;               /* source port */
        u_short uh_dport;               /* destination port */
        u_short uh_ulen;                /* datagram length */
        u_short uh_sum;                 /* datagram checksum */
};

static void assert_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet) {
        unsigned int ipl;
        uint32_t src, dst;
        struct ip *ip;
        struct ether_header *eth_header;

        eth_header = (struct ether_header *) packet;
        if (ntohs(eth_header->ether_type) != ETHERTYPE_IP)
                return;

        packet += sizeof(struct ether_header);
        ip = (struct ip *) packet;
        ipl = ip->ip_hl * 4;

        src = inet_addr("192.168.50.6");
        dst = inet_addr("192.168.50.5");

        assert_memory_equal(&dst, &ip->ip_dst, sizeof(uint32_t));
        assert_memory_equal(&src, &ip->ip_src, sizeof(uint32_t));

        if (ip->ip_p == IPPROTO_UDP) {
                struct UDP_hdr *udp;

                packet += ipl;

                udp = (struct UDP_hdr *) packet;

                printf("UDP src_port=%d dst_port=%d\n", ntohs(udp->uh_sport), ntohs(udp->uh_dport));

                assert_int_equal(2425, ntohs(udp->uh_sport));
                assert_int_equal(2426, ntohs(udp->uh_dport));
        } else if (ip->ip_p == IPPROTO_TCP) {
                struct tcphdr *tcp;
                packet += ipl;

                tcp = (struct tcphdr *) packet;

                printf("TCP src_port=%d dst_port=%d\n", ntohs(tcp->th_sport), ntohs(tcp->th_dport));

                assert_int_equal(2425, ntohs(tcp->th_sport));
                assert_int_equal(2426, ntohs(tcp->th_dport));
        }
}

void *capture_packet_live(void *ptr) {
        char dev[] = "veth-test";
        char error_buffer[PCAP_ERRBUF_SIZE];
        struct bpf_program filter;
        bpf_u_int32 subnet_mask, ip;
        int total_packet_count;
        int r;

        r = pcap_lookupnet(dev, &ip, &subnet_mask, error_buffer);
        assert_true(r >=0);

        handle = pcap_open_live(dev, BUFSIZ, 1, 1000, error_buffer);
        assert_non_null(handle);

        r = pcap_compile(handle, &filter, ptr, 0, ip);
        assert_true(r >= 0);

        r = pcap_setfilter(handle, &filter);
        assert_true(r >= 0);

        pcap_loop(handle, total_packet_count, assert_packet, NULL);

        return 0;
}

void terminate_thread(int signum) {

        pcap_breakloop(handle);
        pcap_close(handle);

        handle = NULL;
        pthread_exit(NULL);
}

static void test_udp_packet_ipv4(void **state) {
        char dst[6] = {0xff,0xff,0xff,0xff,0xff,0xff};
        char src[6] = {0x12,0x34,0x56,0x78,0x9a,0xab};
        char err_buf[LIBNET_ERRBUF_SIZE] = {};
        char buf[1024] = {};
        libnet_t* l;
        int r, i;
        uint32_t len;
        pthread_t pcap_thread;
        struct itimerval tval;

        timerclear(& tval.it_interval); /* zero interval means no reset of timer */
        timerclear(& tval.it_value);
        tval.it_value.tv_sec = 10;      /* 10 second timeout */

        (void) signal(SIGALRM, terminate_thread);
        (void) setitimer(ITIMER_REAL, & tval, NULL);

        r = pthread_create(&pcap_thread, NULL, capture_packet_live, "udp port 2425");
        assert_true(r >=0);

        l = libnet_init(LIBNET_LINK_ADV, "veth-peer", err_buf);
        assert_non_null(l);
        len = sprintf(buf, "1:1:1111111111111:32:hello world%d", 1);

        for (i = 0; i < 5; i++) {

                r = libnet_build_udp(2425, 2426, len + 8, 0, buf, len, l, 0);
                assert_true(r >= 0);

                r = libnet_build_ipv4(20 + 8 + len, 0, 0, 0, 128, 17, 0, inet_addr("192.168.50.6"), inet_addr("192.168.50.5"), NULL, 0, l, 0);
                assert_true(r >= 0);

                r = libnet_build_ethernet(dst, src, 0x0800, NULL, 0, l, 0);
                assert_true(r >= 0);

                r = libnet_write(l);
                assert_true(r >= 0);

                sleep(1);
        }

        libnet_destroy(l);
}

static void test_tcp_packet_ipv4(void **state) {
        char dst[6] = {0xff,0xff,0xff,0xff,0xff,0xff};
        char src[6] = {0x12,0x34,0x56,0x78,0x9a,0xab};
        char errbuf[LIBNET_ERRBUF_SIZE];
        uint8_t *payload, payload_s;
        libnet_ptag_t tcp, ip, eth;
        int c, i, j, seqn, ack;
        char buf[1024] = {};
        pthread_t pcap_thread;
        struct itimerval tval;
        uint32_t len;
        libnet_t *l;
        int r;

        timerclear(& tval.it_interval);
        timerclear(& tval.it_value);
        tval.it_value.tv_sec = 10;

        (void) signal(SIGALRM, terminate_thread);
        (void) setitimer(ITIMER_REAL, & tval, NULL);

        r = pthread_create(&pcap_thread, NULL, capture_packet_live, "tcp port 2425");
        assert_true(r >=0);

        payload_s = 10;
        payload = malloc(payload_s*sizeof(uint8_t));
        assert_non_null(payload);
        memset(payload,0,payload_s);

        l = libnet_init(LIBNET_LINK, "veth-peer", errbuf);
        assert_non_null(l);

        tcp = ip = eth = LIBNET_PTAG_INITIALIZER;
        for (i=0; i<5; i++){
                seqn=i * (LIBNET_TCP_H+payload_s + 1);
                r = libnet_build_tcp(2425, 2426, seqn, seqn + LIBNET_TCP_H + payload_s + 1,
                                     TH_SYN, 32767, 0, 10, LIBNET_TCP_H + payload_s,
                                     payload, payload_s, l, tcp);
                assert_true(r >=0);

                r = libnet_build_ipv4(LIBNET_IPV4_H + LIBNET_TCP_H + payload_s,0,242,0,64,IPPROTO_TCP,0,
                                      inet_addr("192.168.50.6"), inet_addr("192.168.50.5"),
                                      NULL,0,l,ip);
                assert_true(r >=0);

                r = libnet_build_ethernet(dst, src, ETHERTYPE_IP, NULL, 0, l, eth);
                assert_true(r >=0);

                r = libnet_write(l);
                assert_true(r >=0);

                sleep(1);
        }
}

int main(int argc, char *argv[]) {
        const struct CMUnitTest libnet_tests[] = {
                                                  cmocka_unit_test(test_udp_packet_ipv4),
                                                  cmocka_unit_test(test_tcp_packet_ipv4),
        };

        return cmocka_run_group_tests(libnet_tests, NULL, NULL);
}
