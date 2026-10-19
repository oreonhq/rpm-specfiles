%global source0_hash e568b193fa2f752416102543e06be81cf0dd785b881a6e99ecb77c9a07a2fd6c
Summary:        SASL DIGEST-MD5 authentication (RFC2831)
Name:		perl-Authen-DigestMD5
Version:	0.04
Release:        52%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Authen-DigestMD5
Source0:        https://cpan.metacpan.org/modules/by-module/Authen/Authen-DigestMD5-%{version}.tar.gz
Patch0:		Authen-DigestMD5-0.04-UTF8.patch
Patch1:		Authen-DigestMD5-0.04-shellbang.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module supports DIGEST-MD5 SASL authentication as defined in RFC-2831.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-DigestMD5-%{version}

# Fix wrong script interpreter, and set permissions to avoid extra deps
%patch -P 1
chmod -c 644 digest-md5-auth.pl

# Fix character encoding
%patch -P 0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
rm -f %{buildroot}%{perl_vendorlib}/Authen/digest-md5-auth.pl
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
