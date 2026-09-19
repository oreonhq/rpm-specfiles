%global source0_hash b796cd0ab197083301d8f44f5e21ee3e014b7a0791c9e10f3a51204029fd3a3b

Name:		perl-Text-Hunspell
Version:	2.16
Release:	13%{?dist}
Summary:	Perl interface to the Hunspell library
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Text-Hunspell
Source0:	https://cpan.metacpan.org/modules/by-module/Text/Text-Hunspell-%{version}.tar.gz
Patch1:		Text-Hunspell-2.15-no-Alien.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc-c++
BuildRequires:	hunspell-devel >= 1.2.8
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(vars)
# Test Suite
%if 0%{?fedora} > 23 || 0%{?rhel} > 7
BuildRequires:	glibc-langpack-en
%endif
BuildRequires:	hunspell-en
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(warnings)
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides a Perl interface to the Hunspell library. This module
is to meet the need of looking up many words, one at a time, in a single
session, such as spell-checking a document in memory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Hunspell-%{version}

# We don't have (nor need) Alien::Hunspell, so revert to using ExtUtils::PkgConfig
%patch -P 1

# Fix up shellbang in example
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' examples/basic.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
LANG=en_US make test TEST_POD=1 TEST_VERBOSE=1

%files
%license LICENSE
%doc Changes README examples/
%{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/Text/
%{_mandir}/man3/Text::Hunspell.3*

%changelog
%autochangelog
