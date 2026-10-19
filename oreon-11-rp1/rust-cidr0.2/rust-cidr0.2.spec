%global source0_hash 6bdf600c45bd958cf2945c445264471cca8b6c8e67bc87b71affd6d7e5682621
%bcond check 0
%global debug_package %{nil}
%global crate cidr
Name:           rust-cidr0.2
Version:        0.2.3
Release:        1%{?dist}
Summary:        IP network and IP host within network types
License:        MIT
URL:            https://crates.io/crates/cidr
Source0:        https://static.crates.io/crates/cidr/cidr-%{version}.crate
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
Summary:        IP network and IP host within network types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitstring-devel
Summary:        IP network and IP host within network types
BuildArch:      noarch
%description -n %{name}+bitstring-devel

This package contains library source intended for building other packages which
use the "bitstring" feature of the "%{crate}" crate.

%package     -n %{name}+no_unsafe-devel
Summary:        IP network and IP host within network types
BuildArch:      noarch
%description -n %{name}+no_unsafe-devel

This package contains library source intended for building other packages which
use the "no_unsafe" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        IP network and IP host within network types
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        IP network and IP host within network types
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
%files -n rust-cidr0.2-devel -f %{oreon_filedir}/rust-cidr0.2-devel.list

%changelog

%autochangelog
