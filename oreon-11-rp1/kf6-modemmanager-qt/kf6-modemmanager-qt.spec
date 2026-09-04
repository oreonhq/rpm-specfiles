%global source0_hash 742891c3c1dfcd6c9eaa2b1664cfe7e9b311187eec7ecd9d8812829dce8485c9

%global framework modemmanager-qt

%global stable_kf6 stable
%global majmin_ver_kf6 6.28

Name:    kf6-%{framework}
Version: 6.29.0
Release:        1%{?dist}
Summary: A Tier 1 KDE Frameworks module wrapping ModemManager DBus API
License: GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ModemManager-devel >= 1.0.0
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem

%description
A Qt 6 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       qt6-qtbase-devel
%description    devel
Qt 6 libraries and header files for developing applications
that use ModemManager.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%doc README README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/qlogging-categories6/*.renamecategories
%{_kf6_libdir}/libKF6ModemManagerQt.so.*

%files devel
%{_kf6_libdir}/libKF6ModemManagerQt.so
%{_kf6_libdir}/cmake/KF6ModemManagerQt/
%{_kf6_includedir}/ModemManagerQt/


%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.29.0-1
- Latest upstream release

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-2
- Prepare for Oreon 11 (RP1)

