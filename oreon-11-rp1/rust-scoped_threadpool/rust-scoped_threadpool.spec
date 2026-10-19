%global source0_hash 1d51f5df5af43ab3f1360b429fa5e0152ac5ce8c0bd6485cae490332e96846a8
%bcond check 0
%global debug_package %{nil}
%global crate scoped_threadpool
Name:           rust-scoped_threadpool
Version:        0.1.9
Release:        1%{?dist}
Summary:        Library for scoped and cached threadpools
License:        MIT
URL:            https://crates.io/crates/scoped_threadpool
Source0:        https://static.crates.io/crates/scoped_threadpool/scoped_threadpool-%{version}.crate
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
Summary:        Library for scoped and cached threadpools
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Library for scoped and cached threadpools
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-scoped_threadpool-devel -f %{oreon_filedir}/rust-scoped_threadpool-devel.list

%changelog

%autochangelog
