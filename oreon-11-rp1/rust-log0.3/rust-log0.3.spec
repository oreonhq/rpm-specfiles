%global source0_hash e19e8d5c34a3e0e2223db8e060f9e8264aeeb5c5fc64a4ee9965c062211c024b
%bcond check 0
%global debug_package %{nil}
%global crate log
Name:           rust-log0.3
Version:        0.3.9
Release:        1%{?dist}
Summary:        A lightweight logging facade for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/log
Source0:        https://static.crates.io/crates/log/log-%{version}.crate
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
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_debug-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_debug-devel

This package contains library source intended for building other packages which
use the "max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_error-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_error-devel

This package contains library source intended for building other packages which
use the "max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_info-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_info-devel

This package contains library source intended for building other packages which
use the "max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_off-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_off-devel

This package contains library source intended for building other packages which
use the "max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_trace-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_trace-devel

This package contains library source intended for building other packages which
use the "max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_warn-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_warn-devel

This package contains library source intended for building other packages which
use the "max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_debug-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_debug-devel

This package contains library source intended for building other packages which
use the "release_max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_error-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_error-devel

This package contains library source intended for building other packages which
use the "release_max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_info-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_info-devel

This package contains library source intended for building other packages which
use the "release_max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_off-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_off-devel

This package contains library source intended for building other packages which
use the "release_max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_trace-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_trace-devel

This package contains library source intended for building other packages which
use the "release_max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_warn-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_warn-devel

This package contains library source intended for building other packages which
use the "release_max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        A lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

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
%files -n rust-log0.3-devel -f %{oreon_filedir}/rust-log0.3-devel.list

%changelog

%autochangelog
