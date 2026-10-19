%global source0_hash 7d88f747710a968a0a32ce4c4ae90ead21dc36a06aceabbb4367452679a95eb6
%bcond_without check
%global debug_package %{nil}
%global crate exhaustigen
Name:           rust-exhaustigen
Version:        0.1.0
Release:        1%{?dist}
Summary:        Exhaustive test generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/exhaustigen
Source0:        https://static.crates.io/crates/exhaustigen/exhaustigen-%{version}.crate
Patch:          https://github.com/graydon/exhaustigen-rs/pull/1.patch
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
Summary:        Exhaustive test generator
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
%files -n rust-exhaustigen-devel -f %{oreon_filedir}/rust-exhaustigen-devel.list

%changelog

%autochangelog
