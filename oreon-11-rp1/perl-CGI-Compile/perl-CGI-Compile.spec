%global source0_hash f6b0bae840260ee0b45a1a5be36e25b07ca91eedda264a83ce4f41483cb88ddd

# Perform optional tests
%bcond_without perl_CGI_Compile_enables_optional_test

Name:           perl-CGI-Compile
Summary:        Compile .cgi scripts to a code reference like ModPerl::Registry
Version:        0.27
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-%{version}.tar.gz 
URL:            https://metacpan.org/release/CGI-Compile
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Sub::Name)
# Tests:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
%if %{with perl_CGI_Compile_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-Plack → perl-CGI-Compile → perl-Plack
BuildRequires:  perl(CGI::Emulate::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Test)
%endif
BuildRequires:  perl(Sub::Identify)
# Test::Pod 1.41 not used
%endif

%{?perl_default_filter}

%description
CGI::Compile is an utility to compile CGI scripts into a code reference
that can run many times on its own namespace, as long as the script is
ready to run on a persistent environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Compile-%{version}

sed -i 's/\r//' t/data_crlf.cgi t/end_crlf.cgi
sed -i -e '1s,#!.*perl,#!/usr/bin/perl,' t/*.t

%build
/usr/bin/perl Build.PL --installdirs vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING AUTOMATED_TESTING
./Build test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
