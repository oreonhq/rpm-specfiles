%global source0_hash 074cc48931ffe9054919763b4e97699e6a2be554484de684a05e16d403e5fb9c

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Sereal_enables_optional_test
%else
%bcond_with perl_Sereal_enables_optional_test
%endif

Name:           perl-Sereal
Version:        5.008
Release:        1%{?dist}
Summary:        Fast, compact, powerful binary (de-)serialization
# Makefile.PL defines LICENSE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sereal
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# blib not used
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# Devel::CheckLib not used
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Find not used
# File::Path not used
# File::Spec not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Sereal::Decoder) >= %{version}
BuildRequires:  perl(Sereal::Encoder) >= %{version}
# Tests:
# Benchmark not used
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
# Hash::Util is needed on perl >= 5.25. It's in an eval to proceed to
# num_buckets() definition with older perls.
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder::Constants)
BuildRequires:  perl(Sereal::Encoder::Constants)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
# Time::HiRes not used
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
%if %{with perl_Sereal_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Deep::NoTest)
%endif

Provides:       perl(Sereal)
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

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Sereal.pm
%{_mandir}/man3/Sereal.3*

%changelog
%autochangelog
