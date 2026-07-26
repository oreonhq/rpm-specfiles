%global source0_hash 1bab900d6984f4cbec517354cd6ffb11fd1f50887c5bf711ff4305376e039627

%undefine __cmake_in_source_build
%global framework bluez-qt

Name:           kf5-%{framework}
Summary:        A Qt wrapper for Bluez
Version: 5.116.0
Release: 5%{?dist}

License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

# For %%{_udevrulesdir}
BuildRequires:  systemd

Requires:       kf5-filesystem >= %{version}
%if 0%{?fedora} > 22
Recommends:     bluez >= 5
%else
Requires:       bluez >= 5
%endif

%if 0%{?fedora} >= 22
## libbluedevil 5.2.2 was the last release
Obsoletes:      libbluedevil < 5.2.90
%endif

%description
BluezQt is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}
%if 0%{?fedora} >= 22
## libbluedevil 5.2.2 was the last release
Obsoletes:      libbluedevil-devel < 5.2.90
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%{cmake_kf5} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_libdir}/libKF5BluezQt.so.*
%{_kf5_qmldir}/org/kde/bluezqt/
%{_udevrulesdir}/61-kde-bluetooth-rfkill.rules

%files devel
%{_kf5_includedir}/BluezQt/

%{_kf5_libdir}/libKF5BluezQt.so
%{_kf5_libdir}/cmake/KF5BluezQt/
%{_kf5_libdir}/pkgconfig/KF5BluezQt.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_BluezQt.pri

%changelog
%autochangelog
