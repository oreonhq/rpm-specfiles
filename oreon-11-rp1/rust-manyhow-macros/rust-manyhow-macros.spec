%global source0_hash 46fce34d199b78b6e6073abf984c9cf5fd3e9330145a93ee0738a7443e371495
%bcond check 1
%global debug_package %{nil}
%global crate manyhow-macros
Name:           rust-manyhow-macros
Version:        0.11.4
Release:        1%{?dist}
Summary:        Macro for manyhow
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/manyhow-macros
Source0:        https://static.crates.io/crates/manyhow-macros/manyhow-macros-%{version}.crate
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
Summary:        Macro for manyhow
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
%files -n rust-manyhow-macros-devel -f %{oreon_filedir}/rust-manyhow-macros-devel.list

%changelog

%autochangelog
