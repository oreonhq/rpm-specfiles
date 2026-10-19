%global source0_hash 90f60a3ee149005c5819e03e3d73ba4a470bc18b52b0c8422cfe1bea2cae63c6
%bcond check 0
%global debug_package %{nil}
%global crate rtnetlink
Name:           rust-rtnetlink
Version:        0.23.0
Release:        1%{?dist}
Summary:        manipulate linux networking resources via netlink
License:        MIT
URL:            https://crates.io/crates/rtnetlink
Source0:        https://static.crates.io/crates/rtnetlink/rtnetlink-%{version}.crate
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
Summary:        manipulate linux networking resources via netlink
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-global-executor-devel
Summary:        manipulate linux networking resources via netlink
BuildArch:      noarch
%description -n %{name}+async-global-executor-devel

This package contains library source intended for building other packages which
use the "async-global-executor" feature of the "%{crate}" crate.

%package     -n %{name}+smol_socket-devel
Summary:        manipulate linux networking resources via netlink
BuildArch:      noarch
%description -n %{name}+smol_socket-devel

This package contains library source intended for building other packages which
use the "smol_socket" feature of the "%{crate}" crate.

%package     -n %{name}+test_as_root-devel
Summary:        manipulate linux networking resources via netlink
BuildArch:      noarch
%description -n %{name}+test_as_root-devel

This package contains library source intended for building other packages which
use the "test_as_root" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        manipulate linux networking resources via netlink
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_socket-devel
Summary:        manipulate linux networking resources via netlink
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
%files -n rust-rtnetlink-devel -f %{oreon_filedir}/rust-rtnetlink-devel.list

%changelog

%autochangelog
