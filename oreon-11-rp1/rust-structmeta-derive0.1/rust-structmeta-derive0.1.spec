%global source0_hash 24420be405b590e2d746d83b01f09af673270cf80e9b003a5fa7b651c58c7d93
%bcond check 0
%global debug_package %{nil}
%global crate structmeta-derive
Name:           rust-structmeta-derive0.1
Version:        0.1.6
Release:        1%{?dist}
Summary:        derive macro for structmeta crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/structmeta-derive
Source0:        https://static.crates.io/crates/structmeta-derive/structmeta-derive-%{version}.crate
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
Summary:        derive macro for structmeta crate.
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
%files -n rust-structmeta-derive0.1-devel -f %{oreon_filedir}/rust-structmeta-derive0.1-devel.list

%changelog

%autochangelog
