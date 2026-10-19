%global source0_hash 68c4ac7eabfa957dcf894c2c23bcec096f87e8cf06dedfcbbf702e5531dbb137
Summary:        Pure-perl Lanman and NT MD4 hash functions
Name:		perl-Crypt-SmbHash
Version:	0.12
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://metacpan.org/release/Crypt-SmbHash
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-SmbHash-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(Digest::MD4)
Requires:	perl(Encode)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD4)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module generates Lanman and NT MD4 style password hashes, using perl-only
code for portability. The module aids in the administration of Samba style
systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-SmbHash-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
