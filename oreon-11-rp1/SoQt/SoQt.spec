%global source0_hash e15789928725f7c5963c06b6a2ed52a239ecf56887e0448fec909e3b8935f73e

%global cpack_hash 118ac5a21bcf57f0f90e2b0e681c9dcbf07074c2
%global cpack_short %(c=%{cpack_hash}; echo ${c:0:10})
%global cpack_date 20200419
%global soanydata_hash 3ff6e9203fbb0cc08a2bdf209212b7ef4d78a1f2
%global soanydata_short %(c=%{soanydata_hash}; echo ${c:0:10})
%global soanydata_date 20200419
%global sogui_hash 4b0019d1ecc2b9ad3e77333b9f243b57a15ebc4e
%global sogui_short %(c=%{soanydata_hash}; echo ${c:0:10})
%global sogui_date 20200419

Name:           SoQt
Version:        1.6.0
Release:        21%{?dist}
Summary:        High-level 3D visualization library
# Old version had been licensed GPLv2
License:        BSD-3-Clause

URL:            http://www.coin3d.org
Source0:        https://github.com/coin3d/soqt/archive/%{name}-%{version}.tar.gz

Source1:        https://github.com/coin3d/cpack.d/archive/%{cpack_hash}/coin3d-cpack-%{cpack_date}git%{cpack_short}.tar.gz
Source2:        https://github.com/coin3d/soanydata/archive/%{soanydata_hash}/coin3d-soanydata-%{soanydata_date}git%{soanydata_short}.tar.gz
Source3:        https://github.com/coin3d/sogui/archive/%{sogui_hash}/coin3d-sogui-%{sogui_date}git%{sogui_short}.tar.gz

Patch1:         SoQt-1.6.0-cmake.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  /usr/bin/iconv
BuildRequires:  /usr/bin/perl
BuildRequires:  Coin4-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libXi-devel

Provides:       Coin4-SoQt = %{version}-%{release}

%description
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

%package devel
Summary: Development files for SoQt
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: Coin4-devel
Requires: qt5-qtbase-devel
Requires: libXi-devel

Provides: Coin4-SoQt-devel = %{version}-%{release}

%description devel
Development package for SoQt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n soqt-%{name}-%{version}

mkdir cpack.d data src/Inventor/Qt/common
tar --strip-components=1 -C cpack.d -xf %{SOURCE1}
tar --strip-components=1 -C data -xf %{SOURCE2}
tar --strip-components=1 -C src/Inventor/Qt/common -xf %{SOURCE3}

# Some sources are ISO-8859-1 encoded
# We want doxygen to generate utf-8 encoded docs from them
for nonUTF8 in \
  src/Inventor/Qt/common/SoGuiRenderArea.cpp.in \
  src/Inventor/Qt/common/viewers/SoGuiExaminerViewer.cpp.in \
  src/Inventor/Qt/common/viewers/SoGuiFullViewer.h.in \
  src/Inventor/Qt/common/viewers/SoGuiViewer.cpp.in \
; do \
  %{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
  mv -f $nonUTF8.conv $nonUTF8
done

# No timestamps in doxygen generated docs!
sed -i -e 's,HTML_TIMESTAMP.*= YES,HTML_TIMESTAMP = NO,' \
  src/Inventor/Qt/common/sogui.doxygen.cmake.in

%build
mkdir build-%{_build_arch} && cd build-%{_build_arch}
%cmake -DSOQT_BUILD_DOCUMENTATION=TRUE \
       -DSOQT_BUILD_DOC_MAN=TRUE \
       -S .. -B .

%make_build

%install
cd build-%{_build_arch}
%make_install

# Move the headers to the same directory as Coin4.
mkdir -p %{buildroot}%{_includedir}/Coin4
mv %{buildroot}%{_includedir}/Inventor %{buildroot}%{_includedir}/Coin4/

# Remove stray files
rm -rf %{buildroot}/usr/share/info/SoQt1

%files
%doc AUTHORS ChangeLog* README
%license COPYING
%{_libdir}/libSoQt.so.*

%files devel
%{_docdir}/%{name}/html/
%{_datadir}/%{name}/
%{_includedir}/Coin4/Inventor/
%{_libdir}/libSoQt.so
%{_libdir}/pkgconfig/SoQt.pc
%{_libdir}/cmake/%{name}-%{version}/
%{_mandir}/man?/*.?.gz

%changelog
%autochangelog
