%global source0_hash f6b0bae840260ee0b45a1a5be36e25b07ca91eedda264a83ce4f41483cb88ddd
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_CGI_Compile_enables_optional_test
Name:           perl-CGI-Compile
Summary:        Compile .cgi scripts to a code reference like ModPerl::Registry
Version:        0.27
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-%{version}.tar.gz
URL:            https://metacpan.org/release/CGI-Compile
BuildArch:      noarch
%if %{with perl_CGI_Compile_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Emulate::PSGI)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

unset AUTHOR_TESTING AUTOMATED_TESTING
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
