%global framework kjobwidgets
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	4%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for KJobs
# The following are in the LICENSES folder, but go unused: LGPL-3.0-only, LicenseRef-KDE-Accepted-LGPL
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  pkgconfig(shiboken6)
BuildRequires:  pkgconfig(pyside6)
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel

BuildRequires:  pkgconfig(xkbcommon)
Requires:       kf6-filesystem

%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
%description    devel
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

%find_lang_kf6 kjobwidgets6_qt

%files -f kjobwidgets6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6JobWidgets.so.*

%files -n python3-%{name}
%{python3_sitearch}/KJobWidgets.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KJobWidgets/
%{_kf6_libdir}/libKF6JobWidgets.so
%{_kf6_libdir}/cmake/KF6JobWidgets/
%{_kf6_datadir}/dbus-1/interfaces/*.xml

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

