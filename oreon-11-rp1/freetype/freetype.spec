# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 36bc4f1cc413335368ee656c42afca65c5a3987e8768cc28cf11ba775e785a5f
%global source1_hash 66a988d8bbb58f83efafe555678ac172f70f0b060cf61424fe5460157470fd21
%global source2_hash 1ac96a066c39108f2b0cc8aa805106ed2c38146c8913dc2396dc242e91e35686

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond harfbuzz 0
%bcond ftinspect 0

%global pc_version 26.6.20

Name: freetype
Version: 2.14.3
Release: 1%{?dist}
Summary: A free and portable font rendering engine
License: (FTL OR GPL-2.0-or-later) AND BSD-3-Clause AND MIT AND MIT-Modern-Variant AND LicenseRef-Fedora-Public-Domain AND Zlib
URL: https://www.freetype.org
Source0: https://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.xz
Source1: https://download.savannah.gnu.org/releases/freetype/freetype-doc-%{version}.tar.xz
Source2: https://download.savannah.gnu.org/releases/freetype/ft2demos-%{version}.tar.xz
Source3: ftconfig.h

Patch0: freetype-2.3.0-enable-spr.patch
Patch1: freetype-2.2.1-enable-valid.patch
Patch3: freetype-2.6.5-libtool.patch
Patch4: freetype-2.8-multilib.patch
Patch5: freetype-2.10.0-internal-outline.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: libX11-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: brotli-devel
%if %{with ftinspect}
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-qtbase-devel
%endif
%if %{with harfbuzz}
BuildRequires: harfbuzz-devel
%endif

Provides: %{name}-bytecode
Provides: %{name}-subpixel
Obsoletes: freetype-freeworld < 2.9.1-2

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.

%package demos
Summary: A collection of FreeType demos
Requires: %{name}%{?_isa} = %{version}-%{release}

%description demos
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. The demos package includes a set of useful
small utilities showing various capabilities of the FreeType library.

%if %{with ftinspect}
%package qt-demos
Summary: Qt-based FreeType font inspection demo
Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt-demos
The freetype-qt-demos package provides ftinspect, a Qt-based application
for inspecting fonts and FreeType rendering behavior.
%endif

%package devel
Summary: FreeType development libraries and header files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconf%{?_isa}
Provides: pkgconfig(freetype2) = %{pc_version}

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -

%setup -q -b 1 -a 2
%autopatch -p1

%build
%configure --disable-static \
           --with-zlib=yes \
           --with-bzip2=yes \
           --with-png=yes \
           --enable-freetype-config \
%if %{with harfbuzz}
           --with-harfbuzz=yes \
%else
           --with-harfbuzz=no \
%endif
           --with-brotli=yes
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
%make_build

pushd ft2demos-%{version}
make TOP_DIR=".."
popd

%if %{with ftinspect}
pushd ft2demos-%{version}/src/ftinspect
ft_root="$(realpath ../../..)"
%cmake \
  -DUSE_QT_VERSION=6 \
  -DFREETYPE_INCLUDE_DIR_ft2build="${ft_root}/include" \
  -DFREETYPE_INCLUDE_DIR_freetype2="${ft_root}/include" \
  -DFREETYPE_LIBRARY="${ft_root}/objs/.libs/libfreetype.so" \
  -DCMAKE_SKIP_RPATH=ON
%cmake_build
popd
%endif

%install
%make_install gnulocaledir=%{buildroot}%{_datadir}/locale

for ftdemo in ftbench ftdump ftlint ftvalid ttdebug ftdiff ftgamma ftgrid ftmulti ftsdf ftstring ftview; do
    builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo %{buildroot}%{_bindir}
    builds/unix/libtool --mode=install install -m 644 ft2demos-%{version}/man/${ftdemo}.1 %{buildroot}%{_mandir}/man1
done

%if %{with ftinspect}
install -D -p -m 0755 \
  ft2demos-%{version}/src/ftinspect/%{_vpath_builddir}/ftinspect \
  %{buildroot}%{_bindir}/ftinspect
%endif

%define wordsize %{__isa_bits}

mv %{buildroot}%{_includedir}/freetype2/freetype/config/ftconfig.h \
   %{buildroot}%{_includedir}/freetype2/freetype/config/ftconfig-%{wordsize}.h
install -p -m 644 %{SOURCE3} %{buildroot}%{_includedir}/freetype2/freetype/config/ftconfig.h

rm -f %{buildroot}%{_libdir}/*.{a,la}

%ldconfig_post
%ldconfig_postun

%files
%license LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT
%doc README ChangeLog
%{_libdir}/libfreetype.so.*

%files demos
%{_bindir}/ftbench
%{_bindir}/ftdump
%{_bindir}/ftlint
%{_bindir}/ftvalid
%{_bindir}/ttdebug
%{_bindir}/ftdiff
%{_bindir}/ftgamma
%{_bindir}/ftgrid
%{_bindir}/ftmulti
%{_bindir}/ftsdf
%{_bindir}/ftstring
%{_bindir}/ftview
%{_mandir}/man1/ftbench.1*
%{_mandir}/man1/ftdump.1*
%{_mandir}/man1/ftlint.1*
%{_mandir}/man1/ftvalid.1*
%{_mandir}/man1/ttdebug.1*
%{_mandir}/man1/ftdiff.1*
%{_mandir}/man1/ftgamma.1*
%{_mandir}/man1/ftgrid.1*
%{_mandir}/man1/ftmulti.1*
%{_mandir}/man1/ftsdf.1*
%{_mandir}/man1/ftstring.1*
%{_mandir}/man1/ftview.1*

%if %{with ftinspect}
%files qt-demos
%license LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT
%{_bindir}/ftinspect
%endif

%files devel
%doc docs/CHANGES docs/formats.txt docs/ft2faq.html
%doc docs/design
%doc docs/glyphs
%doc docs/reference
%doc docs/tutorial
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc
%{_mandir}/man1/freetype-config.1*

%changelog
%autochangelog
