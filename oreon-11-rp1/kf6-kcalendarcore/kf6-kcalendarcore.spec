%global		framework kcalendarcore

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	4%{?dist}
Summary:	KDE Frameworks 6 Tier 1 KCalendarCore Library
License:	BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	bison
BuildRequires:	libical-devel
BuildRequires:	qt6-qtbase-devel
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:  cmake(Qt6Qml)

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = :%{version}-%{release}
Requires:	libical-devel
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
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*kcalendarcore.*
%{_kf6_libdir}/libKF6CalendarCore.so.*
%{_kf6_qmldir}/org/kde/calendarcore/

%files devel
%{_kf6_includedir}/KCalendarCore/
%{_kf6_libdir}/libKF6CalendarCore.so
%{_kf6_libdir}/cmake/KF6CalendarCore/
%{_kf6_libdir}/pkgconfig/KF6CalendarCore.pc

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

