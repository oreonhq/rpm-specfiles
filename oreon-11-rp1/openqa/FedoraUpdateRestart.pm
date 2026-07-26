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

package OpenQA::WebAPI::Plugin::FedoraUpdateRestart;

use strict;
use warnings;

use parent 'Mojolicious::Plugin';
use Mojo::IOLoop;
use OpenQA::Events;
use OpenQA::Schema::Result::Jobs;

sub register {
    my ($self, $app) = @_;
    OpenQA::Events->singleton->on("openqa_job_done" => sub { shift; $self->on_job_done($app, @_) });
}

# when a job completes, if it's an update test, it failed, and it's
# not already a clone, restart it.
# Also restart all aarch64 install jobs that fail in the first test
# module, due to https://bugzilla.redhat.com/show_bug.cgi?id=1689037,
# which seems very common on aarch64
# We could use the `dup_type_auto` behaviour, but that allows 3
# restarts, which is kinda a lot.
sub on_job_done {
    my ($self, $app, $args) = @_;
    my ($user_id, $connection_id, $event, $event_data) = @$args;
    my $schema = $app->schema;
    my $jobid = $event_data->{id};
    OpenQA::Utils::log_debug("Update restarter considering job $jobid");
    my $job = $schema->resultset('Jobs')->find({id => $jobid});
    my @jobmodules = $job->modules_with_job_prefetched->all;
    my $firstmodule = $jobmodules[0];
    my $clone_of = $schema->resultset("Jobs")->find({clone_id => $jobid});
    my $restart = "";
    $restart = "update" if (
            $job->result eq OpenQA::Schema::Result::Jobs::FAILED && !$clone_of &&
            $job->FLAVOR =~ /^updates-/
    );
    $restart = "aarch64 install" if (
            $job->result eq OpenQA::Schema::Result::Jobs::FAILED && !$clone_of &&
            $job->TEST =~/^install_/ &&
            $firstmodule->result eq OpenQA::Schema::Result::Jobs::FAILED
    );
    if ($restart) {
        OpenQA::Utils::log_info("Update restarter restarting job $jobid: $restart");
        $job->auto_duplicate;
    }
}

1;
