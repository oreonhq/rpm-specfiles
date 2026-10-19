%global source0_hash 330a5ed07fa54e4702c9d6c4174f74427fc0ef6e214bbd677ae50a5099946470
%bcond check 0
%global debug_package %{nil}
%global crate anyhow
Name:           rust-anyhow
Version:        1.0.104
Release:        1%{?dist}
Summary:        Flexible concrete Error type built on std::error::Error
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anyhow
Source0:        https://static.crates.io/crates/anyhow/anyhow-%{version}.crate
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
Summary:        Flexible concrete Error type built on std::error::Error
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Flexible concrete Error type built on std::error::Error
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Flexible concrete Error type built on std::error::Error
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
%files -n rust-anyhow-devel -f %{oreon_filedir}/rust-anyhow-devel.list

%changelog

%autochangelog
