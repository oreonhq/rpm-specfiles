%global source0_hash 5095000aa86cbee7c798664e7bfd6d74b31cbaf337e41e2b9d185bcec8810946

# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_Sereal_Encoder_enables_optional_test
%else
%bcond_with perl_Sereal_Encoder_enables_optional_test
%endif

Name:           perl-Sereal-Encoder
Version:        5.008
Release:        1%{?dist}
Summary:        Perl serialization into Sereal format
# lib/Sereal/Encoder.pm:    GPL+ or Artistic
# qsort.h:                  LGPLv2+ (borrowed from glibc)
## Unbundled
# miniz.c:                  MIT and Unlicense
# snappy:                   BSD
# zstd/decompress/zstd_decompress.c:   GPLv2 or BSD
# See <https://github.com/Sereal/Sereal/issues/72>
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LGPL-2.1-or-later
URL:            https://metacpan.org/release/Sereal-Encoder
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Encoder-%{version}.tar.gz
Patch0:         Sereal-Encoder-5.004-external-miniz.patch
# Build:
BuildRequires:  coreutils
BuildRequires:  csnappy-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  miniz-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::CheckLib) >= 1.16
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.0
# File::Find not used
# File::Path not used in inc/Sereal/BuildTools.pm
# File::Spec not used in inc/Sereal/BuildTools.pm
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
# Benchmark not used
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
# Hash::Util is needed on perl >= 5.25. It's in an eval to proceed to
# num_buckets() definition with older perls.
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder) >= %{version}
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
# Time::HiRes not used
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
%if %{with perl_Sereal_Encoder_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Deep::NoTest)
%endif

Provides:       perl(Sereal::Encoder)
Provides:       perl(Sereal::Encoder::Constants)
%description
This library implements an efficient, compact-output, and feature-rich
serializer using a binary protocol called Sereal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sereal-Encoder-%{version}

# Fix detection of miniz 3.1.0
%patch -P0

# Remove bundled Perl modules
rm -r ./inc/Devel
perl -i -ne 'print $_ unless m{^inc/Devel/}' MANIFEST
# Remove bundled csnappy
rm -r ./snappy
perl -i -ne 'print $_ unless m{^snappy/}' MANIFEST
# Remove bundled miniz
rm miniz.*
perl -i -ne 'print $_ unless m{^miniz\.}' MANIFEST
# Remove bundled zstd
rm -r zstd
perl -i -ne 'print $_ unless m{^zstd/}' MANIFEST

%build
unset DEBUG SEREAL_USE_BUNDLED_LIBS SEREAL_USE_BUNDLED_CSNAPPY \
    SEREAL_USE_BUNDLED_MINIZ SEREAL_USE_BUNDLED_ZSTD
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}" INC="$(pkg-config --cflags miniz)"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/Sereal/
%{perl_vendorarch}/Sereal/
%{_mandir}/man3/Sereal::Encoder.3*

%changelog
%autochangelog
