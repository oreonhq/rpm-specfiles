%global source0_hash 72f81bee8c8ef9b577d1681a70ebbc962c232461e397b22c208c43c04b67a155
%bcond check 1
%global debug_package %{nil}
%global crate rmp-serde
Name:           rust-rmp-serde
Version:        1.3.1
Release:        1%{?dist}
Summary:        Serde support for MessagePack
License:        MIT
URL:            https://crates.io/crates/rmp-serde
Source0:        https://static.crates.io/crates/rmp-serde/rmp-serde-%{version}.crate
Patch:          rmp-serde-fix-metadata.diff
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
Summary:        Serde support for MessagePack
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
%files -n rust-rmp-serde-devel -f %{oreon_filedir}/rust-rmp-serde-devel.list

%changelog

%autochangelog
