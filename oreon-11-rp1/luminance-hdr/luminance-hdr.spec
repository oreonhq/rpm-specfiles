%global source0_hash fa5a870ee00392a972755dd04a35e928ec9c50c474f4c72d0477dea337e0b81a
Name:           luminance-hdr
Version:        2.6.1.1
Release:        1%{?dist}
Summary:        GUI that provides a complete workflow for HDR imaging
License:        %{shrink:
                GPL-2.0-only AND
                GPL-3.0-or-later AND
                LGPL-2.1-or-later AND
                BSD-3-Clause AND
                MIT AND
                BSL-1.0 AND
                CC0-1.0
                }
URL:            http://qtpfsgui.sourceforge.net/
%global forgeurl https://github.com/LuminanceHDR/LuminanceHDR/
Source0:        %{forgeurl}/archive/v.%{version}/%{name}-%{version}.tar.gz
Source1:        luminance-hdr.1
Source2:        luminance-hdr-cli.1
ExcludeArch:    %{ix86}
Patch:          luminance-hdr-2.6.1.1-sleef-boost-license.patch
Patch:          luminance-hdr-2.6.1.1-external-librtprocess.patch
Patch:          0001-Update-help-tree-files-from-Scribus-SVN-24770.patch
Patch:          0002-Fix-an-include-path-in-schelptreemodel.h.patch
Patch:          0003-Comment-out-Q_OBJECT-in-ScHelpTreeModel-and-TreeMode.patch
Patch:          %{forgeurl}/pull/253.patch
Patch:          %{forgeurl}/pull/277.patch
Patch:          0001-Fix-build-with-exiv2-0.28.0-raise-minimum-to-0.27.0.patch
Patch:          https://github.com/gentoo/gentoo/raw/f183705a78237d697d57279c392fe4afb27b9ae3/media-gfx/luminance-hdr/files/luminance-hdr-2.6.1.1-openexr3.patch
Patch:          %{forgeurl}/pull/288.patch
Patch:          %{forgeurl}/pull/284.patch
%ifarch %{qt5_qtwebengine_arches}
%else
%endif
Obsoletes:      qtpfsgui < 2.2.0
Provides:       qtpfsgui = %{version}-%{release}
Provides:       bundled(pfstools)
Provides:       bundled(pfstmo) = 2.0.5
Provides:       bundled(sleef)
Requires:       luminance-hdr-data = %{version}-%{release}
%global app_id net.sourceforge.qtpfsgui.LuminanceHDR
# oreon:deps
BuildRequires:  (pkgconfig(eigen3) with eigen3-static)
BuildRequires:  LibRaw-devel
BuildRequires:  appstream
BuildRequires:  boost-devel
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  exiv2-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  gtest-devel
BuildRequires:  lcms2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librtprocess-devel
BuildRequires:  libtiff-devel
BuildRequires:  openexr-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtwebkit-devel
# /oreon:deps
%description
Luminance HDR is a graphical user interface (based on the Qt5 toolkit) that
provides a complete workflow for HDR imaging.

Supported HDR formats:

  • OpenEXR (extension: exr)
  • Radiance RGBE (extension: hdr)
  • Tiff formats: 16bit, 32bit (float) and LogLuv (extension: tiff)
  • Raw image formats (extension: various)
  • PFS native format (extension: pfs)

Supported LDR formats:

  • JPEG, PNG, PPM, PBM, TIFF, FITS

Supported features:

  • Create an HDR file from a set of images (JPEG, TIFF 8bit and 16bit, RAW) of
    the same scene taken at different exposure settings
  • Save and load HDR files
  • Rotate and resize HDR files
  • Tonemap HDR images
  • Projective Transformations
  • Copy EXIF data between sets of images
  • Supports internationalization

Raw image formats are supported - and treated as HDR - thanks to LibRAW.

The code is in part based on the existing open source packages:

  • “pfstools”, “pfstmo” and “pfscalibration” by Grzegorz Krawczyk and Rafal
    Mantiuk
  • “qpfstmo”, by Nicholas Phillips.

Without their contribution all of this would have not been possible.

%package data
Summary:        Architecture-independent data files for luminance-hdr
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       pfstools
%description data
Architecture-independent data files for luminance-hdr, such as HTML help and
translations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n LuminanceHDR-v.%{version} -p1

# Just in case the bundled librtprocess shows up in the tarball:
rm -rf librtprocess

# https://github.com/LuminanceHDR/LuminanceHDR/pull/236
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(TestPoissonSolver\b.*pfstmo)'\
'[[:blank:]]*$/\1 common/' \
    test/CMakeLists.txt
# https://github.com/LuminanceHDR/LuminanceHDR/pull/237
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(pfstmo[[:blank:]]+)(Qt5::)/\1pfs \2/' \
     src/TonemappingOperators/CMakeLists.txt
# https://github.com/LuminanceHDR/LuminanceHDR/issues/240
# https://github.com/LuminanceHDR/LuminanceHDR/pull/238
sed -r -i \
    -e 's/(TARGET_LINK_LIBRARIES\(pfs[[:blank:]]+)(Qt5::)/\1rtprocess \2/' \
     src/Libpfs/CMakeLists.txt

# Remove bundled copy of hdrhtml from pfstools package; let the build system
# install an empty directory, then replace it with a symbolic link to the
# pfstools copy.
rm -rf hdrhtml/*

# build error against boost 1.88 due to outdated C++ std version
# https://github.com/LuminanceHDR/LuminanceHDR/issues/291
sed -r -i 's/\b(CMAKE_CXX_STANDARD[[:blank:]]+)11\b/\114/' \
    build_files/Modules/CompilerSettings.cmake

%conf
# Since Fedora 44 / eigen3 5.0, we actually need to set the proper include path
# for eigen3. There are still no linker flags for eigen3, but we check anyway.
export CXXFLAGS="${CXXFLAGS} $(pkgconf --cflags eigen3)"
export LDFLAGS="${LDFLAGS} $(pkgconf --libs eigen3)"

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_UNIT_TEST:BOOL=ON

%build

%cmake_build
%install
%cmake_install
rm -rvf '%{buildroot}%{_datadir}/luminance-hdr/doc'
install -t '%{buildroot}/%{_datadir}/mime/packages' -D -p -m 0644 \
    luminance-hdr.xml
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications \
    %{app_id}.desktop
install -d '%{buildroot}%{_metainfodir}'
mv -v '%{buildroot}%{_datadir}/appdata/%{app_id}.appdata.xml' \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE1}' '%{SOURCE2}'
%find_lang lang --with-qt
rm -rvf '%{buildroot}%{_datadir}/luminance-hdr/hdrhtml'
ln -s ../pfstools '%{buildroot}%{_datadir}/luminance-hdr/hdrhtml'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

x='Mantiuk06Pyramid'
%ifarch %{ix86}
x="${x}|PoissonSolver"
%endif
%ctest --exclude-regex "^Test(${x})\$"
%files -f %{oreon_filedir}/main.list
%files -n luminance-hdr-data -f %{oreon_filedir}/luminance-hdr-data.list

%changelog

%autochangelog
