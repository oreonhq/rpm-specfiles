%global source0_hash 3704c90942fd68803e22bfe8b344740f5dfbfd6755453d8e7177bd86a49b5b07

%global framework kxmlrpcclient

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 3 library for interaction with XML RPC services

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 3 library for interaction with XML RPC services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kio-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5XmlRpcClient.so.*

%files devel

%{_kf5_includedir}/KXmlRpcClient/
%{_kf5_libdir}/libKF5XmlRpcClient.so
%{_kf5_libdir}/cmake/KF5XmlRpcClient/
%{_kf5_archdatadir}/mkspecs/modules/qt_KXmlRpcClient.pri

%changelog
%autochangelog
