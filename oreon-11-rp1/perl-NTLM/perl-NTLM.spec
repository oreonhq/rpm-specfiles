%global source0_hash c823e30cda76bc15636e584302c960e2b5eeef9517c2448f7454498893151f85
%bcond_without perl_NTLM_enables_optional_test
Name:           perl-NTLM
Version:        1.09
Release:        42%{?dist}
Summary:        NTLM Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/NTLM
Source0:        https://cpan.metacpan.org/authors/id/N/NB/NBEBOUT/NTLM-%{version}.tar.gz
Patch0:         NTLM-1.09-Remove-shebangs-from-the-modules.patch
BuildArch:      noarch
%if %{with perl_NTLM_enables_optional_test}
%endif
Provides:       perl(Authen::NTLM)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides methods to use NTLM authentication.  It can be used
as an authenticate method with the Mail::IMAPClient module to perform
the challenge/response mechanism for NTLM connections or it can be used
on its own for NTLM authentication with other protocols (eg. HTTP).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n NTLM-%{version}
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.09-42
- Prepare for Oreon 11 (RP1)
