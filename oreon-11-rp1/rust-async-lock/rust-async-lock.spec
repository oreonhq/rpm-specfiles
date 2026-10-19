%global source0_hash 290f7f2596bd5b78a9fec8088ccd89180d7f9f55b94b0576823bbbdc72ee8311
%bcond check 0
%global debug_package %{nil}
%global crate async-lock
Name:           rust-async-lock
Version:        3.4.2
Release:        1%{?dist}
Summary:        Async synchronization primitives
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-lock
Source0:        https://static.crates.io/crates/async-lock/async-lock-%{version}.crate
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
Summary:        Async synchronization primitives
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+loom-devel
Summary:        Async synchronization primitives
BuildArch:      noarch
%description -n %{name}+loom-devel

This package contains library source intended for building other packages which
use the "loom" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Async synchronization primitives
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
%files -n rust-async-lock-devel -f %{oreon_filedir}/rust-async-lock-devel.list

%changelog

%autochangelog
