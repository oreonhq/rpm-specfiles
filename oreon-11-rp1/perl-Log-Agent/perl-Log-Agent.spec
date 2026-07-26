%global source0_hash 7f4732279e4f79d17aa8b9983575c439a57e4dd5fed4ff29f9d13aacf8312eff

# Disable support for Carp-Datum because it is Artistic 1 only, CPAN RT#105332
%bcond_with datum
# Perform optional tests
%bcond_without perl_Log_Agent_enables_optional_test

Name:           perl-Log-Agent
Version:        1.005
Release:        15%{?dist}
Summary:        Logging agent
License:        Artistic-2.0
URL:            https://metacpan.org/release/Log-Agent
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
# Carp::Datum not needed at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Mail::Mailer not needed at tests
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Sys::Syslog not needed at tests
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_Log_Agent_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Callback)
%endif
Requires:       perl(warnings)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(\\.::t/

%description
The Log::Agent Perl module provides an abstract layer for logging and tracing,
which is independent from the actual method used to physically perform those
activities. It acts as an agent (hence the name) that collects the requests
and delegates processing to a logging driver.

%if %{with datum}
%package Carp-Datum
Summary:        Carp::Datum driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Carp)
Requires:       perl(Carp::Datum)

%description Carp-Datum
The purpose of this logging driver is to cooperate with Carp::Datum by emitting
traces to the debug channel via Carp::Datum's traces facilities.
%endif

%package mail
Summary:        E-mail driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description mail
This logging driver maps the log calls to email messages.  Each call generates
a separate email message.

%package syslog
Summary:        Syslog driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Carp)

%description syslog
This logging driver delegates log operations to syslog() via the
Sys::Syslog interface.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Log_Agent_enables_optional_test}
Requires:       perl(Callback)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Agent-%{version}
# Fix end of lines
perl -i -pe 's/\r\n/\n/' CHANGELOG.md README
%if !%{with perl_Log_Agent_enables_optional_test}
rm t/tag_callback.t
perl -i -ne 'print $_ unless m{\A\Qt/tag_callback.t\E}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# The tests are not parallel-safe, they overwrite files in CWD, CPAN RT#113812
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
prove -I . -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# The tests are not parallel-safe, they overwrite files in CWD, CPAN RT#113812
make test

%files
%doc CHANGELOG.md README
%{perl_vendorlib}/*
%{_mandir}/man3/*
# Carp-Datum
%exclude %{perl_vendorlib}/Log/Agent/Driver/Datum.pm
%exclude %{_mandir}/man3/Log::Agent::Driver::Datum.*
# mail
%exclude %{perl_vendorlib}/Log/Agent/Driver/Mail.pm
%exclude %{_mandir}/man3/Log::Agent::Driver::Mail.*
# syslog
%exclude %{perl_vendorlib}/Log/Agent/Channel/Syslog.pm
%exclude %{perl_vendorlib}/Log/Agent/Driver/Syslog.pm
%exclude %{_mandir}/man3/Log::Agent::Channel::Syslog.*
%exclude %{_mandir}/man3/Log::Agent::Driver::Syslog.*

%if %{with datum}
%files Carp-Datum
%{perl_vendorlib}/Log/Agent/Driver/Datum.pm
%{_mandir}/man3/Log::Agent::Driver::Datum.*
%endif

%files mail
%{perl_vendorlib}/Log/Agent/Driver/Mail.pm
%{_mandir}/man3/Log::Agent::Driver::Mail.*

%files syslog
%{perl_vendorlib}/Log/Agent/Channel/Syslog.pm
%{perl_vendorlib}/Log/Agent/Driver/Syslog.pm
%{_mandir}/man3/Log::Agent::Channel::Syslog.*
%{_mandir}/man3/Log::Agent::Driver::Syslog.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
