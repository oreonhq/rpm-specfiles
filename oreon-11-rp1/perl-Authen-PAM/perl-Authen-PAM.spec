%global source0_hash 0e949bd9a2a9df0f829971030fe9169cbaf6cec78b92faf22f547ff6c6155c9b
Name:           perl-Authen-PAM
Version:        0.16
Release:        1%{?dist}
Summary:        Authen::PAM Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-PAM
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIKIP/Authen-PAM-%{version}.tar.gz
Patch0:         Authen-PAM-0.16-Fix-building-on-Perl-without-dot-in-INC.patch
%{?_with_check:BuildRequires:  perl(POSIX)}
%{?_with_check:BuildRequires:  perl(strict)}
%{?_with_check:BuildRequires:  perl(vars)}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a Perl interface to the PAM library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-PAM-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{?_with_check:make test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
