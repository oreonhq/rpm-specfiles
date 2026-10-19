%global source0_hash 5c55b744399c25532d63a0d2789b109df8d46fc93752d46b0782991a931a782f
%bcond check 0
%global debug_package %{nil}
%global crate scale-info
Name:           rust-scale-info
Version:        1.0.0
Release:        1%{?dist}
Summary:        Info about SCALE encodable Rust types
License:        Apache-2.0
URL:            https://crates.io/crates/scale-info
Source0:        https://static.crates.io/crates/scale-info/scale-info-%{version}.crate
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
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+bitvec-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+bitvec-devel

This package contains library source intended for building other packages which
use the "bitvec" feature of the "%{crate}" crate.

%package     -n %{name}+decode-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+decode-devel

This package contains library source intended for building other packages which
use the "decode" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+scale-info-derive-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+scale-info-derive-devel

This package contains library source intended for building other packages which
use the "scale-info-derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Info about SCALE encodable Rust types
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Info about SCALE encodable Rust types
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
%files -n rust-scale-info-devel -f %{oreon_filedir}/rust-scale-info-devel.list

%changelog

%autochangelog
