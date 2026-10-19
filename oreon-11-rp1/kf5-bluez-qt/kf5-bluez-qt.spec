%global source0_hash 1bab900d6984f4cbec517354cd6ffb11fd1f50887c5bf711ff4305376e039627
%undefine __cmake_in_source_build
%global framework bluez-qt
Name:           kf5-%{framework}
Summary:        A Qt wrapper for Bluez
Version: 5.116.0
Release:        1%{?dist}
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Requires:       kf5-filesystem >= %{version}
Requires:       bluez >= 5
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  systemd
# /oreon:deps
%description
BluezQt is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-bluez-qt-devel -f %{oreon_filedir}/kf5-bluez-qt-devel.list

%changelog

%autochangelog
