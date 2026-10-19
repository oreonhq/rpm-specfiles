%global source0_hash 8b75356056920673b02621b35afd0f7dda9306d03c79a30f5c56c44cf256e3de
%bcond check 0
%global debug_package %{nil}
%global crate async-task
Name:           rust-async-task
Version:        4.7.1
Release:        1%{?dist}
Summary:        Task abstraction for building executors
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-task
Source0:        https://static.crates.io/crates/async-task/async-task-%{version}.crate
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
Summary:        Task abstraction for building executors
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        Task abstraction for building executors
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Task abstraction for building executors
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
%files -n rust-async-task-devel -f %{oreon_filedir}/rust-async-task-devel.list

%changelog

%autochangelog
