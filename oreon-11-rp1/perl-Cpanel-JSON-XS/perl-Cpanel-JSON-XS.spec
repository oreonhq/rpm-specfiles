%global source0_hash e1ac2fab1e3a6d2d998d3440c600067365bdc7dbf0c8f2b2059cbce4b4c83173
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Cpanel_JSON_XS_enables_extra_test
Name:		perl-Cpanel-JSON-XS
Summary:        JSON::XS for Cpanel, fast and correct serializing
Version:	4.42
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Cpanel-JSON-XS
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-%{version}.tar.gz
Patch0:		Cpanel-JSON-XS-4.20-signature.patch
%if !%{defined perl_bootstrap}
%if %{with perl_Cpanel_JSON_XS_enables_extra_test}
%endif
%endif
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
%{?perl_default_filter}
Provides:       perl(Cpanel::JSON::XS) = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::LZF)
BuildRequires:  perl(Config)
BuildRequires:  perl(Convert::Bencode)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(charnames)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%if !%{defined perl_bootstrap} && %{with perl_Cpanel_JSON_XS_enables_extra_test}
make test xtest AUTHOR_TESTING=1
%else
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
