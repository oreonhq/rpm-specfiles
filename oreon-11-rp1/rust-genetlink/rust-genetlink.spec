%global source0_hash b0bc61df27194def0f714249ee8a5abb15f031daa8d1eff1c0bf661aee80203d
%bcond check 0
%global debug_package %{nil}
%global crate genetlink
Name:           rust-genetlink
Version:        0.3.0
Release:        1%{?dist}
Summary:        communicate with generic netlink
License:        MIT
URL:            https://crates.io/crates/genetlink
Source0:        https://static.crates.io/crates/genetlink/genetlink-%{version}.crate
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
Summary:        communicate with generic netlink
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        communicate with generic netlink
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+smol_socket-devel
Summary:        communicate with generic netlink
BuildArch:      noarch
%description -n %{name}+smol_socket-devel

This package contains library source intended for building other packages which
use the "smol_socket" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        communicate with generic netlink
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_socket-devel
Summary:        communicate with generic netlink
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
%files -n rust-genetlink-devel -f %{oreon_filedir}/rust-genetlink-devel.list

%changelog

%autochangelog
