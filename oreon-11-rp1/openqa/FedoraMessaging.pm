# Copyright (C) Red Hat Inc.
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
# with this program; if not, see <http://www.gnu.org/licenses/>.

# This is a plugin for publishing messages to fedora-messaging, Fedora's
# AMQP message broker. It piggybacks on the upstream AMQP plugin but
# includes headers required by the fedora-messaging spec and publishes
# messages in the "CI Messages" spec: https://pagure.io/fedora-ci/messages
# as well as more 'native' style messages.

package OpenQA::WebAPI::Plugin::FedoraMessaging;

use Digest::SHA qw(sha256_hex);
use POSIX qw(strftime);

use Mojo::Base 'OpenQA::WebAPI::Plugin::AMQP', -signatures;
use OpenQA::Jobs::Constants;
use OpenQA::Log qw(log_debug log_error);
use OpenQA::Utils;
use UUID::URandom 'create_uuid_string';

sub _iso8601_now {
    # we do this twice, so factor it out
    my $now = strftime("%Y-%m-%dT%H:%M:%S", gmtime()) . 'Z';
    return $now;
}

sub publish_amqp ($self, $topic, $event_data, $headerframe = {}, $remaining_attempts = undef, $retry_delay = undef) {
    # note: the parent method has a retry mechanism which means that
    # if publication fails, *this* method will be re-run with
    # $headerframe populated, $remaining_attempts decremented and
    # $retry_delay increased
    # re-doing the wrap in this case is harmless as we ultimately
    # merge the newly-created frame with the passed-in one and give
    # the passed-in one priority
    my $sentat = _iso8601_now;
    my $messageid = create_uuid_string;
    # default fedora-messaging compliant header frame. Ridiculous
    # naming note: AMQP wire format has a header frame and then the
    # body. Inside the header frame *is a field called headers*. Yo
    # dawg, I heard you liked headers...fedora-messaging has specific
    # expectations for some other fields in the header frame, and for
    # some of the fields in the 'headers' field in the header frame.
    # Mojo::RabbitMQ::Client tends to call things that represent the
    # header frame "%headers" and "$headers", so that's fun.
    my %fullheaderframe = (
        headers => {
            fedora_messaging_severity   => 20,
            fedora_messaging_schema     => 'base.message',
            "sent-at"                   => $sentat,
        },
        content_encoding => 'utf-8',
        delivery_mode => 2,
        message_id => $messageid,
    );
    # merge in the passed header frame values to allow overriding
    %fullheaderframe = (%fullheaderframe, %$headerframe);
    # call parent method. it's vital that we pass through $remaining_attempts
    # to avoid an eternal loop
    $self->SUPER::publish_amqp($topic, $event_data, \%fullheaderframe, $remaining_attempts, $retry_delay);
}

sub log_event_fedora_ci_messages {
    # this is for publishing messages in the "CI Messages" format:
    # https://pagure.io/fedora-ci/messages
    # This is a Fedora/Red Hat-ish thing in a way, but in theory
    # anyone could adopt it
    my ($self, $event, $job, $baseurl) = @_;
    my $stdevent;
    my $clone_of;
    my $job_id;
    # first, get the standard 'state' (from 'queued', 'running',
    # 'complete', 'error'; we cannot do 'running' at present
    if ($event eq 'openqa_job_create') {
        $stdevent = 'queued';
        $job_id   = $job->id;
    }
    elsif ($event eq 'openqa_job_restart' || $event eq 'openqa_job_duplicate') {
        $stdevent = 'queued';
        $clone_of = $job->id;
        $job_id   = $job->clone_id;
    }
    elsif ($event eq 'openqa_job_cancel') {
        $stdevent = 'error';
        $job_id   = $job->id;
    }
    elsif ($event eq 'openqa_job_done') {
        $job_id = $job->id;
        # lifecycle note: any job cancelled directly via the web API will
        # see both job_cancel and job_done with result USER_CANCELLED, so
        # we emit duplicate standardized fedmsgs in this case. This is
        # kinda unavoidable, though, as it's possible for a job to wind up
        # USER_CANCELLED *without* an openqa_job_cancel event happening,
        # so we can't just throw away all openqa_job_done USER_CANCELLED
        # events...
        $stdevent = (grep { $job->result eq $_ } COMPLETE_RESULTS) ? 'complete' : 'error';
    }
    else {
        return undef;
    }

    # we need this for the system dict; it should be the release of
    # the system-under-test (the VM in which the test runs) at the
    # *start* of the test, I think. We're trying to capture info about
    # the environment in which the test runs
    my $sysrelease = $job->VERSION;
    my $hdd1;
    my $bootfrom;
    $hdd1     = $job->settings_hash->{HDD_1}    if ($job->settings_hash->{HDD_1});
    $bootfrom = $job->settings_hash->{BOOTFROM} if ($job->settings_hash->{BOOTFROM});
    if ($hdd1 && $bootfrom) {
        $sysrelease = $1 if ($hdd1 =~ /disk_f(\d+)/ && $bootfrom eq 'c');
    }

    # next, get the 'artifact' (type of thing we tested)
    my $artifact;
    my $artifact_alias;
    my $artifact_builds;
    my $artifact_id;
    my $artifact_release;
    my $compose_type;
    my $test_namespace;
    # current date/time in ISO 8601 format
    my $generated_at = _iso8601_now;

    # this is used as a 'pipeline ID', see
    # https://pagure.io/fedora-ci/messages/blob/master/f/schemas/pipeline.yaml
    my $pipeid = join('.', "openqa", $job->BUILD, $job->TEST, $job->MACHINE, $job->FLAVOR, $job->ARCH);

    my $build = $job->BUILD;
    if ($build =~ /^Fedora/) {
        $artifact       = 'productmd-compose';
        $artifact_id    = $build;
        $compose_type   = 'production';
        $compose_type   = 'nightly' if ($build =~ /\.n\./);
        $compose_type   = 'test' if ($build =~ /\.t\./);
        $test_namespace = 'compose';
    }
    elsif ($build =~ /^Update-FEDORA/) {
        $artifact    = 'fedora-update';
        $artifact_alias = $build;
        $artifact_alias =~ s/^Update-//;
        $artifact_release = {
            version => $job->VERSION,
            name => "F" . $job->VERSION
        };
        # handle old-style single ADVISORY_NVRS with all NVRs
        my @nvrs = split(/ /, $job->settings_hash->{ADVISORY_NVRS} || '');
        unless (@nvrs) {
            # handle new-style chunked ADVISORY_NVRS_N settings
            my $count = 1;
            while ($count) {
                if ($job->settings_hash->{"ADVISORY_NVRS_$count"}) {
                    push @nvrs, split(/ /, $job->settings_hash->{"ADVISORY_NVRS_$count"});
                    $count++;
                }
                else {
                    $count = 0;
                }
            }
            unless (@nvrs) {
                log_error "ADVISORY_NVRS(_N) not found for update test $job_id! Cannot publish!";
                return;
            }
        }
        @nvrs = sort(@nvrs);
        my @builds;
        my $id = '';
        foreach my $nvr (@nvrs) {
            push @builds, {'nvr' => $nvr};
            $id .= $nvr;
        }
        $artifact_builds = \@builds;
        $artifact_id = 'sha256:' . sha256_hex($id);
        $test_namespace   = 'update';
    }
    else {
        # unhandled artifact type
        return undef;
    }

    # finally, construct the message content
    my %msg_data = (
        contact => {
            name  => 'Fedora openQA',
            team  => 'Fedora QA',
            url   => $baseurl,
            docs  => 'https://fedoraproject.org/wiki/OpenQA',
            irc   => '#fedora-qa',
            email => 'qa-devel@lists.fedoraproject.org',
        },
        run => {
            url => "$baseurl/tests/$job_id",
            log => "$baseurl/tests/$job_id/file/autoinst-log.txt",
            id  => $job_id,
        },
        artifact => {
            type => $artifact,
            id   => $artifact_id,
        },
        pipeline => {
            # per https://pagure.io/fedora-ci/messages/issue/61 this
            # is meant to be unique per test scenario *and* artifact,
            # so we construct it out of BUILD and the scenario keys.
            # 'name' is supposed to be a 'human readable name', well,
            # this is human readable, so we'll just use it twice
            id   => $pipeid,
            name => $pipeid,
        },
        test => {
            # openQA tests are pretty much always validation
            category => 'validation',
            # test identifier: test name plus scenario keys
            type      => join(' ', $job->TEST, $job->MACHINE, $job->FLAVOR, $job->ARCH),
            namespace => $test_namespace,
        },
        system => [
            {
                # it's interesting whether we should record info on the
                # *worker host itself* or the *SUT* (the VM run on top of
                # the worker host environment) here...on the whole I think
                # SUT is more in line with expectations, so let's do that
                os => "fedora-${sysrelease}",
                # openqa provisions itself...we *could* I guess set this
                # to 'createhdds' if we booted a disk image, but ehhhh
                provider     => 'openqa',
                architecture => $job->ARCH,
            },
        ],
        generated_at => $generated_at,
        version      => "0.2.1",
    );

    # add keys that don't exist in all cases to the message
    if ($stdevent eq 'complete') {
        $msg_data{test}{result} = $job->result;
        $msg_data{test}{result} = 'info' if $job->result eq 'softfailed';
    }
    elsif ($stdevent eq 'error') {
        $msg_data{error} = {};
        $msg_data{error}{reason} = $job->result;
    }
    elsif ($stdevent eq 'queued') {
        # this is a hint to consumers that the job probably went away
        # if they don't get a 'complete' or 'error' in 4 hours
        # FIXME: we should set this as 2 hours on 'running', but we
        # can't emit running because there is no internal event for
        # it, there is no job_running event or anything like it -
        # this is part of https://progress.opensuse.org/issues/31069
        $msg_data{test}{lifetime} = 240;
    }
    $msg_data{run}{clone_of} = $clone_of if ($clone_of);

    $msg_data{artifact}{release} = $artifact_release if ($artifact_release);
    $msg_data{artifact}{builds} = $artifact_builds if ($artifact_builds);
    $msg_data{artifact}{alias} = $artifact_alias if ($artifact_alias);

    $msg_data{artifact}{compose_type} = $compose_type if ($compose_type);

    my $subvariant = $job->settings_hash->{SUBVARIANT} || '';
    $msg_data{system}[0]{variant} = $subvariant if ($subvariant);

    # record info about the image tested, for compose tests. In theory
    # we might test more than one image in a job, which would break
    # the schema. But we don't do that yet fortunately
    if ($artifact eq 'productmd-compose') {
        # this is a handy variable which indicates what the 'thing'
        # the test really tests is (also used for resultsdb)
        my $target = $job->settings_hash->{TEST_TARGET} || '';
        my $imgname = $job->settings_hash->{"$target"} || '';
        if ($imgname) {
            $msg_data{image} = {
                id   => $imgname,
                name => $imgname,
                type => $target
            };
        }
    }

    # create the topic
    my $topic = "ci.$artifact.test.$stdevent";

    # prepend the prefix (kinda duplicated with parent log_event)
    my $prefix = $self->{config}->{amqp}{topic_prefix};
    $topic     = $prefix . '.' . $topic if ($prefix);

    # finally, send the message
    log_debug("Sending CI Messages AMQP message for $event");
    # FIXME: we should set fedora_messaging_schema header here, but the
    # ci-messages schemas are not currently provided as fedora-messaging
    # Python classes anywhere, so we kinda can't. See:
    # https://pagure.io/fedora-ci/messages/issue/33
    $self->publish_amqp($topic, \%msg_data);
}

sub on_job_event {
    # do just enough work to send the 'CI messaging' spec message
    # (unfortunately a bit of duplication is inevitable)
    my ($self, $args) = @_;
    my ($user_id, $connection_id, $event, $event_data) = @$args;
    my $jobs = $self->{app}->schema->resultset('Jobs');
    my $job  = $jobs->find({id => $event_data->{id}});
    my $baseurl = $self->{config}->{global}->{base_url} || "http://UNKNOWN";
    $self->log_event_fedora_ci_messages($event, $job, $baseurl);
    # call parent method to send 'native' message
    $self->SUPER::on_job_event($args);
}

1;
