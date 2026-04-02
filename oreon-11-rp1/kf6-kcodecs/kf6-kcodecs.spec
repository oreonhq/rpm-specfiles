%global		framework kcodecs

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with string manipulation methods
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MPL-1.1
URL:		https://invent.kde.org/frameworks/%{framework}
Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gperf
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with string manipulation methods.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 kcodecs6_qt
%fdupes LICENSES

%files -f kcodecs6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Codecs.so.*

%files devel
%{_kf6_includedir}/KCodecs/
%{_kf6_libdir}/libKF6Codecs.so
%{_kf6_libdir}/cmake/KF6Codecs/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
