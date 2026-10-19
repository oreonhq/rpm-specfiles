%global source0_hash 8e9c5777e732316ec6d3088bf1b39abcf407f88f52f66be2720da41979f2cefe
%global commit aaf963c95b30b9afb2b3749bb078f973ac3ab19a
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251209
Name:           dynamic-hibernate
Version:        0.1.0%{?commitdate:~git%{commitdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Automatic dynamic swapfile management on Btrfs for hibernation
SourceLicense:  (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0
License:        (GPL-2.0-only OR GPL-3.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
URL:            https://invent.kde.org/tduck/dynamic-hibernate
Source0:        https://invent.kde.org/tduck/%{name}/-/archive/%{commit}/%{name}-aaf963c.tar.gz
Patch:          https://invent.kde.org/tduck/dynamic-hibernate/-/merge_requests/1.patch
Requires:       dbus-common
ExcludeArch:   %{ix86} %{arm32} %{riscv32}
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  cmake(KF6I18n)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This software enables dynamically creating swapfiles before hibernation
on btrfs-based systems (as well as automatically hiding the bootloader
on systemd-boot based systems), and then allows you to hibernate to it.

This circumvents the requirement for a swap partition or pre-existing swapfile.

It also provides a notifier which alerts the user if and why hibernation fails.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cmake_install
%oreon_autofiles main

%post

%systemd_post %{name}-prepare.service %{name}-cleanup.service
%systemd_user_post %{name}-notifier.service
%preun

%systemd_preun %{name}-prepare.service %{name}-cleanup.service
%systemd_user_preun %{name}-notifier.service
%postun

%systemd_postun_with_restart %{name}-prepare.service %{name}-cleanup.service
%systemd_user_postun_with_restart %{name}-notifier.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
