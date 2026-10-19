%global source0_hash 8843fead5115355c27269a786734a8105ab9f66a4b587cab26af7a783e0c2032
%bcond dft 1
%bcond quad 1
%bcond static 0
%bcond tlfloat 1
Name:           sleef
Version:        3.9.0
%global tag %{version}
%global so_version 3
Release:        1%{?dist}
Summary:        Vectorized math library
License:        BSL-1.0
URL:            https://sleef.org
Source0:        %{name}-%{version}-filtered.tar.zst
Source1:        get_source.sh
ExcludeArch:    %{ix86}
%ifarch %{arm64}
%global _lto_cflags %{nil}
%endif
%if %{with dft}
%endif
%if %{with tlfloat}
%endif
%global gnuabi_arches %{ix86} %{x86_64} %{arm64}
%if %{with static}
%global inline_enabled 1
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(tlfloat)
# /oreon:deps
%description
SLEEF stands for SIMD Library for Evaluating Elementary Functions. It
implements vectorized versions of all C99 real floating point math functions.
It can utilize SIMD instructions that are available on modern processors. SLEEF
is designed to efficiently perform computation with SIMD instructions by
reducing the use of conditional branches and scatter/gather memory access.

The library contains implementations of all C99 real FP math functions in
double precision and single precision. Different accuracy of the results can be
chosen for a subset of the elementary functions; for this subset there are
versions with up to 1 ULP error (which is the maximum error, not the average)
and even faster versions with a few ULPs of error. For non-finite inputs and
outputs, the functions return correct results as specified in the C99 standard.

%package devel
Summary:        Development files for sleef
Requires:       sleef%{?_isa} = %{version}-%{release}
%description devel
The sleef-devel package contains libraries and header files for
developing applications that use sleef.

%if 0%{?inline_enabled}
%package static
Summary:        Inline headers and static library for sleef
Requires:       sleef-devel%{?_isa} = %{version}-%{release}
%description static
The sleef-static package contains libraries and header files for
developing applications that use sleef.
%endif

%package doc
Summary:        Documentation for sleef
BuildArch:      noarch
%description doc
The sleef-doc package contains detailed API documentation for developing
applications that use sleef.

%ifarch %{gnuabi_arches}
%package gnuabi
Summary:        GNUABI version of sleef
%global gnuabi_enabled 1
%description gnuabi
The GNUABI version of the library (libsleefgnuabi.so) is built for x86 and
aarch64 architectures. This library provides an API compatible with libmvec in
glibc, and the API conforms to the x86 vector ABI, AArch64 vector ABI and Power
Vector ABI.

%package gnuabi-devel
Summary:        Development files for GNUABI version of sleef
Requires:       sleef-gnuabi%{?_isa} = %{version}-%{release}
%description gnuabi-devel
The sleef-gnuabi-devel package contains libraries for developing applications
that use the GNUABI version of sleef. Note that this package does not contain
any header files.
%endif

%if %{with dft}
%package dft
Summary:        Discrete Fourier Transform (DFT) library
Requires:       sleef%{?_isa} = %{version}-%{release}
%description dft
SLEEF includes subroutines for discrete Fourier transform(DFT). These
subroutines are fully vectorized, heavily unrolled, and parallelized in such a
way that modern SIMD instructions and multiple cores can be utilized for
efficient computation. It has an API similar to that of FFTW for easy
migration. The subroutines can utilize long vectors up to 2048 bits.

%package dft-devel
Summary:        Development files for sleef-dft
Requires:       sleef-dft%{?_isa} = %{version}-%{release}
%description dft-devel
The sleef-dft-devel package contains libraries and header files for
developing applications that use sleef-dft.
%endif

%if %{with quad}
%package quad
Summary:        Vectorized quad-precision math library
%description quad
An experimental quad-precision library

%package quad-devel
Summary:        Development files for sleef-quad
Requires:       sleef-quad%{?_isa} = %{version}-%{release}
%description quad-devel
The sleef-quad-devel package contains libraries and header files for
developing applications that use sleef-quad.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sleef-%{tag} -p1
# Remove an unwanted hidden file from the docs
find docs/ -type f -name .nojekyll -print -delete

%conf
# -GNinja: This used to be required for parallel builds; it is still faster.
#
# -DENFORCE_TESTER3: The build should fail if we cannot build all tests.
# -DENFORCE_TESTER4: Likewise, except that tester4 requires tlfloat.
#
# -DBUILD_INLINE_HEADERS: Do not build the “inline” headers. This would provide
#   an arch-specific collection of sleefinline_*.h headers in _includedir, as
#   well as a static support library, libsleefinline.a, in _libdir. Both the
#   static library and the headers (which are basically a header-only library,
#   and would thus also be treated as a static library in the Fedora
#   guidelines) should be omitted unless something in Fedora absolutely
#   requires them.
#
# -DSLEEFDFT_ENABLE_STREAM: The author writes, “The recommended value for
#   SLEEFDFT_ENABLE_STREAM depends on the architecture, and it is only
#   recommended to be turned on on x86_64.”
#   https://github.com/shibatch/sleef/discussions/654#discussioncomment-12860550
%cmake \
    -GNinja \
    -DSLEEF_BUILD_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE} \
    -DSLEEF_ENFORCE_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE} \
%ifarch %{x86_64}
    -DSLEEFDFT_ENABLE_STREAM:BOOL=TRUE \
%else
    -DSLEEFDFT_ENABLE_STREAM:BOOL=FALSE \
%endif
    -DSLEEF_BUILD_GNUABI_LIBS:BOOL=%{?gnuabi_enabled:TRUE}%{?!gnuabi_enabled:FALSE} \
    -DSLEEF_BUILD_INLINE_HEADERS:BOOL=%{?inline_enabled:TRUE}%{?!inline_enabled:FALSE} \
    -DSLEEF_BUILD_QUAD:BOOL=%{?with_quad:TRUE}%{?!with_quad:FALSE} \
    -DSLEEF_BUILD_SHARED_LIBS:BOOL=TRUE \
    -DSLEEF_ENFORCE_TESTER3:BOOL=TRUE \
    -DSLEEF_ENFORCE_TESTER4:BOOL=%{?with_tlfloat:TRUE}%{?!with_tlfloat:FALSE} \
    -DSLEEF_ENABLE_TLFLOAT:BOOL=%{?with_tlfloat:TRUE}%{?!with_tlfloat:FALSE}

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

echo '==== Build host CPU features ===='
cat /proc/cpuinfo
skips='^($.'
%ifarch %{arm64}
if ! grep -E '[Ff](lags|eatures).*\bsve\b' /proc/cpuinfo >/dev/null
then
  skips="${skips}|gnuabi_compatibility_SVE(_masked)?|qiutsve"
fi
%endif
%ifarch %{power64}
if grep -E -i '\bPOWER8\b' /proc/cpuinfo >/dev/null
then
  skips="${skips}|.*vsx3(nofma)?"
fi
%endif
%ifarch %{x86_64}
%if %{undefined fc43} && %{undefined fc42} && %{undefined el10}
skips="${skips}|tester4ypurec_scalar"
%endif
%endif
skips="${skips})$"
%ctest --exclude-regex "${skips}" --extra-verbose
%files -f %{oreon_filedir}/main.list
%files -n sleef-devel -f %{oreon_filedir}/sleef-devel.list
%files -n sleef-static -f %{oreon_filedir}/sleef-static.list
%files -n sleef-doc -f %{oreon_filedir}/sleef-doc.list
%files -n sleef-dft -f %{oreon_filedir}/sleef-dft.list
%files -n sleef-dft-devel -f %{oreon_filedir}/sleef-dft-devel.list
%files -n sleef-quad -f %{oreon_filedir}/sleef-quad.list
%files -n sleef-quad-devel -f %{oreon_filedir}/sleef-quad-devel.list

%changelog

%autochangelog
