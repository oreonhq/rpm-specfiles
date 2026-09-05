%global source0_hash 52a4ccb2af5d63c6d046c6208485118f8db51eaf51c6b875f73f266d39302f1a

%global         base_name breeze-plymouth

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plymouth-theme-breeze
Version: 6.7.4
Release: 1%{?dist}
Summary: Breeze theme for Plymouth

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL:     https://invent.kde.org/plasma/%{base_name}

Source0: https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

Source10: plymouth-theme-breeze.conf

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  plymouth-devel

Provides:       %{base_name} = %{version}-%{release}

Requires:       plymouth
Requires:       plymouth-plugin-script

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

%files
%license LICENSES/*.txt
%{_libdir}/plymouth/breeze-text.so
%{_datadir}/plymouth/themes/breeze-text/
%{_datadir}/plymouth/themes/breeze/
%{_prefix}/lib/dracut/dracut.conf.d/10-plymouth-theme-breeze.conf

%changelog
%autochangelog
