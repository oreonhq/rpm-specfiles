%global source0_hash ef53942eb7bf7ff43a617b3e2c1c4a5ecf5944a7c1bc12d7ee39bbb15e5c1519
%bcond check 0
%global debug_package %{nil}
%global crate linux-raw-sys
Name:           rust-linux-raw-sys0.3
Version:        0.3.8
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

%package     -n %{name}+ioctl-devel
Summary:        Generated bindings for Linux's userspace API
BuildArch:      noarch
%description -n %{name}+ioctl-devel

This package contains library source intended for building other packages which
use the "ioctl" feature of the "%{crate}" crate.

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
%files -n rust-linux-raw-sys0.3-devel -f %{oreon_filedir}/rust-linux-raw-sys0.3-devel.list

%changelog

%autochangelog
