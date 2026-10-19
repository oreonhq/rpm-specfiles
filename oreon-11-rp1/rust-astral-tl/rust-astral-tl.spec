%global source0_hash d90933ffb0f97e2fc2e0de21da9d3f20597b804012d199843a6fe7c2810d28f3
%bcond check 1
%global debug_package %{nil}
%global crate astral-tl
Name:           rust-astral-tl
Version:        0.7.11
Release:        1%{?dist}
Summary:        Fast HTML parser written in pure Rust
License:        MIT
URL:            https://crates.io/crates/astral-tl
Source0:        https://static.crates.io/crates/astral-tl/astral-tl-%{version}.crate
Patch:          astral-tl-fix-metadata.diff
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
Summary:        Fast HTML parser written in pure Rust
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
%files -n rust-astral-tl-devel -f %{oreon_filedir}/rust-astral-tl-devel.list

%changelog

%autochangelog
