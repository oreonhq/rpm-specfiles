%global source0_hash 3a0219bd7d979d58245a4f41f695e1ac9f8befdffadd7f61f1bae9e39abc6620
%bcond check 0
%global debug_package %{nil}
%global crate sponge-cursor
Name:           rust-sponge-cursor
Version:        0.1.0
Release:        1%{?dist}
Summary:        Cursor for sponge-based absorption and squeezing
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sponge-cursor
Source0:        https://static.crates.io/crates/sponge-cursor/sponge-cursor-%{version}.crate
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

%package     -n %{name}+zeroize-devel
Summary:        Cursor for sponge-based absorption and squeezing
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-sponge-cursor-devel -f %{oreon_filedir}/rust-sponge-cursor-devel.list

%changelog

%autochangelog
