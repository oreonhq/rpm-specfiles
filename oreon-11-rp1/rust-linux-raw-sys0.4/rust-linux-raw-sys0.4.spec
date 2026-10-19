%global source0_hash d26c52dbd32dccf2d10cac7725f8eae5296885fb5703b261f7d0a0739ec807ab
%bcond check 0
%global debug_package %{nil}
%global crate linux-raw-sys
Name:           rust-linux-raw-sys0.4
Version:        0.4.15
Release:        1%{?dist}
Summary:        Generated bindings for Linux's userspace API
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/linux-raw-sys
Source0:        https://static.crates.io/crates/linux-raw-sys/linux-raw-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bootparam-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+bootparam-devel

This package contains library source intended for building other packages which
use the "bootparam" feature of the "%{crate}" crate.

%package     -n %{name}+btrfs-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+btrfs-devel

This package contains library source intended for building other packages which
use the "btrfs" feature of the "%{crate}" crate.

%package     -n %{name}+compiler_builtins-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+compiler_builtins-devel

This package contains library source intended for building other packages which
use the "compiler_builtins" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+elf-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+elf-devel

This package contains library source intended for building other packages which
use the "elf" feature of the "%{crate}" crate.

%package     -n %{name}+elf_uapi-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+elf_uapi-devel

This package contains library source intended for building other packages which
use the "elf_uapi" feature of the "%{crate}" crate.

%package     -n %{name}+errno-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+errno-devel

This package contains library source intended for building other packages which
use the "errno" feature of the "%{crate}" crate.

%package     -n %{name}+general-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+general-devel

This package contains library source intended for building other packages which
use the "general" feature of the "%{crate}" crate.

%package     -n %{name}+if_arp-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+if_arp-devel

This package contains library source intended for building other packages which
use the "if_arp" feature of the "%{crate}" crate.

%package     -n %{name}+if_ether-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+if_ether-devel

This package contains library source intended for building other packages which
use the "if_ether" feature of the "%{crate}" crate.

%package     -n %{name}+if_packet-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+if_packet-devel

This package contains library source intended for building other packages which
use the "if_packet" feature of the "%{crate}" crate.

%package     -n %{name}+io_uring-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+io_uring-devel

This package contains library source intended for building other packages which
use the "io_uring" feature of the "%{crate}" crate.

%package     -n %{name}+ioctl-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+ioctl-devel

This package contains library source intended for building other packages which
use the "ioctl" feature of the "%{crate}" crate.

%package     -n %{name}+landlock-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+landlock-devel

This package contains library source intended for building other packages which
use the "landlock" feature of the "%{crate}" crate.

%package     -n %{name}+loop_device-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+loop_device-devel

This package contains library source intended for building other packages which
use the "loop_device" feature of the "%{crate}" crate.

%package     -n %{name}+mempolicy-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+mempolicy-devel

This package contains library source intended for building other packages which
use the "mempolicy" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+netlink-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+netlink-devel

This package contains library source intended for building other packages which
use the "netlink" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%package     -n %{name}+prctl-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+prctl-devel

This package contains library source intended for building other packages which
use the "prctl" feature of the "%{crate}" crate.

%package     -n %{name}+ptrace-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+ptrace-devel

This package contains library source intended for building other packages which
use the "ptrace" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+system-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+system-devel

This package contains library source intended for building other packages which
use the "system" feature of the "%{crate}" crate.

%package     -n %{name}+xdp-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+xdp-devel

This package contains library source intended for building other packages which
use the "xdp" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-linux-raw-sys0.4-devel -f %{oreon_filedir}/rust-linux-raw-sys0.4-devel.list

%changelog

%autochangelog
