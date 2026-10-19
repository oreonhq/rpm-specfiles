%global source0_hash 5c6532e5b62b652073bff0e2050ef57e4697a853be118d6c57c32b59fffdeaab
%bcond check 1
%global debug_package %{nil}
%global crate toml-span
Name:           rust-toml-span
Version:        0.6.0
Release:        1%{?dist}
Summary:        Toml parser and deserializer that preserves span information
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml-span
Source0:        https://static.crates.io/crates/toml-span/toml-span-%{version}.crate
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
Summary:        Toml parser and deserializer that preserves span information
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+reporting-devel
Summary:        Toml parser and deserializer that preserves span information
BuildArch:      noarch
%description -n %{name}+reporting-devel

This package contains library source intended for building other packages which
use the "reporting" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Toml parser and deserializer that preserves span information
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-toml-span-devel -f %{oreon_filedir}/rust-toml-span-devel.list

%changelog

%autochangelog
