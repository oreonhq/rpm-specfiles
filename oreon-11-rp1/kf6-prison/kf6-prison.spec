%global source0_hash ad24dd64b5150ec9ebc4df9734b4c2a58c27a588eafeb4239cdcef01629fe696

%define framework prison

%global stable_kf6 stable
%global majmin_ver_kf6 6.28

Name:		kf6-%{framework}
Summary:	KDE Frameworks 6 Tier 1 barcode library
Version:	6.28.0
Release:        1%{?dist}
License:	BSD-3-Clause AND CC0-1.0 AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	cmake(ZXing)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(libqrencode)

Requires:	kf6-filesystem
Requires:	qrencode-libs%{?_isa}
Requires:	libdmtx%{?_isa}

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
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
%files
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6Prison.so.%{version}
%{_kf6_libdir}/libKF6PrisonScanner.so.6
%{_kf6_libdir}/libKF6PrisonScanner.so.%{version}
%{_qt6_qmldir}/org/kde/prison/

%files devel
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so
%{_kf6_libdir}/cmake/KF6Prison/


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

