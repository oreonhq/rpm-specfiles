%global source0_hash 9a53c1b7c7f160e898e6cb5be9948d64141d2819ade2d7a873d0e87d1e83f666
Name:           perl-Mail-AuthenticationResults
Version:        2.20260216
Release:        1%{?dist}
Summary:        Object Oriented Authentication-Results Headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-AuthenticationResults/
Source0:        https://cpan.metacpan.org/modules/by-module/Mail/Mail-AuthenticationResults-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Mail::AuthenticationResults::Header::AuthServID)
Provides:       perl(Mail::AuthenticationResults::Parser)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Object Oriented Authentication-Results email headers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mail-AuthenticationResults-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20260216-1
- Prepare for Oreon 11 (RP1)
