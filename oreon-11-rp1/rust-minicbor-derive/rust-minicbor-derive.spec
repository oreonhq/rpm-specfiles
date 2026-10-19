%global source0_hash bd2209fff77f705b00c737016a48e73733d7fbccb8b007194db148f03561fb70
%bcond check 1
%global debug_package %{nil}
%global crate minicbor-derive
Name:           rust-minicbor-derive
Version:        0.15.3
Release:        1%{?dist}
Summary:        Derive minicbor Decode and Encode traits
License:        BlueOak-1.0.0
URL:            https://crates.io/crates/minicbor-derive
Source0:        https://static.crates.io/crates/minicbor-derive/minicbor-derive-%{version}.crate
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
Summary:        Derive minicbor Decode and Encode traits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Derive minicbor Decode and Encode traits
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Derive minicbor Decode and Encode traits
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
%files -n rust-minicbor-derive-devel -f %{oreon_filedir}/rust-minicbor-derive-devel.list

%changelog

%autochangelog
