%global source0_hash bc002d405ed18f7a15711918ab766af1e7278576f0661704329205bb9b9a1b3e
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_Sereal_Decoder_enables_optional_test
Name:           perl-Sereal-Decoder
Version:        5.008
Release:        1%{?dist}
Summary:        Perl deserialization for Sereal format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sereal-Decoder
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Decoder-%{version}.tar.gz
Patch0:         Sereal-Decoder-5.004-external-miniz.patch
%if %{with perl_Sereal_Decoder_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Provides:       perl(Sereal::Decoder)
Provides:       perl(Sereal::Decoder::Constants)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  csnappy-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  miniz-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This library implements a deserializer for an efficient, compact-output,
and feature-rich binary protocol called Sereal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sereal-Decoder-%{version}

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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
