%global source0_hash 074cc48931ffe9054919763b4e97699e6a2be554484de684a05e16d403e5fb9c
%bcond_with perl_Sereal_enables_optional_test
Name:           perl-Sereal
Version:        5.008
Release:        1%{?dist}
Summary:        Fast, compact, powerful binary (de-)serialization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sereal
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Sereal_enables_optional_test}
%endif
Provides:       perl(Sereal)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Decoder::Constants)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Sereal::Encoder::Constants)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Sereal is an efficient, compact-output, binary and feature-rich serialization
protocol. The Perl encoder is implemented as the Sereal::Encoder module, the
Perl decoder correspondingly as Sereal::Decoder. This Sereal module is a very
thin wrapper around both Sereal::Encoder and Sereal::Decoder. It depends on
both and loads both.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sereal-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
