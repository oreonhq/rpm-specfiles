%global source0_hash 7d9d6b57bef2c3a33142c4cf0ca07d8801575e53b7f054b83df9f616bd2a7773

Name:           perl-CGI-FastTemplate
Version:        1.09
Release:        52%{?dist}
Summary:        Perl extension for managing templates and performing variable interpolation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-FastTemplate
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMOORE/CGI-FastTemplate-1.09.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)

%description
CGI::FastTemplate manages templates and parses templates replacing
variable names with values.  It was designed for mid to large scale web
applications (CGI, mod_perl) where there are great benefits to separating
the logic of an application from the specific implementation details.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-FastTemplate-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
