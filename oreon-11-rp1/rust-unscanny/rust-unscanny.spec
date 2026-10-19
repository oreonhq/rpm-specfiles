%global source0_hash e9df2af067a7953e9c3831320f35c1cc0600c30d44d9f7a12b01db1cd88d6b47
%bcond check 0
%global debug_package %{nil}
%global crate unscanny
Name:           rust-unscanny
Version:        0.1.0
Release:        1%{?dist}
Summary:        Painless string scanning
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unscanny
Source0:        https://static.crates.io/crates/unscanny/unscanny-%{version}.crate
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
Summary:        Painless string scanning
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
%files -n rust-unscanny-devel -f %{oreon_filedir}/rust-unscanny-devel.list

%changelog

%autochangelog
