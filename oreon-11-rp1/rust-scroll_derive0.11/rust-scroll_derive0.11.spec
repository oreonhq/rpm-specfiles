%global source0_hash 1db149f81d46d2deba7cd3c50772474707729550221e69588478ebf9ada425ae
%bcond check 1
%global debug_package %{nil}
%global crate scroll_derive
Name:           rust-scroll_derive0.11
Version:        0.11.1
Release:        1%{?dist}
Summary:        Derive implementation for scroll::Pread and scroll::Pwrite traits
License:        MIT
URL:            https://crates.io/crates/scroll_derive
Source0:        https://static.crates.io/crates/scroll_derive/scroll_derive-%{version}.crate
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
Summary:        Derive implementation for scroll::Pread and scroll::Pwrite traits
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
%files -n rust-scroll_derive0.11-devel -f %{oreon_filedir}/rust-scroll_derive0.11-devel.list

%changelog

%autochangelog
