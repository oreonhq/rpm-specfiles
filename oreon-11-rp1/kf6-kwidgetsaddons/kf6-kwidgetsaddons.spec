%global source0_hash dfe563e58b0d8c72e8a1da4f379f03610552d8663eac613e47a2a6a384c20107

%global		framework kwidgetsaddons

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	6%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-qttools-static
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	fdupes

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets.

%package	-n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description	-n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 kwidgetsaddons6_qt
%fdupes %{buildroot}/%{_kf6_includedir}/KWidgetsAddons/
%fdupes LICENSES

%files -f kwidgetsaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6WidgetsAddons.so.*
%{_kf6_datadir}/qlogging-categories6/*categories

%files -n python3-%{name}
%{python3_sitearch}/KWidgetsAddons.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so
%{_kf6_libdir}/cmake/KF6WidgetsAddons/
%{_kf6_qtplugindir}/designer/kwidgetsaddons6widgets.so


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

