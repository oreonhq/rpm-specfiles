%global source0_hash 0f8fcb7638a8f3db4c797df94fdbc56013749142f2f94cbc95b43c9fca096a13

%bcond_without RRD

Name:           perl-Log-Log4perl
Version:        1.57
Release:        9%{?dist}
Summary:        Log4j implementation for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Log4perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Log-Log4perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Semaphore)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::FileRotate) >= 1.10
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Log::Dispatch::Syslog)
BuildRequires:  perl(POSIX)
%if %{with RRD}
BuildRequires:  perl(RRDs)
%endif
BuildRequires:  perl(Safe)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
# Term::ANSIColor is not needed for runing tests
# Time::HiRes is not needed for runing the tests
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::DOM) >= 1.29
# Tests
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(fields)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(utf8)
# Optional tests
%if ! (0%{?rhel} >= 7)
BuildRequires:  perl(DBD::CSV) >= 0.33
BuildRequires:  perl(DBI) >= 1.607
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(SQL::Statement) >= 1.20
BuildRequires:  perl(Sys::Syslog)
%endif
Requires:       perl(Encode)
Requires:       perl(Net::LDAP)
Requires:       perl(Safe)
Requires:       perl(Sys::Hostname)
Requires:       perl(Time::HiRes)

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Log4perlInternalTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(L4pResurrectable\\)

Provides:       perl(Log::Log4perl)
Provides:       perl(Log::Log4perl::Level)
Provides:       perl(Log::Log4perl::Layout::PatternLayout)
Provides:       perl(Log::Log4perl::Layout::SimpleLayout)
Provides:       perl(Log::Log4perl::Appender::File)
Provides:       perl(Log::Log4perl::Appender::Screen)
%description
Log::Log4perl lets you remote-control and fine-tune the logging
behavior of your system from the outside. It implements the widely
popular (Java-based) Log4j logging package in pure Perl.

To log into RRD database, install perl-Log-Log4perl-Appender-RRDs package.
To log into a database via DBI, install perl-Log-Log4perl-Appender-DBI package.

To read log4j XML configuration files, install
perl-Log-Log4perl-Config-DOMConfigurator package.

%package Appender-DBI
Summary:        Log to a database
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name} < 1.46-2

%description Appender-DBI
Log::Log4perl::Appender::DBI appender facilitates writing data to a database
using DBI interface via Log4perl.

%if %{with RRD}
%package Appender-RRDs
Summary:        Log to a RRDtool archive
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name} < 1.46-2

%description Appender-RRDs
Log::Log4perl::Appender::RRDs appender facilitates writing data to
RRDtool round-robin archives via Log4perl.
%endif

%package Config-DOMConfigurator
Summary:        Read log4j XML configuration files
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name} < 1.46-2

%description Config-DOMConfigurator
Log::Log4perl::Config::DOMConfigurator adds support for log4j XML
configuration files to Log::Log4perl Perl logging system.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Filter::Util::Call)
# Optional tests
%if ! (0%{?rhel} >= 7)
Requires:       perl(DBD::CSV) >= 0.33
Requires:       perl(DBI) >= 1.607
Requires:       perl(Log::Dispatch)
Requires:       perl(SQL::Statement) >= 1.20
Requires:       perl(Sys::Syslog)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Log-Log4perl-%{version}
find lib -name '*.pm' -exec chmod -c a-x {} +
perl -MConfig -pi -e 's|^#!/usr/local/bin/perl|$Config{startperl}|' \
    eg/newsyslog-test eg/benchmarks/simple

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a eg t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Shared memory tests guarded with L4P_ALL_TESTS fail in mock.
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm
%exclude %{perl_vendorlib}/Log/Log4perl/Appender/DBI.pm
%exclude %{perl_vendorlib}/Log/Log4perl/Config/DOMConfigurator.pm
%exclude %{perl_vendorlib}/Log/Log4perl/JavaMap/JDBCAppender.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Log::Log4perl::Appender::RRDs.*
%exclude %{_mandir}/man3/Log::Log4perl::Appender::DBI.*
%exclude %{_mandir}/man3/Log::Log4perl::Config::DOMConfigurator.*
%exclude %{_mandir}/man3/Log::Log4perl::JavaMap::JDBCAppender.*
%{_bindir}/*

%files Appender-DBI
%{perl_vendorlib}/Log/Log4perl/Appender/DBI.pm
%{perl_vendorlib}/Log/Log4perl/JavaMap/JDBCAppender.pm
%{_mandir}/man3/Log::Log4perl::Appender::DBI.*
%{_mandir}/man3/Log::Log4perl::JavaMap::JDBCAppender.*

%if %{with RRD}
%files Appender-RRDs
%{perl_vendorlib}/Log/Log4perl/Appender/RRDs.pm
%{_mandir}/man3/Log::Log4perl::Appender::RRDs.*
%endif

%files Config-DOMConfigurator
%{perl_vendorlib}/Log/Log4perl/Config/DOMConfigurator.pm
%{_mandir}/man3/Log::Log4perl::Config::DOMConfigurator.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
