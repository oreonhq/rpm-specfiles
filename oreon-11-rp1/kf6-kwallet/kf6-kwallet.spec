%global source1_hash 14737f6ec33d928bc6d76a0fac029f510a8d1d8e37adf149eb243d4f782aeda8
%global source0_hash 93cb9c1df2630807c04bf8c30312e75ae3bb466c77dd9b29bb2c752e71d34a26
%global framework kwallet
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 solution for password management
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf6-filesystem
Requires:       pinentry-gui
Requires:       qca-qt6-ossl%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gpgmepp%{?_isa}
%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kwallet-libs -f %{oreon_filedir}/kf6-kwallet-libs.list
%files -n kf6-kwallet-devel -f %{oreon_filedir}/kf6-kwallet-devel.list

%changelog

%autochangelog
