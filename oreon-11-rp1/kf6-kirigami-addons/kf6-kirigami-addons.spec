%global source0_hash 4ae9ef9cf1fc55fef59328d25a70b28572b6f6a787394c3d292f5ed378f19840
%global framework kirigami-addons
%global orig_name kirigami-addons
%ifarch aarch64
%global _lto_cflags %{nil}
%global _smp_mflags -j2
%endif
Name:           kf6-%{framework}
Version:        1.14.0
Release:        1%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/%{framework}
Source0:        https://download.kde.org/stable/%{framework}/%{framework}-%{version}.tar.xz
Requires: kf6-filesystem
Obsoletes: kf6-kirigami2-addons < 1:0.11.76-5
Provides:  kf6-kirigami2-addons = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons%{?_isa} = 1:%{version}-%{release}
Obsoletes: kf6-kirigami2-addons-dateandtime < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-dateandtime = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-dateandtime%{?_isa} = 1:%{version}-%{release}
Obsoletes: kf6-kirigami2-addons-treeview < 1:0.11.76-5
Provides:  kf6-kirigami2-addons-treeview = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons-treeview%{?_isa} = 1:%{version}-%{release}
Obsoletes: kf6-kirigami-addons-dateandtime < 0.11.76-5
Provides:  kf6-kirigami-addons-dateandtime = %{version}-%{release}
Provides:  kf6-kirigami-addons-dateandtime%{?_isa} = %{version}-%{release}
Obsoletes: kf6-kirigami-addons-treeview < 0.11.76-5
Provides:  kf6-kirigami-addons-treeview = %{version}-%{release}
Provides:  kf6-kirigami-addons-treeview%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package   devel
Summary:   Development files for %{name}
Requires:  %{name} = %{version}-%{release}
Conflicts: kf6-kirigami-addons < 1.4.0
%description devel
The %{name}-devel package contains CMake definitions, libraries
and header files for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version}

%build

%cmake_kf6 \
    -DBUILD_WITH_QT6=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{orig_name}6 --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kirigami-addons-devel -f %{oreon_filedir}/kf6-kirigami-addons-devel.list

%changelog

%autochangelog
