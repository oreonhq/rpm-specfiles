%global framework bluez-qt

%global stable_kf6 stable
%global majmin_ver_kf6 6.24
 
Name:           kf6-%{framework}
Summary:        A Qt wrapper for Bluez
Version:        6.24.0
Release:	3%{?dist}
 
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/%{framework}
 
%global versiondir %(echo %{version} | cut -d. -f1-2)
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:	gcc-c++
BuildRequires:  cmake
 
# For %%{_udevrulesdir}
BuildRequires:  systemd
 
Requires:       kf6-filesystem >= %{version}
Recommends:     bluez >= 5
 
%description
BluezQt is Qt-based library written handle all Bluetooth functionality.
 
%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
Development files for %{name}.
 

%package	html
Summary:	Developer Documentation files for %{name} in HTML format
BuildArch:	noarch
%description	html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1
 
%build
 %{cmake_kf6} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
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
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKF6BluezQt.so.*
%{_kf6_qmldir}/org/kde/bluezqt/
 
%files devel
%{_kf6_includedir}/BluezQt/ 
%{_kf6_libdir}/libKF6BluezQt.so
%{_kf6_libdir}/cmake/KF6BluezQt/
%{_kf6_libdir}/pkgconfig/KF6BluezQt.pc

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

