%global source0_hash 747d141f216eb25e563473c3cdabb6ee9b38bcc31742d1fcfa1143be794f66f0
%undefine __cmake_in_source_build
%global framework kpeople
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 library for contact and people aggregation
License: CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 3 library for interaction with XML RPC services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%{cmake_kf5} \
    -DENABLE_EXAMPLES:BOOL=OFF
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_kf5_qtplugindir}/kpeople/{actions,datasource,widgets}
%find_lang %{name} --all-name
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kpeople-devel -f %{oreon_filedir}/kf5-kpeople-devel.list

%changelog

%autochangelog
