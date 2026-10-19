%global source0_hash 0a5b4ddaee55fb2bea2bf0e5000747e5f5c0de765e5a5ff87f4cd106439f4bb3
%bcond check 0
%global debug_package %{nil}
%global crate sysinfo
Name:           rust-sysinfo0.30
Version:        0.30.13
Release:        1%{?dist}
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
License:        MIT
URL:            https://crates.io/crates/sysinfo
Source0:        https://static.crates.io/crates/sysinfo/sysinfo-%{version}.crate
Patch:          sysinfo-fix-metadata-auto.diff
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
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+c-interface-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+c-interface-devel

This package contains library source intended for building other packages which
use the "c-interface" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+linux-netdevs-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+linux-netdevs-devel

This package contains library source intended for building other packages which
use the "linux-netdevs" feature of the "%{crate}" crate.

%package     -n %{name}+linux-tmpfs-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+linux-tmpfs-devel

This package contains library source intended for building other packages which
use the "linux-tmpfs" feature of the "%{crate}" crate.

%package     -n %{name}+multithread-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+multithread-devel

This package contains library source intended for building other packages which
use the "multithread" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library to get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-sysinfo0.30-devel -f %{oreon_filedir}/rust-sysinfo0.30-devel.list

%changelog

%autochangelog
