%global source0_hash 9d60d9648c35ce2754731eb4deb7f05809ece1bd633b74d74795aed9ec732570

# Supported rpmbuild options:
#
# --with email_tests ... also check sending e-mails.
#     Default: --without (Exclude e-mail tests)
%bcond_with     release_tests
# --without httpd ... do not build ApacheLog logging output for httpd.
#     Default: --with (Build ApacheLog)
%if 0%{?rhel} >= 9
%bcond_with     httpd
%else
%bcond_without     httpd
%endif
# --with release_tests ... also check "RELEASE_TESTS".
#     Default: --without (Exclude tests)
%bcond_with     release_tests

Name:           perl-Log-Dispatch
Version:        2.71
Release:        8%{?dist}
Summary:        Dispatches messages to one or more outputs
License:        Artistic-2.0
URL:            https://metacpan.org/release/Log-Dispatch
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Apache2::Log not used at tests
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
#BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(lib)
BuildRequires:  perl(Mail::Send)
BuildRequires:  perl(Mail::Sender)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(parent)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio) >= 0.32
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog) >= 0.28
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# Optional
BuildRequires:  perl(CPAN::Meta) >= 2.120900

# testsuite
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)

# If LOG_DISPATCH_TEST_EMAIL is passed to tests, a sendmail will be needed,
# bug #1083418
BuildRequires:  %{_sbindir}/sendmail

%if %{with release_tests} 
# for improved tests
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Spelling)
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Mojibake)
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Version)
BuildRequires:  perl(Test::Code::TidyAll) > 0.24

# Required by t/release-pod-no404s.t
# Likely a bug underneath of Test::Pod::No404s
BuildRequires:  perl(LWP::Protocol::https)
%endif

# Ouch - Introduced by upstream in 2.40
Conflicts:      perl(Log::Dispatch::File::Stamped) >= 0.10


Provides:       perl(Log::Dispatch)
Provides:       perl(Log::Dispatch::Screen)
Provides:       perl(Log::Dispatch::File)
Provides:       perl(Log::Dispatch::Syslog)
Provides:       perl(Log::Dispatch::Output)
%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level.  It is designed to be easily subclassed, both for creating a
new dispatcher object and particularly for creating new outputs.
An Apache output is available in perl-Log-Dispatch-ApacheLog package.

%if %{with httpd}
%package ApacheLog
Summary:        Log::Dispatch output for logging to Apache::Log objects
Requires:       %{name} = %{?epoch:%{epocho}:}%{version}-%{release}
Requires:       perl(Apache2::Log)
Conflicts:      perl-Log-Dispatch < 2.70-2

%description ApacheLog
This Perl module enables you to pass messages to Apache's log object,
represented by the Apache::Log class.
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Log-Dispatch-%{version}

%build
%{__perl} Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test %{?with_release_tests:RELEASE_TESTING=1} \
    %{?with_email_tests:LOG_DISPATCH_TEST_EMAIL="root@localhost.localdomain"}

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Log/
%exclude %{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%{_mandir}/man3/*.3pm*
%exclude %{_mandir}/man3/Log::Dispatch::ApacheLog.3pm*

%if %{with httpd}
%files ApacheLog
%{perl_vendorlib}/Log/Dispatch/ApacheLog.pm
%{_mandir}/man3/Log::Dispatch::ApacheLog.3pm*
%endif

%changelog
%autochangelog
