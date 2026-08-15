%global source0_hash 9afe5ca9d1c4bd06479b2619326ec6f1e3c3998859dceaae3da9a4b7318d5a21

%global framework kcmutils

%global stable_kf6 stable
%global majmin_ver_kf6 6.28


Name:    kf6-%{framework}
Version: 6.28.0
Release:        2%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extra API to write KConfigModules

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons) >= %{version}
BuildRequires:  cmake(KF6I18n) >= %{version}
BuildRequires:  cmake(KF6IconThemes) >= %{version}
BuildRequires:  cmake(KF6ItemViews) >= %{version}
BuildRequires:  cmake(KF6Package) >= %{version}
BuildRequires:  cmake(KF6XmlGui) >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6KIO) >= %{version}
BuildRequires:  cmake(KF6GuiAddons) >= %{version}
BuildRequires:  cmake(KF6WindowSystem) >= %{version}
BuildRequires:  cmake(KF6ColorScheme) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6Kirigami) >= %{version}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires: kf6-filesystem
Requires: qt6qml(org.kde.kirigami)

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ConfigWidgets)
Requires:       cmake(KF6Service)
Requires:       cmake(Qt6Qml)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kcms

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kcmshell6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6KCMUtils.so.*
%{_kf6_libdir}/libKF6KCMUtilsCore.so.*
%{_kf6_qmldir}/org/kde/kcmutils/
%{_kf6_qtplugindir}/kcms/
%{_libdir}/libKF6KCMUtilsQuick.so.6
%{_libdir}/libKF6KCMUtilsQuick.so.%{version}

%files devel
%{_kf6_includedir}/KCMUtils/
%{_kf6_includedir}/KCMUtilsCore/
%{_kf6_libdir}/libKF6KCMUtils.so
%{_libdir}/libKF6KCMUtilsQuick.so
%{_kf6_libdir}/libKF6KCMUtilsCore.so
%{_kf6_libdir}/cmake/KF6KCMUtils/
%{_kf6_libexecdir}/kcmdesktopfilegenerator
%{_kf6_includedir}/KCMUtilsQuick


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

