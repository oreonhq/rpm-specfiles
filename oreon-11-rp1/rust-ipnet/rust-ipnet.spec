%global source0_hash d98f6fed1fde3f8c21bc40a1abb88dd75e67924f9cffc3ef95607bad8017f8e2
%bcond check 0
%global debug_package %{nil}
%global crate ipnet
Name:           rust-ipnet
Version:        2.12.0
Release:        1%{?dist}
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ipnet
Source0:        https://static.crates.io/crates/ipnet/ipnet-%{version}.crate
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
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+schemars-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+schemars-devel

This package contains library source intended for building other packages which
use the "schemars" feature of the "%{crate}" crate.

%package     -n %{name}+schemars08-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+schemars08-devel

This package contains library source intended for building other packages which
use the "schemars08" feature of the "%{crate}" crate.

%package     -n %{name}+schemars1-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+schemars1-devel

This package contains library source intended for building other packages which
use the "schemars1" feature of the "%{crate}" crate.

%package     -n %{name}+ser_as_str-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+ser_as_str-devel

This package contains library source intended for building other packages which
use the "ser_as_str" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Provides types and useful methods for working with IPv4 and IPv6 netw...
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
%files -n rust-ipnet-devel -f %{oreon_filedir}/rust-ipnet-devel.list

%changelog

%autochangelog
