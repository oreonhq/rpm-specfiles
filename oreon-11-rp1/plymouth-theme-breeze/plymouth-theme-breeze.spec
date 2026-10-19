%global source1_hash d0c1476e5a08ff68d9731d17efb0b9067ef6a2a20145ff6be7e0c42efb5037ee
%global source0_hash 9cb05ef4fed5ac19bc35f5c4b18ec425e499fae47d52d344821fbf38474c44a0
%global         base_name breeze-plymouth
ExcludeArch: %{ix86}
Name:    plymouth-theme-breeze
Version: 6.7.5
Release:        1%{?dist}
Summary:        Breeze theme for Plymouth
License: GPL-3.0-only
URL:     https://invent.kde.org/plasma/%{base_name}
Source0:        https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig
Source10: plymouth-theme-breeze.conf
Provides:       %{base_name} = %{version}-%{release}
Requires:       plymouth
Requires:       plymouth-plugin-script
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  plymouth-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
install -D -m644 -p %{SOURCE10} \
  %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/10-plymouth-theme-breeze.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
