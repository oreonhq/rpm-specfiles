%global source0_hash 623fd1c01db3fce83bbba055b3e801ea1414fb9eb06395dfb9164a984aa23742
%global source1_hash 7466a53fe9416230e39c053b895a2e5277c1fdec3b3e4b4193d2df8b0d50850d
%bcond_without check
%global udevdir %(pkg-config --variable=udevdir udev)
%global dracutdir %(pkg-config --variable=dracutdir dracut)
Name:           stratisd
Version:        3.9.3
Release:        1%{?dist}
Summary:        Daemon that manages block devices to create filesystems
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/stratis-storage/stratisd
Source0:        https://github.com/stratis-storage/stratisd/archive/refs/tags/stratisd-v3.9.3.tar.gz#/stratisd-3.9.3.tar.gz
Source1:        https://github.com/stratis-storage/stratisd/releases/download/stratisd-v3.8.6/stratisd-3.8.6-vendor.tar.gz
ExclusiveArch:  %{rust_arches}
Requires:       xfsprogs
Requires:       device-mapper-persistent-data
Requires:       systemd-libs
Requires:       dbus-libs
Requires:       cryptsetup-libs
Requires:       libblkid
Recommends:     clevis-luks >= 18
# oreon:deps
BuildRequires:  /bin/a2x
BuildRequires:  clang
BuildRequires:  cryptsetup-devel
BuildRequires:  dbus-devel
BuildRequires:  device-mapper-devel
BuildRequires:  dracut
BuildRequires:  glibc-static
BuildRequires:  libblkid-devel
BuildRequires:  rust-packaging
BuildRequires:  rust-srpm-macros
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
%{summary}.

%package dracut
Summary: Dracut modules for use with stratisd
ExclusiveArch:  %{rust_arches}
Requires:     stratisd
Requires:     dracut >= 051
Requires:     systemd
%description dracut
%{summary}.

%package tools
Summary: Tools that support Stratis operation
ExclusiveArch:  %{rust_arches}
Requires:     stratisd
%description tools
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stratisd-stratisd-v%{version}
%oreon_prep
%build

%{cargo_license -f engine,dbus_enabled,min,systemd_compat,extras,udev_scripts} > LICENSE.dependencies
%{__cargo} build %{?__cargo_common_opts} --release --bin=stratisd
%{__cargo} build %{?__cargo_common_opts} --release --bin=stratis-min --bin=stratisd-min --bin=stratis-utils --no-default-features --features engine,min,systemd_compat
%{__cargo} rustc %{?__cargo_common_opts} --release --bin=stratis-str-cmp --no-default-features --features udev_scripts -- -Ctarget-feature=+crt-static
%{__cargo} rustc %{?__cargo_common_opts} --release --bin=stratis-base32-decode --no-default-features --features udev_scripts -- -Ctarget-feature=+crt-static
%{__cargo} build %{?__cargo_common_opts} --release --bin=stratisd-tools --no-default-features --features engine,extras
a2x -f manpage docs/stratisd.txt
a2x -f manpage docs/stratis-dumpmetadata.txt
%{cargo_vendor_manifest}
%install
%make_install DRACUTDIR=%{dracutdir} PROFILEDIR=release
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- --no-run
%endif
%post

%systemd_post stratisd.service
%preun

%systemd_preun stratisd.service
%postun

%systemd_postun_with_restart stratisd.service
%files -f %{oreon_filedir}/main.list
%files -n stratisd-dracut -f %{oreon_filedir}/stratisd-dracut.list
%files -n stratisd-tools -f %{oreon_filedir}/stratisd-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8.6-1
- Prepare for Oreon 11 (RP1)
