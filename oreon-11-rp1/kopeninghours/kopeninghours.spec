%global source0_hash 674f7dd168679eecbc85d7e68052a0a979f4243a432958a698ba5bbd82178589
Name:    kopeninghours
Version: 25.12.3
Release:        2%{?dist}
Summary:        Library for parsing and evaluating OSM opening hours expressions
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  python3-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DBUILD_QCH=OFF -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kopeninghours-devel -f %{oreon_filedir}/kopeninghours-devel.list
%files -n kopeninghours-doc -f %{oreon_filedir}/kopeninghours-doc.list

%changelog

%autochangelog
