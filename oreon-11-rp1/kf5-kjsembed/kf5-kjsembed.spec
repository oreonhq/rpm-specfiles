%global source0_hash 9b97d556b0c4e61154614879d804c98202dbde64ad352fbcab2b6f5e54b5b517
%undefine __cmake_in_source_build
%global framework kjsembed
ExcludeArch: %{ix86}
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 addon for binding JS objects to QObjects
License: LicenseRef-Callaway-LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/v%{version}/%{framework}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kjs-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-static
# /oreon:deps
%description
KSJEmbed provides a method of binding JavaScript objects to QObjects, so you
can script your applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kjs-devel >= %{majmin}
Requires:       kf5-ki18n-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-v%{version}

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-man
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kjsembed-devel -f %{oreon_filedir}/kf5-kjsembed-devel.list

%changelog

%autochangelog
