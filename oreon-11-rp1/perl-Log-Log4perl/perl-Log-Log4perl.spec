%global source0_hash 0f8fcb7638a8f3db4c797df94fdbc56013749142f2f94cbc95b43c9fca096a13
%bcond_without RRD
Name:           perl-Log-Log4perl
Version:        1.57
Release:        1%{?dist}
Summary:        Log4j implementation for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Log4perl
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/Log-Log4perl-%{version}.tar.gz
BuildArch:      noarch
%if %{with RRD}
%endif
Requires:       perl(Encode)
Requires:       perl(Net::LDAP)
Requires:       perl(Safe)
Requires:       perl(Sys::Hostname)
Requires:       perl(Time::HiRes)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Log4perlInternalTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(L4pResurrectable\\)
Provides:       perl(Log::Log4perl)
Provides:       perl(Log::Log4perl::Level)
Provides:       perl(Log::Log4perl::Layout::PatternLayout)
Provides:       perl(Log::Log4perl::Layout::SimpleLayout)
Provides:       perl(Log::Log4perl::Appender::File)
Provides:       perl(Log::Log4perl::Appender::Screen)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Semaphore)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::FileRotate)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Log::Dispatch::Syslog)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RRDs)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a eg t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Log-Log4perl-Appender-DBI -f %{oreon_filedir}/perl-Log-Log4perl-Appender-DBI.list
%files -n perl-Log-Log4perl-Appender-RRDs -f %{oreon_filedir}/perl-Log-Log4perl-Appender-RRDs.list
%files -n perl-Log-Log4perl-Config-DOMConfigurator -f %{oreon_filedir}/perl-Log-Log4perl-Config-DOMConfigurator.list
%files -n perl-Log-Log4perl-tests -f %{oreon_filedir}/perl-Log-Log4perl-tests.list

%changelog

%autochangelog
