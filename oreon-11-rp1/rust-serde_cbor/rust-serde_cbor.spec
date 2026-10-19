%global source0_hash 2bef2ebfde456fb76bbcf9f59315333decc4fda0b2b44b420243c11e0f5ec1f5
%bcond check 0
%global debug_package %{nil}
%global crate serde_cbor
Name:           rust-serde_cbor
Version:        0.11.2
Release:        1%{?dist}
Summary:        CBOR support for serde.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_cbor
Source0:        https://static.crates.io/crates/serde_cbor/serde_cbor-%{version}.crate
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
Summary:        CBOR support for serde.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        CBOR support for serde.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        CBOR support for serde.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tags-devel
Summary:        CBOR support for serde.
BuildArch:      noarch
%description -n %{name}+tags-devel

This package contains library source intended for building other packages which
use the "tags" feature of the "%{crate}" crate.

%package     -n %{name}+unsealed_read_write-devel
Summary:        CBOR support for serde.
BuildArch:      noarch
%description -n %{name}+unsealed_read_write-devel

This package contains library source intended for building other packages which
use the "unsealed_read_write" feature of the "%{crate}" crate.

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
%files -n rust-serde_cbor-devel -f %{oreon_filedir}/rust-serde_cbor-devel.list

%changelog

%autochangelog
