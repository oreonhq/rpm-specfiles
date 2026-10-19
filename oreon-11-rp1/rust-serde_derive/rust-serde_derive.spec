%global source0_hash e7a5d71263a5a7d47b41f6b3f06ba276f10cc18b0931f1799f710578e2309348
%bcond check 0
%global debug_package %{nil}
%global crate serde_derive
Name:           rust-serde_derive
Version:        1.0.229
Release:        1%{?dist}
Summary:        Macros 1.1 implementation of #[derive(Serialize, Deserialize)]
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_derive
Source0:        https://static.crates.io/crates/serde_derive/serde_derive-%{version}.crate
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
Summary:        Macros 1.1 implementation of #[derive(Serialize, Deserialize)]
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+deserialize_in_place-devel
Summary:        Macros 1.1 implementation of #[derive(Serialize, Deserialize)]
BuildArch:      noarch
%description -n %{name}+deserialize_in_place-devel

This package contains library source intended for building other packages which
use the "deserialize_in_place" feature of the "%{crate}" crate.

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
%files -n rust-serde_derive-devel -f %{oreon_filedir}/rust-serde_derive-devel.list

%changelog

%autochangelog
