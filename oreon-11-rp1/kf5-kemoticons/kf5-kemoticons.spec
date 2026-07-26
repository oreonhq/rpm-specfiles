%global source0_hash ac63341b07fe151dcbb622495d9cfd5d42fbfc4c4e67bf915b8eec03cf626853

%undefine __cmake_in_source_build
%global framework kemoticons

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 module with support for emoticons and emoticons themes

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 3 module that provides emoticons themes as well as
helper classes to automatically convert text emoticons to graphical emoticons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kservice-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_libdir}/libKF5Emoticons.so.*
%{_kf5_plugindir}/emoticonsthemes/
%{_kf5_plugindir}/KEmoticonsIntegrationPlugin.so
%{_kf5_datadir}/kservices5/*
%{_kf5_datadir}/kservicetypes5/*
# track specific emoticon themes or not?  (no, for now) -- rex
%{_kf5_datadir}/emoticons/

%files devel

%{_kf5_includedir}/KEmoticons/
%{_kf5_libdir}/libKF5Emoticons.so
%{_kf5_libdir}/cmake/KF5Emoticons/
%{_kf5_archdatadir}/mkspecs/modules/qt_KEmoticons.pri

%changelog
%autochangelog
