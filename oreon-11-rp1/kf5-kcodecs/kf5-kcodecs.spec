%global source0_hash a489d22e91cafcb60854c6e914969e1f3f8270b403baf2ec3a1d76ae2bd3680e

%undefine __cmake_in_source_build
%global framework kcodecs

Name:           kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with string manipulation methods

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MPL-1.1
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  gperf
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 addon with string manipulation methods.

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
%{cmake_kf5}

%cmake_build

%install
%cmake_install

%find_lang_kf5 kcodecs5_qt

%ldconfig_scriptlets

%files -f kcodecs5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_libdir}/libKF5Codecs.so.*

%files devel

%{_kf5_includedir}/KCodecs/
%{_kf5_libdir}/libKF5Codecs.so
%{_kf5_libdir}/cmake/KF5Codecs/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCodecs.pri

%changelog
%autochangelog
