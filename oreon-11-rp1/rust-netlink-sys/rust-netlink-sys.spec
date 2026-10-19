%global source0_hash c99d38e00b420df49e940fe0826e667c3dad82ac68eb4c2bbf754c1c14a83a10
%bcond check 0
%global debug_package %{nil}
%global crate netlink-sys
Name:           rust-netlink-sys
Version:        0.9.0
Release:        1%{?dist}
Summary:        netlink sockets, with optional integration with tokio
License:        MIT
URL:            https://crates.io/crates/netlink-sys
Source0:        https://static.crates.io/crates/netlink-sys/netlink-sys-%{version}.crate
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
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+mio-devel
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+mio-devel

This package contains library source intended for building other packages which
use the "mio" feature of the "%{crate}" crate.

%package     -n %{name}+mio_socket-devel
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+mio_socket-devel

This package contains library source intended for building other packages which
use the "mio_socket" feature of the "%{crate}" crate.

%package     -n %{name}+smol_socket-devel
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+smol_socket-devel

This package contains library source intended for building other packages which
use the "smol_socket" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        netlink sockets, with optional integration with tokio
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_socket-devel
Summary:        netlink sockets, with optional integration with tokio
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
%files -n rust-netlink-sys-devel -f %{oreon_filedir}/rust-netlink-sys-devel.list

%changelog

%autochangelog
