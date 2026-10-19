%global source1_hash baabc5ff3ac59f8c5e116b39d404bbcd7870a601edc508ecd76204ae4c35e0c4
%global source0_hash f5045b14a6c689bbfded9437582f943dd4f8f74537085ab6115bcacdea2110d8
%global framework bluez-qt
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:           kf6-%{framework}
Summary:        A Qt wrapper for Bluez
Version:        6.30.0
Release:        1%{?dist}
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/%{framework}
%global versiondir %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem >= %{version}
Recommends:     bluez >= 5
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  systemd
# /oreon:deps
%description
BluezQt is Qt-based library written handle all Bluetooth functionality.
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
Development files for %{name}.
 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1
 
%build

 %{cmake_kf6} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-bluez-qt-devel -f %{oreon_filedir}/kf6-bluez-qt-devel.list

%changelog

%autochangelog
