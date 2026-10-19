%global source0_hash 01c95bfe8fb2c366b5f54c8be5e9679bd36ec5e1df59e94f95fdd4af697aca13
%bcond check 0
%global debug_package %{nil}
%global crate capnp-rpc
Name:           rust-capnp-rpc
Version:        0.27.0
Release:        1%{?dist}
Summary:        implementation of the Cap'n Proto remote procedure call protocol
License:        MIT
URL:            https://crates.io/crates/capnp-rpc
Source0:        https://static.crates.io/crates/capnp-rpc/capnp-rpc-%{version}.crate
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
Summary:        implementation of the Cap'n Proto remote procedure call protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-capnp-rpc-devel -f %{oreon_filedir}/rust-capnp-rpc-devel.list

%changelog

%autochangelog
