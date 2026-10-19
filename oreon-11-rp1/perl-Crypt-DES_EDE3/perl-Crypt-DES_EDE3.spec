%global source0_hash 28592db7b9e34745aa91f3e19e5dbbb83aaf472a29e707b9791d0d02b3e227f5
Name:           perl-Crypt-DES_EDE3
Version:        0.03
Release:        1%{?dist}
Summary:        Triple-DES EDE encryption/decryption module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-DES_EDE3
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Crypt-DES_EDE3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-DES_EDE3-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
