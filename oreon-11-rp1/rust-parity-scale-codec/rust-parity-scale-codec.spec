%global source0_hash 373b1a4c1338d9cd3d1fa53b3a11bdab5ab6bd80a20f7f7becd76953ae2be909
%bcond check 0
%global debug_package %{nil}
%global crate parity-scale-codec
Name:           rust-parity-scale-codec
Version:        2.3.1
Release:        1%{?dist}
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
License:        Apache-2.0
URL:            https://crates.io/crates/parity-scale-codec
Source0:        https://static.crates.io/crates/parity-scale-codec/parity-scale-codec-%{version}.crate
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
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+bitvec-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+bitvec-devel

This package contains library source intended for building other packages which
use the "bitvec" feature of the "%{crate}" crate.

%package     -n %{name}+chain-error-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+chain-error-devel

This package contains library source intended for building other packages which
use the "chain-error" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+fuzz-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+fuzz-devel

This package contains library source intended for building other packages which
use the "fuzz" feature of the "%{crate}" crate.

%package     -n %{name}+generic-array-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+generic-array-devel

This package contains library source intended for building other packages which
use the "generic-array" feature of the "%{crate}" crate.

%package     -n %{name}+max-encoded-len-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+max-encoded-len-devel

This package contains library source intended for building other packages which
use the "max-encoded-len" feature of the "%{crate}" crate.

%package     -n %{name}+parity-scale-codec-derive-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+parity-scale-codec-derive-devel

This package contains library source intended for building other packages which
use the "parity-scale-codec-derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SCALE - Simple Concatenating Aggregated Little Endians
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
%files -n rust-parity-scale-codec-devel -f %{oreon_filedir}/rust-parity-scale-codec-devel.list

%changelog

%autochangelog
