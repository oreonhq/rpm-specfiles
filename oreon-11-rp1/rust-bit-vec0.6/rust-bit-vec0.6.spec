%global source0_hash 349f9b6a179ed607305526ca489b34ad0a41aed5f7980fa90eb03160b69598fb
%bcond check 0
%global debug_package %{nil}
%global crate bit-vec
Name:           rust-bit-vec0.6
Version:        0.6.3
Release:        1%{?dist}
Summary:        A vector of bits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bit-vec
Source0:        https://static.crates.io/crates/bit-vec/bit-vec-%{version}.crate
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
Summary:        A vector of bits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A vector of bits
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_no_std-devel
Summary:        A vector of bits
BuildArch:      noarch
%description -n %{name}+serde_no_std-devel

This package contains library source intended for building other packages which
use the "serde_no_std" feature of the "%{crate}" crate.

%package     -n %{name}+serde_std-devel
Summary:        A vector of bits
BuildArch:      noarch
%description -n %{name}+serde_std-devel

This package contains library source intended for building other packages which
use the "serde_std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A vector of bits
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
%files -n rust-bit-vec0.6-devel -f %{oreon_filedir}/rust-bit-vec0.6-devel.list

%changelog

%autochangelog
