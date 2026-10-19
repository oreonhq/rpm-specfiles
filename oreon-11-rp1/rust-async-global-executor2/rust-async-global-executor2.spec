%global source0_hash 05b1b633a2115cd122d73b955eadd9916c18c8f510ec9cd1686404c60ad1c29c
%bcond check 1
%global debug_package %{nil}
%global crate async-global-executor
Name:           rust-async-global-executor2
Version:        2.4.1
Release:        1%{?dist}
Summary:        Global executor built on top of async-executor and async-io
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-global-executor
Source0:        https://static.crates.io/crates/async-global-executor/async-global-executor-%{version}.crate
Patch:          async-global-executor-fix-metadata.diff
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
Summary:        Global executor built on top of async-executor and async-io
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        Global executor built on top of async-executor and async-io
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Global executor built on top of async-executor and async-io
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-crate-devel
Summary:        Global executor built on top of async-executor and async-io
BuildArch:      noarch
%description -n %{name}+tokio-crate-devel

This package contains library source intended for building other packages which
use the "tokio-crate" feature of the "%{crate}" crate.

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
%files -n rust-async-global-executor2-devel -f %{oreon_filedir}/rust-async-global-executor2-devel.list

%changelog

%autochangelog
