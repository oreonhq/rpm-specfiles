%global source0_hash 09203c102311149f5df5cc367409f96c725742666d19c24db5ba994d5a81a6f5
%if 0%{?__isa_bits} == 64
%define target linux-64
%else
%define target linux
%endif
%define variants thr thr-ogl
%define beta %nil
Summary:        Parallel / Multiprocessor Ray Tracing System
Name: tachyon
Version: 0.99.5
Release:        5%{?dist}
URL: http://jedi.ks.uiuc.edu/~johns/raytracer/
Source0:        http://jedi.ks.uiuc.edu/~johns/raytracer/files/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.1
Patch0: %{name}-rpm.patch
Patch1: %{name}-shared.patch
License: BSD-3-Clause AND MIT AND ( MIT OR Unlicense ) AND LPPL-1.3a+ AND SGI-OpenGL AND LGPL-2.0-or-later
# oreon:deps
BuildRequires:  gcc
BuildRequires:  latex2html
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
# /oreon:deps
%description
A portable, high performance parallel ray tracing system with
multithreaded implementation.

%package libs
Summary: Parallel / Multiprocessor Ray Tracing System library
%description libs
A portable, high performance parallel ray tracing system with
multithreaded implementation.  Tachyon is built as a C callable
library, which can be used with the included demo programs or within
your own application.

This package contains the shared library.

%package gl
Summary: Parallel / Multiprocessor Ray Tracing System with OpenGL display
Provides: %{name} = %{version}-%{release}
%description gl
A portable, high performance parallel ray tracing system with
multithreaded implementation.

This package contains OpenGL-enabled build.

%package devel
Summary: Development files for tachyon
Requires: %{name}-libs = %{version}-%{release}
%description devel
This package contains development headers and libraries for developing
with tachyon.

%package docs
Summary: Documentation and example scenes for tachyon
Requires: %{name} = %{version}-%{release}
%description docs
This package contains documentation and example scenes for rendering
with tachyon.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}
find . -name CVS | xargs rm -r
# executable sources
chmod 644 src/hash.{c,h}
chmod 644 src/pngfile.h
chmod 644 demosrc/spaceball.c
chmod 644 demosrc/trackball.{c,h}
# delete private symlinks
rm -v scenes/{imaps,tpoly,vol}
# work around unsupported -m32 gcc option
%ifarch aarch64 riscv64
sed -i -e 's/-m32 //g' unix/Make-arch
sed -i -e 's/-m64 //g' unix/Make-arch
%endif

%build

pushd unix
for variant in %{variants} ; do
  make %{?_smp_mflags} OPTFLAGS="$RPM_OPT_FLAGS" %{target}-$variant
done
popd
pushd docs
make html pdf ps
popd
%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},{%{_datadir},%{_includedir}}/tachyon,%{_mandir}/man1}
for variant in %{variants} ; do
  install -pm755 compile/%{target}-$variant/tachyon $RPM_BUILD_ROOT%{_bindir}/tachyon-$variant
done
rename -- -thr "" $RPM_BUILD_ROOT%{_bindir}/*
mkdir docs/html
cp -pr docs/tachyon/*.{css,html,png} docs/html
cp -pr scenes $RPM_BUILD_ROOT%{_datadir}/tachyon/
install -pm644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/
echo ".so tachyon.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tachyon-ogl.1
cp -a compile/%{target}-thr/libtachyon*.so $RPM_BUILD_ROOT%{_libdir}/
install -pm644 src/{hash,tachyon{,_dep},util}.h $RPM_BUILD_ROOT%{_includedir}/tachyon/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tachyon-libs -f %{oreon_filedir}/tachyon-libs.list
%files -n tachyon-gl -f %{oreon_filedir}/tachyon-gl.list
%files -n tachyon-devel -f %{oreon_filedir}/tachyon-devel.list
%files -n tachyon-docs -f %{oreon_filedir}/tachyon-docs.list

%changelog

%autochangelog
