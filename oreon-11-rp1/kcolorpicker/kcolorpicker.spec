%global source0_hash e78c785ec4a8a22a48a91835c97601f5704b5076b154415353b0d2697dc0b4f7

%undefine __cmake_in_source_build

Name:           kcolorpicker
Version:        0.3.1
Release:        1%{?dist}
Summary:        Qt color picker widget library (ksnip)
License:        LGPL-3.0-or-later
URL:            https://github.com/ksnip/kColorPicker

Source0:        https://github.com/ksnip/kColorPicker/archive/refs/tags/v0.3.1.tar.gz#/kColorPicker-0.3.1.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
kColorPicker is a Qt widget library used by kImageAnnotator and similar apps.
This package is the documentation meta; install kcolorpicker-libs or
kcolorpicker-devel as needed.

%package libs
Summary:        Qt6 kColorPicker shared library

%description libs
Shared library for kColorPicker.

%package devel
Summary:        Development files for kcolorpicker
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets)

%description devel
Headers and CMake config for kColorPicker-Qt6.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n kColorPicker-%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_EXAMPLE=OFF \
  -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md

%files libs
%{_libdir}/libkColorPicker.so.0*

%files devel
%{_includedir}/kColorPicker-Qt6/
%{_libdir}/libkColorPicker.so
%{_libdir}/cmake/kColorPicker-Qt6/

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.1-1
- Add kColorPicker Qt6 (dependency for kImageAnnotator / Gwenview)
