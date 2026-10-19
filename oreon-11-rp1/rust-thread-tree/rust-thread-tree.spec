%global source0_hash ffbd370cb847953a25954d9f63e14824a36113f8c72eecf6eccef5dc4b45d630
%bcond check 0
%global debug_package %{nil}
%global crate thread-tree
Name:           rust-thread-tree
Version:        0.3.3
Release:        1%{?dist}
Summary:        A tree-structured thread pool for splitting jobs hierarchically on wo...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/thread-tree
Source0:        https://static.crates.io/crates/thread-tree/thread-tree-%{version}.crate
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
Summary:        A tree-structured thread pool for splitting jobs hierarchically on wo...
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
%files -n rust-thread-tree-devel -f %{oreon_filedir}/rust-thread-tree-devel.list

%changelog

%autochangelog
