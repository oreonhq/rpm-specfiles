%global source0_hash b87fb29e4354acb21f085b7978c7f1f49f41766a1d4f98fc86781fb9884a0841
%global framework krunner
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution with parallelized query system
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
KRunner provides a parallelized query system extendable via plugins.

%package        devel
Summary:        Development files for %{name}
Conflicts:      kapptemplate < 16.03.80
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-plasma-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-krunner-devel -f %{oreon_filedir}/kf5-krunner-devel.list

%changelog

%autochangelog
