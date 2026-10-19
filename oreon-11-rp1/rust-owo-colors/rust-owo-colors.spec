%global source0_hash 13c45bb4a6ae1280ec0803b1ef9d3455eb50f01efbbe1447ab020f1d54fba9d8
%bcond check 0
%global debug_package %{nil}
%global crate owo-colors
Name:           rust-owo-colors
Version:        4.4.0
Release:        1%{?dist}
Summary:        Zero-allocation terminal colors that'll make people go owo
License:        MIT
URL:            https://crates.io/crates/owo-colors
Source0:        https://static.crates.io/crates/owo-colors/owo-colors-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Zero-allocation terminal colors that'll make people go owo
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+supports-colors-devel
Summary:        Zero-allocation terminal colors that'll make people go owo
BuildArch:      noarch
%description -n %{name}+supports-colors-devel

This package contains library source intended for building other packages which
use the "supports-colors" feature of the "%{crate}" crate.

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
%files -n rust-owo-colors-devel -f %{oreon_filedir}/rust-owo-colors-devel.list

%changelog

%autochangelog
