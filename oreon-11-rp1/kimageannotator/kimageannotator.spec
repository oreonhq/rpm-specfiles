%global source0_hash 7eb593d975b1590a184354ef68dbc3c26479d58eaea00de461d73695176f623c
%global source1_hash e78c785ec4a8a22a48a91835c97601f5704b5076b154415353b0d2697dc0b4f7

%undefine __cmake_in_source_build

# Bundled here for %%build so mock does not need kcolorpicker-devel in the root yet.
# Runtime still needs kcolorpicker-libs from the separate kcolorpicker SRPM.
%global kcp_version 0.3.1

Name:           kimageannotator
Version:        0.7.2
Release:        3%{?dist}
Summary:        Image annotation widget library for Qt (ksnip)
License:        LGPL-3.0-or-later
URL:            https://github.com/ksnip/kImageAnnotator

Source0:        https://github.com/ksnip/kImageAnnotator/archive/refs/tags/v%{version}.tar.gz#/kImageAnnotator-%{version}.tar.gz
Source1:        https://github.com/ksnip/kColorPicker/archive/refs/tags/v%{kcp_version}.tar.gz#/kColorPicker-%{kcp_version}.tar.gz
Patch1:         kimageannotator-qt6-output-name.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  libX11-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
kImageAnnotator provides a Qt widget for drawing arrows, text, blur, and
similar annotations on images. Used by Gwenview, ksnip, and other apps.

%package libs
Summary:        Qt6 kImageAnnotator shared library
Requires:       kcolorpicker-libs%{?_isa}

%description libs
Shared library and translation files for kImageAnnotator.

%package devel
Summary:        Development files for kimageannotator
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets)
Requires:       cmake(Qt6Svg)
Requires:       kcolorpicker-devel%{?_isa}

%description devel
Headers and CMake package kImageAnnotator-Qt6 for downstream builds.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n kImageAnnotator-%{version}
tar -xf %{SOURCE1} -C %{_builddir}

%build
kcp_src="%{_builddir}/kColorPicker-%{kcp_version}"
kcp_stage="%{_builddir}/kcp-stage/usr"
mkdir -p "$kcp_stage"

pushd "$kcp_src"
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_EXAMPLE=OFF \
  -DBUILD_TESTS=OFF
%cmake_build
cmake --install "%{__cmake_builddir}" --prefix "$kcp_stage"
popd

pushd "%{_builddir}/kImageAnnotator-%{version}"
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_EXAMPLE=OFF \
  -DBUILD_TESTS=OFF \
  -DCMAKE_PREFIX_PATH="$kcp_stage"
%cmake_build
popd

%install
pushd "%{_builddir}/kImageAnnotator-%{version}"
%cmake_install
popd

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md CHANGELOG.md

%files libs
%{_libdir}/libkImageAnnotator-Qt6.so.0*
%{_datadir}/kImageAnnotator/translations/*.qm

%files devel
%{_includedir}/kImageAnnotator-Qt6/
%{_libdir}/libkImageAnnotator-Qt6.so
%{_libdir}/cmake/kImageAnnotator-Qt6/

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-3
- Qt6 build installs libkImageAnnotator-Qt6.so (Gwenview DT_NEEDED)

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-2
- Bundle kColorPicker %%build-only staging (find_package without kcolorpicker-devel in mock)
- kimageannotator-libs Requires kcolorpicker-libs

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-1
- Add kImageAnnotator Qt6 (cmake kImageAnnotator-Qt6 for Gwenview)
