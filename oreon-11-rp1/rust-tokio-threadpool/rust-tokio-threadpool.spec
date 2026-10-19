%global source0_hash df720b6581784c118f0eb4310796b12b1d242a7eb95f716a8367855325c25f89
%bcond check 0
%global debug_package %{nil}
%global crate tokio-threadpool
Name:           rust-tokio-threadpool
Version:        0.1.18
Release:        1%{?dist}
Summary:        A task scheduler backed by a work-stealing thread pool.
License:        MIT
URL:            https://crates.io/crates/tokio-threadpool
Source0:        https://static.crates.io/crates/tokio-threadpool/tokio-threadpool-%{version}.crate
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
Summary:        A task scheduler backed by a work-stealing thread pool.
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
%files -n rust-tokio-threadpool-devel -f %{oreon_filedir}/rust-tokio-threadpool-devel.list

%changelog

%autochangelog
