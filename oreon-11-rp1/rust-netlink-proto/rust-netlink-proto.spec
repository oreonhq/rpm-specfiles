%global source0_hash 97e03ae6247c6cdb499e8f14e98c72b83954d85822b687056e3a21150b438f2b
%bcond check 0
%global debug_package %{nil}
%global crate netlink-proto
Name:           rust-netlink-proto
Version:        0.13.0
Release:        1%{?dist}
Summary:        async netlink protocol
License:        MIT
URL:            https://crates.io/crates/netlink-proto
Source0:        https://static.crates.io/crates/netlink-proto/netlink-proto-%{version}.crate
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
Summary:        async netlink protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+smol_socket-devel
Summary:        async netlink protocol
BuildArch:      noarch
%description -n %{name}+smol_socket-devel

This package contains library source intended for building other packages which
use the "smol_socket" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_socket-devel
Summary:        async netlink protocol
BuildArch:      noarch
%description -n %{name}+tokio_socket-devel

This package contains library source intended for building other packages which
use the "tokio_socket" feature of the "%{crate}" crate.

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
%files -n rust-netlink-proto-devel -f %{oreon_filedir}/rust-netlink-proto-devel.list

%changelog

%autochangelog
