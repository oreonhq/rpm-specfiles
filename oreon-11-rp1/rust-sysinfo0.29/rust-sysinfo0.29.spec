%global source0_hash cd727fc423c2060f6c92d9534cef765c65a6ed3f428a03d7def74a8c4348e666
%bcond check 1
%global debug_package %{nil}
%global crate sysinfo
Name:           rust-sysinfo0.29
Version:        0.29.11
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
%files -n rust-sysinfo0.29-devel -f %{oreon_filedir}/rust-sysinfo0.29-devel.list

%changelog

%autochangelog
