%global framework kunitconversion

%global stable_kf6 stable
%global majmin_ver_kf6 6.24


Name:    kf6-%{framework}
Version: 6.24.0
Release:	6%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for unit conversions

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# oreon url source checksums begin
%global source0_sha256 a0cd582e48c302d56b5ebcea560b5590f94b8615dbd54bc67bcd165714979fa6
%global source0_file kunitconversion-6.24.0.tar.xz
# oreon url source checksums end

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6I18n)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 2 addon for unit conversions.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/kunitconversion-6.24.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a0cd582e48c302d56b5ebcea560b5590f94b8615dbd54bc67bcd165714979fa6" || { echo "oreon: Source0 SHA256 mismatch for kunitconversion-6.24.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6UnitConversion.so.*
%{_kf6_datadir}/qlogging-categories6/%{framework}.*

%files -n python3-%{name}
%{python3_sitearch}/KUnitConversion.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KUnitConversion/
%{_kf6_libdir}/libKF6UnitConversion.so
%{_kf6_libdir}/cmake/KF6UnitConversion/


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

