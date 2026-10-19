%global source0_hash 986c5ce3b994526b3cd75578e62554abd09f0899d6206de48b3e96ab34ccc8c7
%bcond check 0
%global debug_package %{nil}
%global crate hyperlocal
Name:           rust-hyperlocal
Version:        0.9.1
Release:        1%{?dist}
Summary:        Hyper bindings for Unix domain sockets
License:        MIT
URL:            https://crates.io/crates/hyperlocal
Source0:        https://static.crates.io/crates/hyperlocal/hyperlocal-%{version}.crate
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
Summary:        Hyper bindings for Unix domain sockets
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        Hyper bindings for Unix domain sockets
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+http-body-util-devel
Summary:        Hyper bindings for Unix domain sockets
BuildArch:      noarch
%description -n %{name}+http-body-util-devel

This package contains library source intended for building other packages which
use the "http-body-util" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-util-devel
Summary:        Hyper bindings for Unix domain sockets
BuildArch:      noarch
%description -n %{name}+hyper-util-devel

This package contains library source intended for building other packages which
use the "hyper-util" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Hyper bindings for Unix domain sockets
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+tower-service-devel
Summary:        Hyper bindings for Unix domain sockets
BuildArch:      noarch
%description -n %{name}+tower-service-devel

This package contains library source intended for building other packages which
use the "tower-service" feature of the "%{crate}" crate.

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
%files -n rust-hyperlocal-devel -f %{oreon_filedir}/rust-hyperlocal-devel.list

%changelog

%autochangelog
