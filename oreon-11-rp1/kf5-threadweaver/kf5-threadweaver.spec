%global source0_hash 9723dc652df9a2df8b6b9909af5bf0de3b3eb3aaed260a6419df2b0ddbe8eae0

%undefine __cmake_in_source_build
%global framework threadweaver

Name:           kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon for advanced thread management

License:        CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 addon for advanced thread management.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
# TODO: Please submit an issue to upstream (rhbz#2380680)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5ThreadWeaver.so.*

%files devel
%{_kf5_includedir}/ThreadWeaver/

%{_kf5_libdir}/libKF5ThreadWeaver.so
%{_kf5_libdir}/cmake/KF5ThreadWeaver/
%{_kf5_archdatadir}/mkspecs/modules/qt_ThreadWeaver.pri

%changelog
%autochangelog
