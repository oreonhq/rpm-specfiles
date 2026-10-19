%global source0_hash 0fa23c3f5a8e6aeaf76e1c3f1ff7c10046d4ad925798907cf5b28c9788d297bd
%global base_name libktorrent
ExcludeArch: %{ix86}
Name:    kf5-libktorrent
Summary:        Library providing torrent downloading code
Version: 23.08.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/network/%{base_name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libgcrypt-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: boost-devel
Requires: gmp-devel%{?_isa}
Requires: libgcrypt-devel
Requires: cmake(KF5Archive)
Requires: cmake(KF5Config)
Requires: cmake(KF5KIO)
Requires: cmake(Qt5Network)
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang libktorrent5
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-libktorrent-devel -f %{oreon_filedir}/kf5-libktorrent-devel.list

%changelog

%autochangelog
