%global source0_hash dd5b6c353f08fba100dae09904284f7f73f8328d31f6a67b2c136fad728d158b

Name:           perl-CGI-Emulate-PSGI
Version:        0.23
Release:        32%{?dist}
Summary:        PSGI adapter for CGI applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Emulate-PSGI
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/CGI-Emulate-PSGI-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Requires)
# perl-Plack requires perl-CGI-Emulate-PSGI itself
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Plack::Test)
%endif

%{?perl_default_filter}

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

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI*

%changelog
%autochangelog
