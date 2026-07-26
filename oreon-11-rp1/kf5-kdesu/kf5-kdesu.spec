%global source0_hash 01c9c884ff92e23fcabc95da7445ada07d5ce5057f19a4ea4f452048d0e0d8cb

%undefine __cmake_in_source_build
%global framework kdesu

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 integration with su

License: CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kpty-devel >= %{majmin}
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 3 integration with su for elevated privileges.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kpty-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang kdesu5_qt --all-name

%ldconfig_scriptlets

%files -f kdesu5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*
%{_kf5_libdir}/libKF5Su.so.*
%{_kf5_libexecdir}/kdesu_stub
%attr(2755,root,nobody) %{_kf5_libexecdir}/kdesud

%files devel

%{_kf5_includedir}/KDESu/
%{_kf5_libdir}/libKF5Su.so
%{_kf5_libdir}/cmake/KF5Su/
%{_kf5_archdatadir}/mkspecs/modules/qt_KDESu.pri

%changelog
%autochangelog
