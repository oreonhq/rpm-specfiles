%global source0_hash dd5b6c353f08fba100dae09904284f7f73f8328d31f6a67b2c136fad728d158b
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-CGI-Emulate-PSGI
Version:        0.23
Release:        1%{?dist}
Summary:        PSGI adapter for CGI applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Emulate-PSGI
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/CGI-Emulate-PSGI-%{version}.tar.gz
BuildArch:      noarch
%if 0%{!?perl_bootstrap:1}
%endif
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module allows an application designed for the CGI environment to run
in a PSGI environment, and thus on any of the back-ends that PSGI supports.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Emulate-PSGI-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
