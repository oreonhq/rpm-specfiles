%global source0_hash dc53198b8e237c451c68dba8411a1f8bd92787657689f24d67ae3d6b98c39f59
%bcond check 0
%global debug_package %{nil}
%global crate scientific
Name:           rust-scientific
Version:        0.5.2
Release:        1%{?dist}
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
License:        MIT
URL:            https://crates.io/crates/scientific
Source0:        https://static.crates.io/crates/scientific/scientific-%{version}.crate
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
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-devel
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
BuildArch:      noarch
%description -n %{name}+arc-devel

This package contains library source intended for building other packages which
use the "arc" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+macro-devel
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
BuildArch:      noarch
%description -n %{name}+macro-devel

This package contains library source intended for building other packages which
use the "macro" feature of the "%{crate}" crate.

%package     -n %{name}+scientific-macro-devel
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
BuildArch:      noarch
%description -n %{name}+scientific-macro-devel

This package contains library source intended for building other packages which
use the "scientific-macro" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Arbitrary precision scientific number (no_std capable, in pure Rust)
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
%files -n rust-scientific-devel -f %{oreon_filedir}/rust-scientific-devel.list

%changelog

%autochangelog
