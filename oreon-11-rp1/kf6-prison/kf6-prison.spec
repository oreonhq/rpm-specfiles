%define framework prison

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Summary:	KDE Frameworks 6 Tier 1 barcode library
Version:	6.24.0
Release:	4%{?dist}
License:	BSD-3-Clause AND CC0-1.0 AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

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

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package	html
Summary:	Developer Documentation files for %{name} in HTML format
BuildArch:	noarch
%description	html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

# Qt6 qdoc: list all files under %{_qt6_docdir} except tags/index (-devel owns those).
: > %{_builddir}/%{framework}-qt6doc.files
if [ -d "%{buildroot}%{_qt6_docdir}" ]; then
  find "%{buildroot}%{_qt6_docdir}" -type f \
    ! -name '*.tags' ! -name '*.index' \
    | sed "s#^%{buildroot}##" >> %{_builddir}/%{framework}-qt6doc.files
fi
LC_ALL=C sort -u -o %{_builddir}/%{framework}-qt6doc.files %{_builddir}/%{framework}-qt6doc.files

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

%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files html -f %{_builddir}/%{framework}-qt6doc.files

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

