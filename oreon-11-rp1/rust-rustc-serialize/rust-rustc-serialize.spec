%global source0_hash fe834bc780604f4674073badbad26d7219cadfb4a2275802db12cbae17498401
%bcond check 0
%global debug_package %{nil}
%global crate rustc-serialize
Name:           rust-rustc-serialize
Version:        0.3.25
Release:        1%{?dist}
Summary:        Generic serialization/deserialization support corresponding to the
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-serialize
Source0:        https://static.crates.io/crates/rustc-serialize/rustc-serialize-%{version}.crate
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
Summary:        Generic serialization/deserialization support corresponding to the
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
%files -n rust-rustc-serialize-devel -f %{oreon_filedir}/rust-rustc-serialize-devel.list

%changelog

%autochangelog
