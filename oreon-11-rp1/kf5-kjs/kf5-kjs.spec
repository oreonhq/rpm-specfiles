%global source0_hash 9fb4f33e31d5b31eb6449311c1c61acaa968d42419252c0ab9dccb1f5fd9e1b7
%global framework kjs
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 functional module with JavaScript interpreter
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/Attic/frameworks/%{majmin}/portingAids/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pcre-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
KDE Frameworks 1 Tier 1 functional module with JavaScript interpret.

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

%cmake_kf5
%cmake_build
%install
%cmake_install
chmod +x %{buildroot}%{_kf5_datadir}/kf5/kjs/create_hash_table
%find_lang %{name} --with-man --all-name
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kjs-devel -f %{oreon_filedir}/kf5-kjs-devel.list

%changelog

%autochangelog
