%global source0_hash 33bd78c11924a0fc1ff3eedde94078cbbf6b6ca9ede046d2b2f561e9e9a72019

Summary:	Perl interface to IDEA block cipher
Name:		perl-Crypt-IDEA
Version:	1.10
Release:	37%{?dist}
License:	BSD-Systemics
URL:		https://metacpan.org/release/Crypt-IDEA
Source0:	https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-IDEA-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies

# Don't provide private perl libs
%{?perl_default_filter}

Provides:       perl(Crypt::IDEA)
Provides:       perl(Crypt::IDEA)
%description
This perl extension is an implementation of the IDEA block cipher algorithm.
The module implements the Crypt::BlockCipher interface.

This implementation is copyright Systemics Ltd (http://www.systemics.com/).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-IDEA-%{version}

# Remove unnecessary shellbang that points to the wrong perl interpreter anyway
sed -i -e '\|^#! */usr/local/bin/perl |d' IDEA.pm

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license COPYRIGHT
%else
%doc COPYRIGHT
%endif
%doc changes
%{perl_vendorarch}/Crypt/
%{perl_vendorarch}/auto/Crypt/
%{_mandir}/man3/Crypt::IDEA.3*

%changelog
%autochangelog
