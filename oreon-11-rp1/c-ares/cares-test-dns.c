#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

static int skip_name(const unsigned char *p, int len, int off)
{
	int steps = 0;
	while (off < len && steps++ < 64) {
		unsigned int lab = p[off];
		if (lab == 0)
			return off + 1;
		if ((lab & 0xc0) == 0xc0)
			return (off + 1 < len) ? off + 2 : -1;
		if (lab & 0xc0)
			return -1;
		off += 1 + (int)lab;
	}
	return -1;
}

static int put_name(unsigned char *p, int cap, int off, const char *name)
{
	const char *dot;
	while (*name) {
		size_t n;
		dot = strchr(name, '.');
		n = dot ? (size_t)(dot - name) : strlen(name);
		if (off < 0 || n == 0 || n > 63 || off + 1 + (int)n >= cap)
			return -1;
		p[off++] = (unsigned char)n;
		memcpy(p + off, name, n);
		off += (int)n;
		if (!dot)
			break;
		name = dot + 1;
	}
	if (off >= cap)
		return -1;
	p[off++] = 0;
	return off;
}

static int put16(unsigned char *p, int cap, int off, unsigned int v)
{
	if (off < 0 || off + 2 > cap)
		return -1;
	p[off++] = (unsigned char)(v >> 8);
	p[off++] = (unsigned char)v;
	return off;
}

static int put32(unsigned char *p, int cap, int off, unsigned int v)
{
	off = put16(p, cap, off, v >> 16);
	if (off < 0)
		return -1;
	return put16(p, cap, off, v & 0xffff);
}

static int eq_ci(const char *a, const char *b)
{
	while (*a && *b) {
		unsigned char ca = (unsigned char)*a;
		unsigned char cb = (unsigned char)*b;
		if (ca >= 'A' && ca <= 'Z')
			ca = (unsigned char)(ca + 32);
		if (cb >= 'A' && cb <= 'Z')
			cb = (unsigned char)(cb + 32);
		if (ca != cb)
			return 0;
		a++;
		b++;
	}
	return *a == 0 && *b == 0;
}

static int qname_eq(const unsigned char *p, int len, int off, const char *want)
{
	char got[256];
	int n = 0;
	int steps = 0;

	while (off < len && steps++ < 64) {
		unsigned int lab = p[off];
		if (lab == 0)
			break;
		if (lab & 0xc0)
			return 0;
		if (off + 1 + (int)lab > len || n + (int)lab + 1 >= (int)sizeof(got))
			return 0;
		if (n)
			got[n++] = '.';
		memcpy(got + n, p + off + 1, lab);
		n += (int)lab;
		off += 1 + (int)lab;
	}
	got[n] = 0;
	return eq_ci(got, want);
}

static int nxdomain(unsigned char *out, int cap, const unsigned char *q, int qend)
{
	unsigned int flags;
	if (qend > cap)
		return -1;
	memcpy(out, q, (size_t)qend);
	flags = 0x8483;
	if (q[2] & 0x01)
		flags |= 0x0100;
	out[2] = (unsigned char)(flags >> 8);
	out[3] = (unsigned char)flags;
	out[4] = out[5] = 0;
	out[6] = out[7] = 0;
	out[8] = out[9] = out[10] = out[11] = 0;
	return qend;
}

static int answer(unsigned char *out, int cap, const unsigned char *q, int qlen)
{
	int name_end, qend, off, rdlen_at, rdata, type;
	unsigned int flags;
	if (qlen < 12)
		return -1;
	name_end = skip_name(q, qlen, 12);
	if (name_end < 0 || name_end + 4 > qlen)
		return -1;
	qend = name_end + 4;
	type = (q[name_end] << 8) | q[name_end + 1];
	if (qend > cap)
		return -1;
	if (type == 12 &&
	    (qname_eq(q, qlen, 12, "0.2.0.192.in-addr.arpa") ||
	     qname_eq(q, qlen, 12,
		      "4.0.3.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.1.0.8.b.d.0.1.0.0.2.ip6.arpa")))
		return nxdomain(out, cap, q, qend);
	memcpy(out, q, (size_t)qend);
	flags = 0x8480;
	if (q[2] & 0x01)
		flags |= 0x0100;
	out[2] = (unsigned char)(flags >> 8);
	out[3] = (unsigned char)flags;
	out[4] = 0;
	out[5] = 1;
	out[6] = 0;
	out[7] = 1;
	out[8] = out[9] = out[10] = out[11] = 0;
	off = qend;
	if (off + 2 > cap)
		return -1;
	out[off++] = 0xc0;
	out[off++] = 12;
	off = put16(out, cap, off, (unsigned int)(type == 255 ? 1 : type));
	off = put16(out, cap, off, 1);
	off = put32(out, cap, off, 60);
	if (off < 0 || off + 2 > cap)
		return -1;
	rdlen_at = off;
	off += 2;
	rdata = off;
	switch (type) {
	case 28:
		if (off + 16 > cap)
			return -1;
		memset(out + off, 0, 16);
		out[off] = 0x20;
		out[off + 1] = 0x01;
		out[off + 2] = 0x0d;
		out[off + 3] = 0xb8;
		out[off + 15] = 1;
		off += 16;
		break;
	case 12:
		off = put_name(out, cap, off, "one.one.one.one");
		break;
	case 2:
		off = put_name(out, cap, off, "ns.google.com");
		break;
	case 15:
		off = put16(out, cap, off, 10);
		if (off > 0)
			off = put_name(out, cap, off, "mail.google.com");
		break;
	case 16:
		if (off + 8 > cap)
			return -1;
		out[off++] = 7;
		memcpy(out + off, "v=oreon", 7);
		off += 7;
		break;
	case 6:
		off = put_name(out, cap, off, "ns.google.com");
		if (off > 0)
			off = put_name(out, cap, off, "a.google.com");
		if (off > 0)
			off = put32(out, cap, off, 1);
		if (off > 0)
			off = put32(out, cap, off, 3600);
		if (off > 0)
			off = put32(out, cap, off, 600);
		if (off > 0)
			off = put32(out, cap, off, 86400);
		if (off > 0)
			off = put32(out, cap, off, 60);
		break;
	case 33:
		off = put16(out, cap, off, 0);
		if (off > 0)
			off = put16(out, cap, off, 0);
		if (off > 0)
			off = put16(out, cap, off, 143);
		if (off > 0)
			off = put_name(out, cap, off, "imap.gmail.com");
		break;
	default:
		off = put32(out, cap, off, 0xc0000201);
		break;
	}
	if (off < 0)
		return -1;
	out[rdlen_at] = (unsigned char)((off - rdata) >> 8);
	out[rdlen_at + 1] = (unsigned char)(off - rdata);
	return off;
}

int main(int argc, char **argv)
{
	int port = argc > 1 ? atoi(argv[1]) : 53;
	int fd;
	struct sockaddr_in addr;

	fd = socket(AF_INET, SOCK_DGRAM, 0);
	if (fd < 0) {
		perror("socket");
		return 1;
	}
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = htonl(0x7f000001);
	addr.sin_port = htons((unsigned short)port);
	if (bind(fd, (struct sockaddr *)&addr, sizeof(addr)) != 0) {
		perror("bind");
		return 1;
	}
	fprintf(stderr, "ready\n");
	fflush(stderr);
	for (;;) {
		unsigned char q[2048], out[2048];
		struct sockaddr_in from;
		socklen_t fromlen = sizeof(from);
		ssize_t n = recvfrom(fd, q, sizeof(q), 0, (struct sockaddr *)&from, &fromlen);
		int outn;
		if (n < 0)
			continue;
		outn = answer(out, (int)sizeof(out), q, (int)n);
		if (outn > 0)
			sendto(fd, out, (size_t)outn, 0, (struct sockaddr *)&from, fromlen);
	}
}
