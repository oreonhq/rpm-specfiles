%global source0_hash 4fc858248ea01b66f19d8e8a6d55f41deaf91e9d495246fd01368d99935c6c01
%bcond check 0
%global debug_package %{nil}
%global crate sysinfo
Name:           rust-sysinfo0.33
Version:        0.33.1
Release:        1%{?dist}
Summary:        Get system information such as processes, CPUs, disks, components and networks
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
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+c-interface-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+c-interface-devel

This package contains library source intended for building other packages which
use the "c-interface" feature of the "%{crate}" crate.

%package     -n %{name}+component-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+component-devel

This package contains library source intended for building other packages which
use the "component" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+disk-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+disk-devel

This package contains library source intended for building other packages which
use the "disk" feature of the "%{crate}" crate.

%package     -n %{name}+linux-netdevs-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+linux-netdevs-devel

This package contains library source intended for building other packages which
use the "linux-netdevs" feature of the "%{crate}" crate.

%package     -n %{name}+linux-tmpfs-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+linux-tmpfs-devel

This package contains library source intended for building other packages which
use the "linux-tmpfs" feature of the "%{crate}" crate.

%package     -n %{name}+multithread-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+multithread-devel

This package contains library source intended for building other packages which
use the "multithread" feature of the "%{crate}" crate.

%package     -n %{name}+network-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+network-devel

This package contains library source intended for building other packages which
use the "network" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+system-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+system-devel

This package contains library source intended for building other packages which
use the "system" feature of the "%{crate}" crate.

%package     -n %{name}+user-devel
Summary:        Get system information such as processes, CPUs, disks, components and networks
BuildArch:      noarch
%description -n %{name}+user-devel

This package contains library source intended for building other packages which
use the "user" feature of the "%{crate}" crate.

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
%files -n rust-sysinfo0.33-devel -f %{oreon_filedir}/rust-sysinfo0.33-devel.list

%changelog

%autochangelog
