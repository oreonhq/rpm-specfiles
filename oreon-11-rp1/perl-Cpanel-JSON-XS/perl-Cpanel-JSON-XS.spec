%global source0_hash e1ac2fab1e3a6d2d998d3440c600067365bdc7dbf0c8f2b2059cbce4b4c83173

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Cpanel_JSON_XS_enables_extra_test
%else
%bcond_with perl_Cpanel_JSON_XS_enables_extra_test
%endif

Name:		perl-Cpanel-JSON-XS
Summary:	JSON::XS for Cpanel, fast and correct serializing
Version:	4.42
Release:	1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Cpanel-JSON-XS
Source0:	https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-%{version}.tar.gz
Patch0:		Cpanel-JSON-XS-4.20-signature.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Script Runtime
BuildRequires:	perl(CBOR::XS)
BuildRequires:	perl(Compress::LZF)
BuildRequires:	perl(Convert::Bencode)
BuildRequires:	perl(CPAN::Meta::YAML)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(YAML)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(YAML::XS)
# Test Suite
BuildRequires:	perl(B)
BuildRequires:	perl(charnames)
BuildRequires:	perl(constant)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Devel::Peek)
BuildRequires:	perl(Encode) >= 1.9081
BuildRequires:	perl(lib)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(threads)
BuildRequires:	perl(threads::shared) >= 1.21
BuildRequires:	perl(Tie::Array)
BuildRequires:	perl(Tie::Hash)
BuildRequires:	perl(utf8)
# Optional Tests
# Cycle: perl-Cpanel-JSON-XS → perl-Test-LeakTrace → perl-Module-Install
# → perl-YAML-Tiny → perl-JSON-MaybeXS → perl-Cpanel-JSON-XS
# Cycle: perl-Cpanel-JSON-XS → perl-Perl-MinimumVersion → perl-PPI
# → perl-List-MoreUtils → perl-Test-LeakTrace → perl-Module-Install
# → perl-YAML-Tiny → perl-JSON-MaybeXS → perl-Cpanel-JSON-XS
# Cycle: perl-Cpanel-JSON-XS → perl-Test-MinimumVerion → perl-YAML-Tiny
# → perl-JSON-MaybeXS → perl-Cpanel-JSON-XS
# Cycle: perl-Cpanel-JSON-XS → perl-Test-Kwalitee → perl-Module-CPANTS-Analyse
# → perl-JSON-MaybeXS → perl-Cpanel-JSON-XS
%if !%{defined perl_bootstrap}
BuildRequires:	perl(common::sense) >= 3.5
BuildRequires:	perl(Hash::Util)
BuildRequires:	perl(JSON) >= 2.09
BuildRequires:	perl(JSON::PP) >= 2.09
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Math::BigFloat) >= 1.16
BuildRequires:	perl(Math::BigInt)
%if 0%{?fedora:1}
BuildRequires:	perl(Mojo::JSON) >= 6.11
%endif
BuildRequires:	perl(Test::LeakTrace)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(Time::Piece)
# Maintainer Tests (Test::Spelling intentionally omitted as associated test would fail due to various technical terms)
%if %{with perl_Cpanel_JSON_XS_enables_extra_test}
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Perl::MinimumVersion) >= 1.20
BuildRequires:	perl(Pod::Spell::CommonMistakes)
BuildRequires:	perl(Test::CheckChanges)
BuildRequires:	perl(Test::CPAN::Changes)
BuildRequires:	perl(Test::CPAN::Meta) >= 0.12
BuildRequires:	perl(Test::Kwalitee)
BuildRequires:	perl(Test::MinimumVersion) >= 0.008
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Text::CSV_XS)
%endif
%endif
# Dependencies
Requires:	perl(Carp)
Requires:	perl(overload)
Requires:	perl(Scalar::Util)
Recommends:	perl(Math::BigFloat) >= 1.16
Recommends:	perl(Math::BigInt)
Suggests:	perl(Bencode)
Suggests:	perl(CBOR::XS)
Suggests:	perl(Compress::LZF)
Suggests:	perl(CPAN::Meta::YAML)
Suggests:	perl(Data::Dump)
Suggests:	perl(Data::Dumper)
Suggests:	perl(Sereal::Decoder)
Suggests:	perl(Sereal::Encoder)
Suggests:	perl(YAML)
Suggests:	perl(YAML::Syck)
Suggests:	perl(YAML::XS)

# Avoid unwanted provides and dependencies
%{?perl_default_filter}

Provides:       perl(Cpanel::JSON::XS) = %{version}
%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Cpanel-JSON-XS-%{version}

# Fix shellbangs
perl -pi -e 's|^#!/opt/bin/perl|#!/usr/bin/perl|' eg/*

# Skip the signature check as we've tweaked some files
%patch -P 0

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
%if !%{defined perl_bootstrap} && %{with perl_Cpanel_JSON_XS_enables_extra_test}
make test xtest AUTHOR_TESTING=1
%else
make test
%endif

%files
%license COPYING
%doc Changes README eg/
%{_bindir}/cpanel_json_xs
%{perl_vendorarch}/auto/Cpanel/
%{perl_vendorarch}/Cpanel/
%{_mandir}/man1/cpanel_json_xs.1*
%{_mandir}/man3/Cpanel::JSON::XS.3*
%{_mandir}/man3/Cpanel::JSON::XS::Boolean.3*
%{_mandir}/man3/Cpanel::JSON::XS::Type.3*

%changelog
%autochangelog
