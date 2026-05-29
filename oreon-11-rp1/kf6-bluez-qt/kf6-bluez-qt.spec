%global source0_hash 907cf77ca2bf0417dad49ac3ebfe51300102029b93520dce5cfa5c35e25e5ab3

%global framework bluez-qt

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

 
Name:           kf6-%{framework}
Summary:        A Qt wrapper for Bluez
Version:        6.24.0
Release:	5%{?dist}
 
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/%{framework}
 
%global versiondir %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.kde.org/stable/frameworks/6.24/bluez-qt-6.24.0.tar.xz
Source1:        https://download.kde.org/stable/frameworks/6.24/bluez-qt-6.24.0.tar.xz.sig

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
 

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{framework}-%{version} -p1
 
%build
 %{cmake_kf6} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
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

