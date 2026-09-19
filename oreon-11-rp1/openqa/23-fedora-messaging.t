#! /usr/bin/perl

# Copyright (C) 2016-2019 SUSE LLC
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

BEGIN {
    unshift @INC, 'lib';
}

use Mojo::Base;
use Mojo::IOLoop;

use FindBin;
use lib "$FindBin::Bin/lib";
use OpenQA::Client;
use OpenQA::Jobs::Constants;
use OpenQA::Test::Database;
use Test::MockModule;
use Test::More;
use Test::Mojo;
use Test::Warnings;
use Mojo::File qw(tempdir path);
use OpenQA::WebAPI::Plugin::AMQP;

my %published;
my $plugin_mock_callcount;

my $uuid_mock = Test::MockModule->new('UUID::URandom');
$uuid_mock->mock(
    create_uuid_string => sub {
        return '9fbba7a5-2402-4f6b-a20e-af478eee05f5';
    }
);

# we mock the parent class here so we can test the child class
my $plugin_mock = Test::MockModule->new('OpenQA::WebAPI::Plugin::AMQP');
$plugin_mock->mock(
    publish_amqp => sub {
        my ($self, $topic, $body, $headerframe) = @_;
        # ignore the non-fedoraci messages, makes it easier to
        # understand the expected call counts
        if ($topic =~ /\.ci\./) {
            $plugin_mock_callcount++;
            # strip the time-based bits, at least till
            # https://github.com/cho45/Test-Time/issues/14 is done
            delete $body->{'generated_at'};
            delete $headerframe->{'headers'}->{'sent-at'};
            $published{$topic} = [$body, $headerframe];
        }
    }
);

OpenQA::Test::Database->new->create(fixtures_glob => '01-jobs.pl 03-users.pl 05-job_modules.pl');

# this test also serves to test plugin loading via config file
my $conf = << 'EOF';
[global]
plugins=FedoraMessaging
base_url=https://openqa.stg.fedoraproject.org
[amqp]
topic_prefix=org.fedoraproject.stg
EOF

my $tempdir = tempdir;
$ENV{OPENQA_CONFIG} = $tempdir;
path($ENV{OPENQA_CONFIG})->make_path->child("openqa.ini")->spew($conf);

my $t = Test::Mojo->new('OpenQA::WebAPI');

# XXX: Test::Mojo loses its app when setting a new ua
# https://github.com/kraih/mojo/issues/598
my $app = $t->app;
$app->config->{'scm git'}->{git_auto_update} = 'no';
$t->ua(
    OpenQA::Client->new(apikey => 'PERCIVALKEY02', apisecret => 'PERCIVALSECRET02')->ioloop(Mojo::IOLoop->singleton));
$t->app($app);

my $settings = {
    DISTRI      => 'Unicorn',
    FLAVOR      => 'pink',
    VERSION     => '42',
    BUILD       => 'Fedora-Rawhide-20180129.n.0',
    TEST        => 'rainbow',
    ISO         => 'whatever.iso',
    DESKTOP     => 'DESKTOP',
    KVM         => 'KVM',
    ISO_MAXSIZE => 1,
    MACHINE     => "RainbowPC",
    ARCH        => 'x86_64',
    SUBVARIANT  => 'workstation',
    TEST_TARGET => 'ISO',
};

my $expected_artifact = {
    id           => 'Fedora-Rawhide-20180129.n.0',
    type         => 'productmd-compose',
    compose_type => 'nightly',
};

my $expected_contact = {
    name  => 'Fedora openQA',
    team  => 'Fedora QA',
    url   => 'https://openqa.stg.fedoraproject.org',
    docs  => 'https://fedoraproject.org/wiki/OpenQA',
    irc   => '#fedora-qa',
    email => 'qa-devel@lists.fedoraproject.org',
};

my $expected_image = {
    id  => 'whatever.iso',
    name  => 'whatever.iso',
    type  => 'ISO',
};

my $expected_pipeline = {
    id   => 'openqa.Fedora-Rawhide-20180129.n.0.rainbow.RainbowPC.pink.x86_64',
    name => 'openqa.Fedora-Rawhide-20180129.n.0.rainbow.RainbowPC.pink.x86_64',
};

my $expected_run = {
    url => '',
    log => '',
    id  => '',
};

my $expected_system = {
    os           => 'fedora-42',
    provider     => 'openqa',
    architecture => 'x86_64',
    variant      => 'workstation',
};

my $expected_test = {
    category  => 'validation',
    type      => 'rainbow RainbowPC pink x86_64',
    namespace => 'compose',
    lifetime  => 240,
};

my $expected_error;

my $expected_version = '0.2.1';

sub get_expected {
    my $expected = {
        artifact => $expected_artifact,
        contact  => $expected_contact,
        image    => $expected_image,
        pipeline => $expected_pipeline,
        run      => $expected_run,
        system   => [$expected_system],
        test     => $expected_test,
        version  => $expected_version,
    };
    $expected->{'error'} = $expected_error if ($expected_error);
    return $expected;
}

# create a job via API
my $job;
my $newjob;
subtest 'create job' => sub {
    # reset the call count
    $plugin_mock_callcount = 0;
    $t->post_ok("/api/v1/jobs" => form => $settings)->status_is(200);
    ok($job = $t->tx->res->json->{id}, 'got ID of new job');
    ok($plugin_mock_callcount == 1,    'plugin mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.productmd-compose.test.queued'}};
    $expected_run = {
        url => "https://openqa.stg.fedoraproject.org/tests/$job",
        log => "https://openqa.stg.fedoraproject.org/tests/$job/file/autoinst-log.txt",
        id  => $job,
    };
    my $expected = get_expected;
    my $expected_headerframe = {
        headers => {
            fedora_messaging_severity   => 20,
            fedora_messaging_schema     => 'base.message',
        },
        content_encoding => 'utf-8',
        delivery_mode => 2,
        # if this fails, probably means mock broke
        message_id => '9fbba7a5-2402-4f6b-a20e-af478eee05f5',
    };
    is_deeply($body, $expected, 'job create triggers standardized amqp');
    is_deeply($headerframe, $expected_headerframe, 'amqp header frame is as expected');
};

subtest 'mark job as done' => sub {
    $plugin_mock_callcount = 0;
    $t->post_ok("/api/v1/jobs/$job/set_done")->status_is(200);
    ok($plugin_mock_callcount == 1, 'mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.productmd-compose.test.error'}};
    $expected_error = {reason => INCOMPLETE,};
    delete $expected_test->{'lifetime'};
    my $expected = get_expected;
    is_deeply($body, $expected, 'job done (failed) triggers standardized amqp');
};

subtest 'duplicate and cancel job' => sub {
    $plugin_mock_callcount = 0;
    $t->post_ok("/api/v1/jobs/$job/duplicate")->status_is(200);
    $newjob = $t->tx->res->json->{id};
    ok($plugin_mock_callcount == 1, 'mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.productmd-compose.test.queued'}};
    $expected_run = {
        clone_of => $job,
        url      => "https://openqa.stg.fedoraproject.org/tests/$newjob",
        log      => "https://openqa.stg.fedoraproject.org/tests/$newjob/file/autoinst-log.txt",
        id       => $newjob,
    };
    $expected_test->{'lifetime'} = 240;
    $expected_error = '';
    delete $expected_test->{'result'};
    my $expected = get_expected;
    is_deeply($body, $expected, 'job duplicate triggers standardized amqp');

    $plugin_mock_callcount = 0;
    $t->post_ok("/api/v1/jobs/$newjob/cancel")->status_is(200);
    ok($plugin_mock_callcount == 1, 'mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.productmd-compose.test.error'}};
    $expected_error = {reason => 'user_cancelled',};
    delete $expected_test->{'lifetime'};
    delete $expected_run->{'clone_of'};
    my $expected = get_expected;
    is_deeply($body, $expected, 'job cancel triggers standardized amqp');
};

subtest 'duplicate and pass job' => sub {
    $plugin_mock_callcount = 0;
    $t->post_ok("/api/v1/jobs/$newjob/duplicate")->status_is(200);
    my $newerjob = $t->tx->res->json->{id};
    # explicitly set job as passed
    $t->post_ok("/api/v1/jobs/$newerjob/set_done?result=passed")->status_is(200);
    ok($plugin_mock_callcount == 2, 'mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.productmd-compose.test.complete'}};
    $expected_run = {
        url => "https://openqa.stg.fedoraproject.org/tests/$newerjob",
        log => "https://openqa.stg.fedoraproject.org/tests/$newerjob/file/autoinst-log.txt",
        id  => $newerjob,
    };
    $expected_test->{'result'} = 'passed';
    $expected_error = '';
    my $expected = get_expected;
    is_deeply($body, $expected, 'job done (passed) triggers standardized amqp');
};

subtest 'create update job' => sub {
    $plugin_mock_callcount = 0;
    diag("Count: $plugin_mock_callcount");
    $settings->{BUILD} = 'Update-FEDORA-2019-6bda4c81f4';
    # this is intentionally not in alphabetical order
    $settings->{ADVISORY_NVRS} = 'kernel-5.2.7-100.fc29 kernel-tools-5.2.7-100.fc29 kernel-headers-5.2.7-100.fc29';
    # let's test HDD_* impact on system->{os} here too
    $settings->{HDD_1}    = 'disk_f40_minimal.qcow2';
    $settings->{BOOTFROM} = 'c';
    # some update tests don't have SUBVARIANT, in which case system
    # variant should not be set
    delete $settings->{SUBVARIANT};
    $t->post_ok("/api/v1/jobs" => form => $settings)->status_is(200);
    ok(my $updatejob = $t->tx->res->json->{id}, 'got ID of update job');
    diag("Count: $plugin_mock_callcount");
    ok($plugin_mock_callcount == 1, 'mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.fedora-update.test.queued'}};
    $expected_artifact = {
        alias   => 'FEDORA-2019-6bda4c81f4',
        builds  => [
            {
                nvr => 'kernel-5.2.7-100.fc29'
            },
            {
                nvr => 'kernel-headers-5.2.7-100.fc29'
            },
            {
                nvr => 'kernel-tools-5.2.7-100.fc29'
            }
        ],
        id      => 'sha256:cf6f57a196a213606246070a99b94053160fee43c7987d071f422de30b2f2953',
        type    => 'fedora-update',
        release => {
            version => '42',
            name    => 'F42'
        },
    };
    $expected_pipeline = {
        id   => 'openqa.Update-FEDORA-2019-6bda4c81f4.rainbow.RainbowPC.pink.x86_64',
        name => 'openqa.Update-FEDORA-2019-6bda4c81f4.rainbow.RainbowPC.pink.x86_64',
    };
    $expected_run = {
        url => "https://openqa.stg.fedoraproject.org/tests/$updatejob",
        log => "https://openqa.stg.fedoraproject.org/tests/$updatejob/file/autoinst-log.txt",
        id  => $updatejob,
    };
    $expected_system->{'os'}      = 'fedora-40';
    $expected_test->{'namespace'} = 'update';
    $expected_test->{'lifetime'}  = 240;
    delete $expected_system->{'variant'};
    delete $expected_test->{'result'};
    my $expected = get_expected;
    # no image for update message
    delete $expected->{'image'};
    is_deeply($body, $expected, 'update job create triggers standardized amqp');
};

subtest 'create update job (new-style ADVISORY_NVR_N)' => sub {
    $plugin_mock_callcount = 0;
    diag("Count: $plugin_mock_callcount");
    delete $settings->{ADVISORY_NVRS};
    # these are intentionally not in alphabetical order
    $settings->{ADVISORY_NVRS_1} = 'kernel-5.2.8-100.fc29 kernel-tools-5.2.8-100.fc29';
    $settings->{ADVISORY_NVRS_2} = 'kernel-headers-5.2.8-100.fc29';
    $t->post_ok("/api/v1/jobs" => form => $settings)->status_is(200);
    ok(my $newupdatejob = $t->tx->res->json->{id}, 'got ID of new-style update job');
    diag("Count: $plugin_mock_callcount");
    ok($plugin_mock_callcount == 1, 'mock was called');
    my ($body, $headerframe) = @{$published{'org.fedoraproject.stg.ci.fedora-update.test.queued'}};
    $expected_artifact = {
        alias   => 'FEDORA-2019-6bda4c81f4',
        builds  => [
            {
                nvr => 'kernel-5.2.8-100.fc29'
            },
            {
                nvr => 'kernel-headers-5.2.8-100.fc29'
            },
            {
                nvr => 'kernel-tools-5.2.8-100.fc29'
            }
        ],
        id      => 'sha256:b85bba148cec9d9c4dafea3a49785abef1f549fbad368f3818e20d9802340b16',
        type    => 'fedora-update',
        release => {
            version => '42',
            name    => 'F42'
        },
    };
    $expected_run = {
        url => "https://openqa.stg.fedoraproject.org/tests/$newupdatejob",
        log => "https://openqa.stg.fedoraproject.org/tests/$newupdatejob/file/autoinst-log.txt",
        id  => $newupdatejob,
    };
    my $expected = get_expected;
    # no image for update message
    delete $expected->{'image'};
    is_deeply($body, $expected, 'update job create triggers standardized amqp');
};

done_testing();
