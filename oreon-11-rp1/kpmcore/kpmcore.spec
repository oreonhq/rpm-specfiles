%global stable_kf6 stable
%global source0_hash 22cac5b6432c4ad606aef72bf884983d9cb7d5245c43e75edd1c5a36f9058668
%global kf6min 5.240.0
%global qt6min 6.5.0
%global sover 13
Name:           kpmcore
Version:        26.08.1
Release:        1%{?dist}
Summary:        Library for managing partitions by KDE programs
License:        GPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0
URL:            https://github.com/KDE/kpmcore
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       e2fsprogs
Requires:       kf6-filesystem
Recommends:     dosfstools
Recommends:     exfatprogs
Recommends:     f2fs-tools
Recommends:     fatresize
Recommends:     hfsutils
Recommends:     hfsplus-tools
Recommends:     jfsutils
Recommends:     nilfs-utils
Recommends:     ocfs2-tools
Recommends:     udftools
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
# /oreon:deps
%description
KPMcore contains common code for managing partitions by KDE Partition Manager 
and other KDE projects

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6min}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%find_lang %{name}._policy_
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kpmcore-devel -f %{oreon_filedir}/kpmcore-devel.list

%changelog

%autochangelog

