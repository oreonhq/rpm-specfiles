%global source0_hash da882b89e91da979a91f6cc32f54e5bdbb18c6b46280a032a2225e30a03390fd
%bcond check 1
%global debug_package %{nil}
%global crate pci-driver
Name:           rust-pci-driver
Version:        0.1.4
Release:        1%{?dist}
Summary:        PCI/PCIe driver development library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pci-driver
Source0:        https://static.crates.io/crates/pci-driver/pci-driver-%{version}.crate
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
Summary:        PCI/PCIe driver development library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_unsafe-op-in-unsafe-fn-devel
Summary:        PCI/PCIe driver development library
BuildArch:      noarch
%description -n %{name}+_unsafe-op-in-unsafe-fn-devel

This package contains library source intended for building other packages which
use the "_unsafe-op-in-unsafe-fn" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        PCI/PCIe driver development library
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+vfio-devel
Summary:        PCI/PCIe driver development library
BuildArch:      noarch
%description -n %{name}+vfio-devel

This package contains library source intended for building other packages which
use the "vfio" feature of the "%{crate}" crate.

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
%files -n rust-pci-driver-devel -f %{oreon_filedir}/rust-pci-driver-devel.list

%changelog

%autochangelog
