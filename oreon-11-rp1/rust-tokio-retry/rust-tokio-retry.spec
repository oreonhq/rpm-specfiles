%global source0_hash 7f57eb36ecbe0fc510036adff84824dd3c24bb781e21bfa67b69d556aa85214f
%bcond check 0
%global debug_package %{nil}
%global crate tokio-retry
Name:           rust-tokio-retry
Version:        0.3.0
Release:        1%{?dist}
Summary:        Extensible, asynchronous retry behaviours for futures/tokio
License:        MIT
URL:            https://crates.io/crates/tokio-retry
Source0:        https://static.crates.io/crates/tokio-retry/tokio-retry-%{version}.crate
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
Summary:        Extensible, asynchronous retry behaviours for futures/tokio
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-tokio-retry-devel -f %{oreon_filedir}/rust-tokio-retry-devel.list

%changelog

%autochangelog
