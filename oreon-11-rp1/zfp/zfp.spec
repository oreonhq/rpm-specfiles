%global source0_hash 4984db6a55bc919831966dd17ba5e47ca7ac58668f4fd278ebd98cd2200da66f
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build
Name:           zfp
Version:        1.0.1
Release:        8%{?dist}
Summary:        Library for compressed numerical arrays with high throughput R/W random access
License:        LicenseRef-Callaway-BSD
URL:            https://computation.llnl.gov/projects/floating-point-compression
Source0:        https://github.com/LLNL/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/LLNL/%{name}/pull/237.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-zfp = %{version}-%{release}
# /oreon:deps
%description
This is zfp, an open source C/C++ library for compressed numerical arrays
that support high throughput read and write random access. zfp was written by
Peter Lindstrom at Lawrence Livermore National Laboratory, and is loosely
based on the algorithm described in the following paper:

Peter Lindstrom
"Fixed-Rate Compressed Floating-Point Arrays"
IEEE Transactions on Visualization and Computer Graphics,
  20(12):2674-2683, December 2014
doi:10.1109/TVCG.2014.2346458

zfp was originally designed for floating-point data only, but has been
extended to also support integer data, and could for instance be used to
compress images and quantized volumetric data. To achieve high compression
ratios, zfp uses lossy but optionally error-bounded compression. Although
bit-for-bit lossless compression of floating-point data is not always
possible, zfp is usually accurate to within machine epsilon in near-lossless
mode.

zfp works best for 2D and 3D arrays that exhibit spatial coherence, such as
smooth fields from physics simulations, images, regularly sampled terrain
surfaces, etc. Although zfp also provides a 1D array class that can be used
for 1D signals such as audio, or even unstructured floating-point streams,
the compression scheme has not been well optimized for this use case, and
rate and quality may not be competitive with floating-point compressors
designed specifically for 1D streams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python3-zfpy
Summary:        zfp compression in Python
BuildRequires:  python3-devel
%description -n python3-zfpy
The python3-zfpy package contains a Python library for using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake3 -DCMAKE_SKIP_INSTALL_RPATH=YES -DHAVE_LIBM_MATH=YES
%cmake3_build
export LDFLAGS="$LDFLAGS -L$PWD/%{_vpath_builddir}/%{_lib}/"
%pyproject_wheel
%install
%cmake3_install
%pyproject_install
%ldconfig_scriptlets
%oreon_autofiles python3-zfpy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n zfp-devel -f %{oreon_filedir}/zfp-devel.list
%files -n python3-zfpy -f %{oreon_filedir}/python3-zfpy.list

%changelog

%autochangelog
