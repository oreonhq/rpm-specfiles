%global source0_hash 84b514d95a258be801fde8a1ff1c974f4a4841d9750f5d1d6690fc07a5ad4049
%bcond check 0
%global debug_package %{nil}
%global crate puffin
Name:           rust-puffin
Version:        0.20.0
Release:        1%{?dist}
Summary:        Simple instrumentation profiler for games
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/puffin
Source0:        https://static.crates.io/crates/puffin/puffin-%{version}.crate
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
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bincode-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+bincode-devel

This package contains library source intended for building other packages which
use the "bincode" feature of the "%{crate}" crate.

%package     -n %{name}+lz4-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+lz4-devel

This package contains library source intended for building other packages which
use the "lz4" feature of the "%{crate}" crate.

%package     -n %{name}+lz4_flex-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+lz4_flex-devel

This package contains library source intended for building other packages which
use the "lz4_flex" feature of the "%{crate}" crate.

%package     -n %{name}+packing-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+packing-devel

This package contains library source intended for building other packages which
use the "packing" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialization-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+serialization-devel

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%package     -n %{name}+web-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+web-devel

This package contains library source intended for building other packages which
use the "web" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        Simple instrumentation profiler for games
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

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
%files -n rust-puffin-devel -f %{oreon_filedir}/rust-puffin-devel.list

%changelog

%autochangelog
