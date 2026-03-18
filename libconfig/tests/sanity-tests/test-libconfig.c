/*
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   Description: libconfig
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
#include <stdio.h>
#include <stdlib.h>
#include <libconfig.h>
#include <unistd.h>

#define TEST_WRITE_FILE_NAME "/var/run/example.cfg"
#define TEST_READ_FILE_NAME "/var/run/auth.cfg"

static void test_config_read(void **state) {
        const char *base = NULL, *host = NULL, *name = NULL;
        const config_setting_t *retries;
        int aretries[] = {10, 15, 20, 60};
        int count, n, enabled;
        config_t cfg, *cf;

        cf = &cfg;
        config_init(cf);

        assert_non_null(config_read_file(cf, TEST_READ_FILE_NAME));

        assert_true(config_lookup_string(cf, "name", &name) >=0);
        assert_string_equal(name, "JP");

        assert_true(config_lookup_bool(cf, "enabled", &enabled) >=0);
        assert_int_equal(enabled, 0);

        assert_true((config_lookup_string(cf, "ldap.host", &host)) >=0);
        assert_string_equal(host, "ldap.example.com");

        assert_true((config_lookup_string(cf, "ldap.base", &base)) >=0);
        assert_string_equal(base , "ou=usr,o=example.com");

        assert_non_null((retries = config_lookup(cf, "ldap.retries")));
        count = config_setting_length(retries);

        assert_int_equal(count, 4);
        for (n = 0; n < count; n++)
                assert_int_equal(aretries[n], config_setting_get_int_elem(retries, n));

        config_destroy(cf);
}

static void test_config_write(void **state) {
        config_setting_t *root, *setting, *group, *array;
        const char *street, *city, *st, *str;
        config_t cfg, *cf;
        int i, zip;

        config_init(&cfg);
        root = config_root_setting(&cfg);

        assert_non_null((group = config_setting_add(root, "address", CONFIG_TYPE_GROUP)));

        assert_non_null((setting = config_setting_add(group, "street", CONFIG_TYPE_STRING)));
        assert_true(config_setting_set_string(setting, "1 Woz Way") >= 0);

        assert_non_null((setting = config_setting_add(group, "city", CONFIG_TYPE_STRING)));
        assert_true(config_setting_set_string(setting, "San Jose") >= 0);

        assert_non_null((setting = config_setting_add(group, "state", CONFIG_TYPE_STRING)));
        assert_true(config_setting_set_string(setting, "CA") >= 0);

        assert_non_null((setting = config_setting_add(group, "zip", CONFIG_TYPE_INT)));
        assert_true(config_setting_set_int(setting, 95110) >= 0);

        assert_non_null((array = config_setting_add(root, "numbers", CONFIG_TYPE_ARRAY)));

        for(i = 0; i < 10; ++i) {
                assert_non_null((setting = config_setting_add(array, NULL, CONFIG_TYPE_INT)));
                assert_true(config_setting_set_int(setting, 10 * i) >=0);
        }

        assert_non_null((config_write_file(&cfg, TEST_WRITE_FILE_NAME)));
        config_destroy(&cfg);

        /* Read Back and test */
        config_init(&cfg);

        assert_non_null((config_read_file(&cfg, TEST_WRITE_FILE_NAME)));
        assert_non_null((setting = config_lookup(&cfg, "address")));

        assert_true(config_setting_lookup_string(setting, "street", &street) >= 0);
        assert_string_equal(street, "1 Woz Way");

        assert_true(config_setting_lookup_string(setting, "city", &city) >=0);
        assert_string_equal(city, "San Jose");

        assert_true(config_setting_lookup_string(setting, "state", &st) >=0);
        assert_string_equal(st, "CA");

        assert_true(config_setting_lookup_int(setting, "zip", &zip) >=0);
        assert_int_equal(zip, 95110);

        array = config_lookup(&cfg, "numbers");
        if(array) {
                int count, n;

                count = config_setting_length(array);
                for (n = 0; n < count; n++) {
                        assert_int_equal(n * 10, config_setting_get_int_elem(array, n));
                }
        }
        config_destroy(&cfg);

        unlink(TEST_WRITE_FILE_NAME);
}

int main(int argc, char *argv[]) {
        const struct CMUnitTest libconfig_tests[] = {
                                                     cmocka_unit_test(test_config_write),
                                                     cmocka_unit_test(test_config_read),
        };

        return cmocka_run_group_tests(libconfig_tests, NULL, NULL);
}
