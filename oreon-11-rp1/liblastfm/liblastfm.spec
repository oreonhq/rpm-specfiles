%global source0_hash e8d1b3b2ea6f09f771d3d243db58d0a6e2756040503f554b125ddfd1ca6bda36
%global __cmake_in_source_build 1
%define fingerprint 1
%global commit 2e8e40d78a331d8e39fe39113bcb7571a7b1d4d6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:    liblastfm
Summary:        Libraries to integrate Last.fm services
Version: 1.1.0
Release:        21%{?dist}
License: GPL-2.0-or-later
URL:     https://github.com/drfiemost/liblastfm
Source0:        https://github.com/drfiemost/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0: make_work_with_stricter_compilation_flags.patch
%if 0%{?fingerprint}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  fftw3-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  ruby
# /oreon:deps
%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software.

%package qt6
Summary: Libraries to integrate Last.fm services
%description qt6
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software.

%package qt6-fingerprint
Summary: Liblastfm fingerprint library
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-fingerprint
%{summary}.

%package qt6-devel
Summary: Development files for %{name}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%if 0%{?fingerprint}
Requires: %{name}-qt6-fingerprint%{?_isa} = %{version}-%{release}
%endif
%description qt6-devel
%{summary}.

%package qt5
Summary: Qt5 libraries to integrate Last.fm services
%description qt5
%{summary}.

%package qt5-fingerprint
Summary: Liblastfm5 fingerprint library
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-fingerprint
%{summary}.

%package qt5-devel
Summary: Development files for liblastfm-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%if 0%{?fingerprint}
Requires: %{name}-qt5-fingerprint%{?_isa} = %{version}-%{release}
%endif
%description qt5-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake .. \
  -DBUILD_FINGERPRINT:BOOL=%{?fingerprint:ON}%{!?fingerprint:OFF} \
  -DBUILD_WITH_QT5:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build
popd
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%cmake .. \
  -DBUILD_FINGERPRINT:BOOL=%{?fingerprint:ON}%{!?fingerprint:OFF} \
  -DBUILD_WITH_QT5:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build
%install
pushd %{_target_platform}-qt5
%cmake_install
popd
pushd %{_target_platform}
%cmake_install
popd
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export CTEST_OUTPUT_ON_FAILURE=1
pushd %{_target_platform}
%ctest -E UrlBuilderTest
popd
%if 0%{?qt5}
pushd %{_target_platform}-qt5
%ctest -E UrlBuilderTest
popd
%endif
%ldconfig_scriptlets -n liblastfm6-qt6
%files -f %{oreon_filedir}/main.list
%files -n liblastfm-qt6 -f %{oreon_filedir}/liblastfm-qt6.list
%files -n liblastfm-qt6-fingerprint -f %{oreon_filedir}/liblastfm-qt6-fingerprint.list
%files -n liblastfm-qt6-devel -f %{oreon_filedir}/liblastfm-qt6-devel.list
%files -n liblastfm-qt5 -f %{oreon_filedir}/liblastfm-qt5.list
%files -n liblastfm-qt5-fingerprint -f %{oreon_filedir}/liblastfm-qt5-fingerprint.list
%files -n liblastfm-qt5-devel -f %{oreon_filedir}/liblastfm-qt5-devel.list

%changelog

%autochangelog
