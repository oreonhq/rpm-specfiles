%global source0_hash 57da8dfb320575825854217e58a773d972c80e43031e83fd0e85cd2e68269884

%undefine __cmake_in_source_build

Name:           prison
Summary:        A Qt-based barcode abstraction library
Version:        1.1.1
Release:        29%{?dist}

License:        MIT
URL:            https://projects.kde.org/projects/kdesupport/prison
Source0:        http://download.kde.org/stable/prison/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches
# post 1.1.1 commits from master/ branch
Patch1: 0001-Add-automoc-increase-cmake-version.patch
Patch2: 0002-Allow-to-build-with-qt5-and-qt4.patch
Patch3: 0003-Generate-cmake-config-version-file.patch
Patch4: 0004-Fix-option-description.patch
Patch5: 0005-Fix-major-for-qt5.patch
Patch6: 0006-Use-ECM-to-locate-the-correct-install-paths-on-a-Qt5.patch
Patch7: 0007-Use-PRISON_VERSION_MAJOR-for-SOVERSION.patch
Patch8: 0008-increase-ECM.patch
Patch9: 0009-Set-also-QT_QTGUI_LIBARARY-as-that-this-variable-is-.patch
## upstreamable patch
# make -qt5 build fully parallel-installable
# needs work to be upstreamable, see 'sed' down in %%install section
Patch10: 0010-parallel-installable-prison-qt5.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(QtGui)
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5Test)
%endif

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%package qt5
Summary: A Qt5-based barcode abstraction library
%description qt5
Prison is a Qt5-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package qt5-devel
Summary: Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libprison.so.0*

%files devel
%{_includedir}/prison/
%{_libdir}/libprison.so
%{_libdir}/cmake/Prison/

%changelog
%autochangelog
