%global source0_hash f747e6575fc68f5811b655ee51674593ff9e90f6016142f2764a8cd3f0ef4fc9

# Run optional test
%bcond_without perl_Log_Report_enables_optional_test

Name:           perl-Log-Report
Version:        1.44
Release:        2%{?dist}
Summary:        Report a problem with exceptions and translation support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Report
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Log-Report-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
# DBIx::Class::Storage::Statistics not used at tests
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
BuildRequires:  perl(Encode) >= 2.00
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch) >= 2.00
BuildRequires:  perl(Log::Log4perl)
# Makefile.PL states Log::Report::Optional 1.07 for contained
# Log::Report::{Minimal::Domain,Util}
BuildRequires:  perl(Log::Report::Minimal::Domain) >= 1.07
BuildRequires:  perl(Log::Report::Util) >= 1.07
%if %{with perl_Log_Report_enables_optional_test}
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Log)
%endif
BuildRequires:  perl(Moo)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# String::Print 1.00 is not used
BuildRequires:  perl(Sys::Syslog) >= 0.27
# Time::HiRes not used at tests
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.00
%if %{with perl_Log_Report_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Log4perl) >= 1.00
BuildRequires:  perl(Mojolicious) >= 2.16
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Error)
%endif
Requires:       perl(Devel::GlobalDestruction) >= 0.09
Requires:       perl(Encode) >= 2.00
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:       perl(Log::Report::Minimal::Domain) >= 1.07
Requires:       perl(Log::Report::Util) >= 1.07
Requires:       perl(overload)
# Removed from perl-Log-Report-1.42 upstream, their dependency on exact
# perl-Log-Report version would break an upgrade.
# The two packages will be replaced with perl-Dancer2-Plugin-LogReport
# SRPM once packaged.
Obsoletes:      perl-Log-Report-Dancer < 1.42
Obsoletes:      perl-Log-Report-Dancer2 < 1.42

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Devel::GlobalDestruction|Encode|Log::Report::Minimal::Domain|Log::Report::Util|Sys::Syslog|Test::More)\\)$

# Remove private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DieTests\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DieTests\\)

%description
Handling messages directed to users can be a hassle, certainly when the same
software is used for command-line and in a graphical interfaces (you may not
know how it is used), or has to cope with internationalization; these modules
try to simplify this.

%package DBIC
Summary:    Query profiler for DBIx::Class
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}

%description DBIC
Log DBIx::Class queries via Log::Report.

%package Dispatcher-Log4perl
Summary:    Log::Log4perl back-end for Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:   perl(Log::Report::Util) >= 1.03

%description Dispatcher-Log4perl
This is an optional Log::Log4perl back-end for Log::Report logging framework.

%package Dispatcher-LogDispatch
Summary:    Log::Dispatch back-end for Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:   perl(Log::Report::Util) >= 1.03

%description Dispatcher-LogDispatch
This is an optional Log::Dispatch back-end for Log::Report logging framework.

%package Dispatcher-Syslog
Summary:    Sys::Syslog back-end for Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
Requires:   perl(Encode) >= 2.00
Requires:   perl(Sys::Syslog) >= 0.27
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:   perl(Log::Report::Util) >= 1.03

%description Dispatcher-Syslog
This is an optional Sys::Syslog back-end for Log::Report logging framework.

%package Mojo
Summary:    Divert log messages into Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
Requires:   perl(Mojo::Log)

%description Mojo
Mojo likes to log messages directly into a file, by default. This is a Mojo
extension that can route Mojo messages into Log::Report logging framework.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 1.00
Requires:       perl(Log::Report::Dispatcher::Callback)
Requires:       perl(Log::Report::Dispatcher::File)
Requires:       perl(Log::Report::Dispatcher::Log4perl)
Requires:       perl(Log::Report::Dispatcher::LogDispatch)
Requires:       perl(Log::Report::Dispatcher::Perl)
Requires:       perl(Log::Report::Dispatcher::Syslog)
Requires:       perl(Log::Report::Dispatcher::Try)
Requires:       perl(Log::Report::Domain)
Requires:       perl(Log::Report::Exception)
Requires:       perl(Log::Report::Translator)
%if %{with perl_Log_Report_enables_optional_test}
Requires:       perl(Log::Dispatch::File)
Requires:       perl(Log::Log4perl) >= 1.00
Requires:       perl(Mojolicious) >= 2.16
Requires:       perl(MojoX::Log::Report)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXML::Error)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Log-Report-%{version}
%if !%{with perl_Log_Report_enables_optional_test}
rm t/60mojo.t
perl -i -ne 'print $_ unless m{^t/60mojo\.t\b}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
# README is a subset of README.md
%doc ChangeLog README.md
%dir %{perl_vendorlib}/Log
%{perl_vendorlib}/Log/Report
%{perl_vendorlib}/Log/Report.pod
%{perl_vendorlib}/Log/Report.pm
%exclude %{perl_vendorlib}/Log/Report/DBIC
%exclude %{perl_vendorlib}/Log/Report/Dispatcher/Log4perl.*
%exclude %{perl_vendorlib}/Log/Report/Dispatcher/LogDispatch.*
%exclude %{perl_vendorlib}/Log/Report/Dispatcher/Syslog.*
%{_mandir}/man3/Log::Report.*
%{_mandir}/man3/Log::Report::*
%exclude %{_mandir}/man3/Log::Report::DBIC::Profiler.*
%exclude %{_mandir}/man3/Log::Report::Dispatcher::Log4perl.*
%exclude %{_mandir}/man3/Log::Report::Dispatcher::LogDispatch.*
%exclude %{_mandir}/man3/Log::Report::Dispatcher::Syslog.*

%files DBIC
%{perl_vendorlib}/Log/Report/DBIC
%{_mandir}/man3/Log::Report::DBIC::Profiler.*

%files Dispatcher-Log4perl
%{perl_vendorlib}/Log/Report/Dispatcher/Log4perl.*
%{_mandir}/man3/Log::Report::Dispatcher::Log4perl.*

%files Dispatcher-LogDispatch
%{perl_vendorlib}/Log/Report/Dispatcher/LogDispatch.*
%{_mandir}/man3/Log::Report::Dispatcher::LogDispatch.*

%files Dispatcher-Syslog
%{perl_vendorlib}/Log/Report/Dispatcher/Syslog.*
%{_mandir}/man3/Log::Report::Dispatcher::Syslog.*

%files Mojo
%{perl_vendorlib}/MojoX
%{_mandir}/man3/MojoX::Log::Report.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
