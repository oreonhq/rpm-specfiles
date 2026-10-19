%global stable_kf6 stable
%global source0_hash 0a55d129024f39b474ceb108bfa536caca15fea6cb0fb3aa7bb0b87acc476845
Name:           libktorrent
Summary:        Torrent downloading library for KDE 6 applications
Version:        26.08.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/network/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libgcrypt-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       libgcrypt-devel%{?_isa}
Requires:       cmake(KF6Archive)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6KIO)
Requires:       cmake(Qt6Network)
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name}6 --with kde
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libktorrent-devel -f %{oreon_filedir}/libktorrent-devel.list

%changelog

%autochangelog

