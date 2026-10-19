%global source0_hash 2aff1918e25c4cd4d7f6462c70f3e95e5bb02a43cc028193bca4949b8dde861f
%global __provides_exclude_from %{_datadir}/openqa/lib
%global __requires_exclude perl\\((OpenQA|DBIx::Class::Timestamps|MojoDebugHandle|db_helpers|db_profiler|Perl::Critic)
%{?perl_default_filter}
%global github_owner    os-autoinst
%global github_name     openQA
%global github_version  5
%global github_commit   19189f0ef4b285279f0492a5c5f4ded6304984b0
%global github_date     20260126
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})
%global openqa_main_service openqa-webui.service
%global openqa_extra_services openqa-gru.service openqa-websockets.service openqa-scheduler.service openqa-enqueue-audit-event-cleanup.service openqa-enqueue-audit-event-cleanup.timer openqa-enqueue-asset-cleanup.service openqa-enqueue-git-auto-update.service openqa-enqueue-asset-cleanup.timer openqa-enqueue-result-cleanup.service openqa-enqueue-result-cleanup.timer openqa-enqueue-bug-cleanup.service openqa-enqueue-bug-cleanup.timer openqa-enqueue-git-auto-update.timer openqa-enqueue-needle-ref-cleanup.service openqa-enqueue-needle-ref-cleanup.timer openqa-enqueue-scheduled-product-cleanup.service openqa-enqueue-scheduled-product-cleanup.timer
%global openqa_services %{openqa_main_service} %{openqa_extra_services}
%global openqa_worker_services openqa-worker.target openqa-slirpvde.service openqa-vde_switch.service openqa-worker-cacheservice.service openqa-worker-cacheservice-minion.service
%global openqa_localdb_services openqa-setup-db.service openqa-dump-db.service openqa-dump-db.timer
%if %{undefined tmpfiles_create}
%global tmpfiles_create() \
%{_bindir}/systemd-tmpfiles --create %{?*} >/dev/null 2>&1 || :
%{nil}
%endif
%define python_scripts_requires python3-requests openqa-client
%define assetpack_requires perl(CSS::Minifier::XS) >= 0.01 perl(JavaScript::Minifier::XS) >= 0.11 perl(Mojolicious) perl(Mojolicious::Plugin::AssetPack) >= 1.36 perl(YAML::PP) >= 0.026
%define common_requires chrony perl-interpreter >= 5.20.0 perl(Carp::Always) >= 0.14.02 perl(Config::IniFiles) perl(Config::Tiny) perl(Cpanel::JSON::XS) >= 4.09 perl(Cwd) perl(Data::Dump) perl(Data::Dumper) perl(Digest::MD5) perl(Feature::Compat::Try) perl(Filesys::Df) perl(Getopt::Long) perl(Minion) >= 10.25 perl(Mojolicious) >= 9.34 perl(Regexp::Common) perl(Storable) perl(Text::Glob) perl(Time::Moment)
%define main_requires %assetpack_requires bsdcat bsdtar git-core hostname openssh-clients perl(BSD::Resource) perl(Carp) perl(CommonMark) perl(Config::Tiny) perl(DBD::Pg) >= 3.7.4 perl(DBI) >= 1.632 perl(DBIx::Class) >= 0.082801 perl(DBIx::Class::DeploymentHandler) perl(DBIx::Class::DynamicDefault) perl(DBIx::Class::OptimisticLocking) perl(DBIx::Class::ResultClass::HashRefInflator) perl(DBIx::Class::Schema::Config) perl(DBIx::Class::Storage::Statistics) perl(Date::Format) perl(DateTime) perl(DateTime::Duration) perl(DateTime::Format::Pg) perl(Exporter) perl(Fcntl) perl(File::Basename) perl(File::Copy) perl(File::Copy::Recursive) perl(File::Path) perl(File::Spec) perl(FindBin) perl(Getopt::Long::Descriptive) perl(IO::Handle) perl(IPC::Run) perl(JSON::Validator) perl(LWP::UserAgent) perl(Module::Load::Conditional) perl(Module::Pluggable) perl(Mojo::Base) perl(Mojo::ByteStream) perl(Mojo::IOLoop) perl(Mojo::JSON) perl(Mojo::Pg) perl(Mojo::RabbitMQ::Client) >= 0.2 perl(Mojo::URL) perl(Mojo::Util) perl(Mojolicious::Commands) perl(Mojolicious::Plugin) perl(Mojolicious::Plugin::OAuth2) perl(Mojolicious::Static) perl(Net::OpenID::Consumer) perl(POSIX) perl(Pod::POM) perl(SQL::Translator) perl(Scalar::Util) perl(Sort::Versions) perl(Text::Diff) perl(Time::HiRes) perl(Time::ParseDate) perl(Time::Piece) perl(Time::Seconds) perl(URI::Escape) perl(YAML::PP) >= 0.026 perl(YAML::XS) perl(aliased) perl(base) perl(constant) perl(diagnostics) perl(strict) perl(warnings)
%define client_requires curl git-core jq perl(Getopt::Long::Descriptive) perl(IO::Socket::SSL) >= 2.009 perl(IPC::Run) perl(JSON::Validator) perl(LWP::Protocol::https) perl(LWP::UserAgent) perl(Test::More) perl(YAML::PP) >= 0.020 perl(YAML::XS)
%define worker_requires bsdcat bsdtar openqa-client optipng os-autoinst perl(Capture::Tiny) perl(File::Map) perl(Minion::Backend::SQLite) >= 5.0.7 perl(Mojo::IOLoop::ReadWriteProcess) >= 0.26 perl(Mojo::SQLite) psmisc sqlite >= 3.24.0
%define mcp_requires %{nil}
%define build_requires %assetpack_requires rubygem(sass)
%define test_requires %common_requires %main_requires %mcp_requires %python_scripts_requires %worker_requires curl jq openssh os-autoinst perl(App::cpanminus) perl(Test::Exception) perl(Test::Fatal) perl(Test::MockModule) perl(Test::MockObject) perl(Test::Mojo) perl(Test::Most) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 perl(Syntax::Keyword::Try::Deparse) postgresql-server
%ifarch x86_64
%define qemu qemu qemu-kvm
%else
%define qemu qemu
%endif
%define style_check_requires ShellCheck perl(Code::TidyAll) perl(Perl::Critic) yamllint shfmt
%define cover_requires perl(Devel::Cover)
%define devel_no_selenium_requires %build_requires %cover_requires %qemu %style_check_requires %test_requires curl perl(Perl::Tidy) postgresql-devel rsync sudo tar
%define devel_requires %devel_no_selenium_requires
%bcond_without tests
Name:           openqa
Version:        %{github_version}%{?github_date:^%{github_date}git%{shortcommit}}
Release:        1%{?dist}
Summary:        OS-level automated testing framework
License:        GPL-2.0-or-later AND MIT AND BSD-3-Clause
Url:            http://os-autoinst.github.io/openQA/
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz
Source1:        assetcache-%{github_commit}.tar.xz
Source2:        FedoraUpdateRestart.pm
Source3:        FedoraMessaging.pm
Source4:        23-fedora-messaging.t
Source5:        geekotest.conf
Source6:        openQA-worker.conf
%if %{with tests}
%endif
Requires:       perl(Minion) >= 10.0
Requires:       %{main_requires}
Requires:       openqa-common = %{version}-%{release}
Requires:       openqa-client = %{version}-%{release}
Requires(post): coreutils
%{?systemd_requires}
%{?sysusers_requires_compat}
Recommends:     perl(Mojolicious::Plugin::OAuth2)
Recommends:     perl(IO::Uncompress::UnXz)
Recommends:     rsync
Recommends:     pngquant
Obsoletes:      openqa < 4.3-7
Provides:       bundled(nodejs-ace-builds) = 1.43.1
Provides:       bundled(nodejs-anser) = 2.3.2
Provides:       bundled(nodejs-bootstrap) = 5.3.7
Provides:       bundled(nodejs-chosen-js) = 1.8.7
Provides:       bundled(nodejs-d3) = 7.9.0
Provides:       bundled(nodejs-dagre-d3) = 0.6.4
Provides:       bundled(nodejs-datatables.net) = 2.3.2
Provides:       bundled(nodejs-datatables.net-bs5) = 2.3.2
Provides:       bundled(nodejs-fork-awesome) = 1.2.0
Provides:       bundled(nodejs-jquery) = 3.7.1
Provides:       bundled(nodejs-jquery-ujs) = 1.2.3
Provides:       bundled(nodejs-timeago) = 1.6.7
BuildArch:      noarch
# oreon:deps
BuildRequires:  bsdcat
BuildRequires:  bsdtar
BuildRequires:  chrony
BuildRequires:  curl
BuildRequires:  git-core
BuildRequires:  glibc-langpack-en
BuildRequires:  hostname
BuildRequires:  jq
BuildRequires:  make
BuildRequires:  openqa-client
BuildRequires:  openssh
BuildRequires:  openssh-clients
BuildRequires:  optipng
BuildRequires:  os-autoinst
BuildRequires:  perl(App::cpanminus)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(CSS::Minifier::XS)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(CommonMark)
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::DeploymentHandler)
BuildRequires:  perl(DBIx::Class::DynamicDefault)
BuildRequires:  perl(DBIx::Class::OptimisticLocking)
BuildRequires:  perl(DBIx::Class::ResultClass::HashRefInflator)
BuildRequires:  perl(DBIx::Class::Schema::Config)
BuildRequires:  perl(DBIx::Class::Storage::Statistics)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::Pg)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Map)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Filesys::Df)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::Validator)
BuildRequires:  perl(JavaScript::Minifier::XS)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Minion)
BuildRequires:  perl(Minion::Backend::SQLite)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::ByteStream)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::IOLoop::ReadWriteProcess)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Pg)
BuildRequires:  perl(Mojo::RabbitMQ::Client)
BuildRequires:  perl(Mojo::SQLite)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Commands)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Mojolicious::Plugin::AssetPack)
BuildRequires:  perl(Mojolicious::Plugin::OAuth2)
BuildRequires:  perl(Mojolicious::Static)
BuildRequires:  perl(Net::OpenID::Consumer)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Syntax::Keyword::Try::Deparse)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Strict)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Moment)
BuildRequires:  perl(Time::ParseDate)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(UUID::URandom)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  postgresql-server
BuildRequires:  psmisc
BuildRequires:  python3-requests
BuildRequires:  rubygem(sass)
BuildRequires:  sqlite
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
openQA is a testing framework that allows you to test GUI applications on one
hand and bootloader and kernel on the other. In both cases, it is difficult to
script tests and verify the output. Output can be a popup window or it can be
an error in early boot even before init is executed.

openQA is an automated test tool that makes it possible to test the whole
installation process of an operating system. It uses virtual machines to
reproduce the process, check the output (both serial console and screen) in
every step and send the necessary keystrokes and commands to proceed to the
next. openQA can check whether the system can be installed, whether it works
properly in 'live' mode, whether applications work or whether the system
responds as expected to different installation options and commands.

Even more importantly, openQA can run several combinations of tests for every
revision of the operating system, reporting the errors detected for each
combination of hardware configuration, installation options and variant of the
operating system.

%package devel
Summary:        Development package pulling in all build+test dependencies
Requires:       %{devel_requires}
%description devel
Development package pulling in all build+test dependencies.

%package common
Summary:        Common components for openQA server and workers
Requires:       %{common_requires}
Requires:       perl(DBIx::Class) >= 0.082801
Requires:       perl(Mojolicious::Plugin::AssetPack) >= 2.01
%description common
This package contains shared resources for the openQA server and
openQA workers.

%package worker
Summary:        The openQA worker
%define worker_requires_including_uncovered_in_tests %worker_requires perl(SQL::SplitStatement)
Requires:       %{worker_requires_including_uncovered_in_tests}
Requires:       openqa-common = %{version}-%{release}
Requires(post): coreutils
Requires(post): os-autoinst >= 4.6
Recommends:     qemu
Recommends:     rsync
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%description worker
The openQA worker manages the os-autoinst test engine. A system with
openqa-worker installed can run an arbitrary number of openQA workers
(as many as its hardware can support), each of which will run a single
openQA test job at a time, as long as appropriate jobs for the worker
are available from the server it is configured to work for.

%package httpd
Summary:        openQA httpd (Apache) integration
Requires:       httpd
Requires:       httpd-filesystem
Obsoletes:      openqa < 4.3-7
%description httpd
This package contains httpd (Apache) configuration for the openQA
automated testing framework. openQA runs as a self-contained http
server which is expected to be reverse-proxied by a public-facing http
server (rather than being accessed directly). The config snippets in
this package help you configure openQA to be reverse proxied by httpd.

%package plugin-fedora-messaging
Summary:        openQA plugin for publishing to fedora-messaging
Requires:       openqa >= 4.3-20
Requires:       perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA)
Requires:       perl(UUID::URandom)
BuildRequires:  perl(UUID::URandom)
Obsoletes:      %{name}-plugin-fedmsg < 4.7
Provides:       %{name}-plugin-fedmsg = %{version}-%{release}
%description plugin-fedora-messaging
This package contains an openQA plugin which sends fedora-messaging
messages for certain openQA internal events. To enable the plugin, put
'plugins = FedoraMessaging' in the global section of
/etc/openqa/openqa.ini. The plugin piggybacks on the upstream AMQP
plugin, and follows its configuration (in the 'amqp' section of
openqa.ini).

%package plugin-fedoraupdaterestart
Summary:        openQA plugin for restarting failed Fedora update tests
Requires:       openqa
%description plugin-fedoraupdaterestart
This package contains an openQA plugin which restarts update tests that
fail. This is a highly Fedora-specific plugin relying on the flavor
names used for update tests in Fedora. The idea is to re-run failed
tests in case the failure was something transient and unrelated to the
update (network issue, quasi-random bug in underlying package, etc.)

%package client
Summary:        Client tools for remote openQA management
Requires:       openqa-common = %{version}
Requires:       %client_requires
%description client
This package contains the openQA client script, along with several
other useful tools and support files. The client script is a convenient
helper for interacting with the openQA REST API.

%package python-scripts
Summary:        Additional scripts in python
Requires:       %python_scripts_requires
%description python-scripts
Additional scripts for the use of openQA in the python programming language.

%package local-db
Summary:        Helper package to ease setup of postgresql DB
Requires:       %{name} = %{version}
Requires:       postgresql-server
BuildRequires:  postgresql-server
Supplements:    packageand(%name:postgresql-server)
%description local-db
You only need this package if you have a local postgresql server
next to the webui.

%package single-instance
Summary:        Convenience package for a single-instance setup using apache proxy
Provides:       %{name}-single-instance-apache
Provides:       %{name}-single-instance-apache2
Requires:       %{name}-local-db
Requires:       %{name} = %{version}
Requires:       %{name}-worker = %{version}
Requires:       httpd
%description single-instance
Use this package to setup a local instance with all services provided together.

%package single-instance-nginx
Summary:        Convenience package for a single-instance setup using nginx proxy
Requires:       %{name}-local-db
Requires:       %{name} = %{version}
Requires:       %{name}-worker = %{version}
Requires:       nginx
%description single-instance-nginx
Use this package to setup a local instance with all services provided together.

%package bootstrap
Summary:        Automated openQA setup
Requires:       curl
Requires:       iputils
Requires:       procps
%description bootstrap
This can automatically setup openQA - either directly on your system
or within a systemd-nspawn container.

%package doc
Summary:        The openQA documentation
%description doc
Documentation material covering installation, configuration, basic test
writing, etc., covering both openQA and the os-autoinst test engine.

%package munin
Summary:        Munin scripts
Requires:       munin
Requires:       munin-node
Requires:       curl
Requires:       perl-interpreter
%description munin
Use this package to install munin scripts that allow to monitor some openQA
statistics.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{github_name}-%{github_commit} -a 1
sed -e 's,/bin/env python,/bin/python,' -i script/openqa-label-all
# Fedora calls it httpd.service, SUSE calls it apache2.service...
sed -i -e 's,apache2\.service,httpd\.service,g' systemd/*.service
# ...Fedora keeps httpd config here, SUSE keeps it there.
sed -i -e 's,"$(DESTDIR)"/etc/apache2/vhosts.d,"$(DESTDIR)"%{_sysconfdir}/httpd/conf.d,g' Makefile
sed -i -e 's,/etc/apache2/vhosts.d,%{_sysconfdir}/httpd/conf.d,g' etc/apache2/vhosts.d/*
# ...Fedora keeps nginx config here, SUSE keeps it there.
sed -i -e 's,"$(DESTDIR)"/etc/nginx/vhosts.d,"$(DESTDIR)"%{_sysconfdir}/nginx/conf.d,g' Makefile
# These are the Fedora-y standard TLS cert/key locations.
sed -i -e 's,/etc/apache2/ssl.crt,%{_sysconfdir}/pki/tls/certs,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.key,%{_sysconfdir}/pki/tls/private,g' etc/apache2/vhosts.d/*
# Add our downstream plugins to the sources
cp %{SOURCE2} lib/OpenQA/WebAPI/Plugin/
cp %{SOURCE3} lib/OpenQA/WebAPI/Plugin/
# we don't really need the tidy test
rm -f t/00-tidy.t
# we don't have the deps for the MCP feature yet
rm -f lib/OpenQA/WebAPI/Plugin/MCP.pm
rm -f t/api/17-mcp.t
# add the fedora-messaging publishing plugin test to the sources
cp %{SOURCE4} t/

%build

make %{?_smp_mflags}
%install
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
%make_install
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/openqa/script/client %{buildroot}%{_bindir}/openqa-client
ln -s %{_datadir}/openqa/script/openqa-cli %{buildroot}%{_bindir}/openqa-cli
ln -s %{_datadir}/openqa/script/openqa-clone-job %{buildroot}%{_bindir}/openqa-clone-job
ln -s %{_datadir}/openqa/script/openqa-dump-templates %{buildroot}%{_bindir}/openqa-dump-templates
ln -s %{_datadir}/openqa/script/openqa-load-templates %{buildroot}%{_bindir}/openqa-load-templates
ln -s %{_datadir}/openqa/script/openqa-clone-custom-git-refspec %{buildroot}%{_bindir}/openqa-clone-custom-git-refspec
ln -s %{_datadir}/openqa/script/openqa-validate-yaml %{buildroot}%{_bindir}/openqa-validate-yaml
ln -s %{_datadir}/openqa/script/setup-db %{buildroot}%{_bindir}/openqa-setup-db
ln -s %{_datadir}/openqa/script/dump-db %{buildroot}%{_bindir}/openqa-dump-db
ln -s %{_datadir}/openqa/script/openqa-label-all %{buildroot}%{_bindir}/openqa-label-all
install -d -m 755 %{buildroot}%{_datadir}/openqa/client
install -m 755 public/openqa-cli.yaml %{buildroot}%{_datadir}/openqa/client/openqa-cli.yaml
install -d -m 755 %{buildroot}/%{_datadir}/munin/plugins
install -m 755 contrib/munin/plugins/minion %{buildroot}/%{_datadir}/munin/plugins/openqa_minion_
install -d -m 755 %{buildroot}/%{_sysconfdir}/munin/plugin-conf.d
install -m 644 contrib/munin/config/minion.config %{buildroot}/%{_sysconfdir}/munin/plugin-conf.d/openqa-minion
install -m 755 contrib/munin/utils/munin-mail %{buildroot}/%{_datadir}/openqa/script/munin-mail
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/geekotest.conf
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/openQA-worker.conf
cd %{buildroot}
grep -rl %{_bindir}/env . | while read file; do
    sed -e 's,%{_bindir}/env perl,%{_bindir}/perl,' -i $file
done
rm -rf %{buildroot}%{_sysconfdir}/apparmor.d
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-auto-update
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-continuous-update
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-rollback
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-check-devel-repo
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-clean-repo-cache
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
rm -rf %{buildroot}/DB
export LC_ALL=en_US.UTF-8
touch openqa-debug.log autoinst-log.txt
chmod a+w openqa-debug.log autoinst-log.txt
sed -i -e 's,unshare -r -n ,,g' t/40-script_openqa-clone-custom-git-refspec.t
rm \
    t/01-test-utilities.t \
    t/17-labels_carry_over.t \
    t/25-cache-service.t
export CI=1
export OPENQA_TEST_TIMEOUT_SCALE_CI=15
export CONTAINER_TEST=0
export HELM_TEST=0
export PERL_TEST_WARNINGS_ONLY_REPORT_WARNINGS=1
make test GIT_CEILING_DIRECTORIES="/" CHECKSTYLE=0 PROVE_ARGS='-r t' TEST_PG_PATH=%{buildroot}/DB
rm -rf %{buildroot}/DB
%endif
%pre

%sysusers_create_compat %{SOURCE5}
%pre worker

%sysusers_create_compat %{SOURCE6}
%post

%tmpfiles_create %{_tmpfilesdir}/openqa-webui.conf
%systemd_post %{openqa_services}
%post worker

%tmpfiles_create %{_tmpfilesdir}/openqa.conf
%systemd_post %{openqa_worker_services}
%post httpd

if [ $1 -eq 1 ]; then
    echo "### copy and edit /etc/httpd/conf.d/openqa.conf.template if using apache!"
    echo "### copy and edit /etc/nginx/conf.d/openqa.conf.template if using nginx!"
fi
%preun

%systemd_preun %{openqa_services}
if [ $1 -eq 0 ]; then
   rm -rf %{_datadir}/openqa/public/packed
fi
%preun worker

%systemd_preun %{openqa_worker_services}
%postun

%systemd_postun_with_restart %{openqa_services}
%postun worker

%systemd_postun_with_restart %{openqa_worker_services}
%post local-db

%systemd_post %{openqa_localdb_services}
%preun local-db

%systemd_preun %{openqa_localdb_services}
%postun local-db

%systemd_postun_with_restart %{openqa_localdb_services}
%files -f %{oreon_filedir}/main.list
%files -n openqa-devel -f %{oreon_filedir}/openqa-devel.list
%files -n openqa-common -f %{oreon_filedir}/openqa-common.list
%files -n openqa-worker -f %{oreon_filedir}/openqa-worker.list
%files -n openqa-httpd -f %{oreon_filedir}/openqa-httpd.list
%files -n openqa-plugin-fedora-messaging -f %{oreon_filedir}/openqa-plugin-fedora-messaging.list
%files -n openqa-plugin-fedoraupdaterestart -f %{oreon_filedir}/openqa-plugin-fedoraupdaterestart.list
%files -n openqa-client -f %{oreon_filedir}/openqa-client.list
%files -n openqa-python-scripts -f %{oreon_filedir}/openqa-python-scripts.list
%files -n openqa-local-db -f %{oreon_filedir}/openqa-local-db.list
%files -n openqa-single-instance -f %{oreon_filedir}/openqa-single-instance.list
%files -n openqa-single-instance-nginx -f %{oreon_filedir}/openqa-single-instance-nginx.list
%files -n openqa-bootstrap -f %{oreon_filedir}/openqa-bootstrap.list
%files -n openqa-doc -f %{oreon_filedir}/openqa-doc.list
%files -n openqa-munin -f %{oreon_filedir}/openqa-munin.list

%changelog

%autochangelog
