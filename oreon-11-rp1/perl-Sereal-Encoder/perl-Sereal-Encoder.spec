%global source0_hash 5095000aa86cbee7c798664e7bfd6d74b31cbaf337e41e2b9d185bcec8810946
%bcond_with perl_Sereal_Encoder_enables_optional_test
Name:           perl-Sereal-Encoder
Version:        5.008
Release:        1%{?dist}
Summary:        Perl serialization into Sereal format
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LGPL-2.1-or-later
URL:            https://metacpan.org/release/Sereal-Encoder
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Encoder-%{version}.tar.gz
Patch0:         Sereal-Encoder-5.004-external-miniz.patch
%if %{with perl_Sereal_Encoder_enables_optional_test}
%endif
Provides:       perl(Sereal::Encoder)
Provides:       perl(Sereal::Encoder::Constants)
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
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
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
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
