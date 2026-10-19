%global source0_hash 9ce1fc6db65a611022b23a0dec6975d63fb80a302cb3388835ff02c097258d50
%bcond check 0
%global debug_package %{nil}
%global crate serde_plain
Name:           rust-serde_plain
Version:        1.0.2
Release:        1%{?dist}
Summary:        Restricted plain text serializer for serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_plain
Source0:        https://static.crates.io/crates/serde_plain/serde_plain-%{version}.crate
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
Summary:        Restricted plain text serializer for serde
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
%files -n rust-serde_plain-devel -f %{oreon_filedir}/rust-serde_plain-devel.list

%changelog

%autochangelog
