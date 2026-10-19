%global source0_hash 3dcaa9ae7725d12cdb85b3ad99a434db70b468c09ded17e012d86b5c1010f7a7
%bcond check 0
%global debug_package %{nil}
%global crate fuchsia-zircon-sys
Name:           rust-fuchsia-zircon-sys
Version:        0.3.3
Release:        1%{?dist}
Summary:        Low-level Rust bindings for the Zircon kernel
License:        BSD-3-Clause
URL:            https://crates.io/crates/fuchsia-zircon-sys
Source0:        https://static.crates.io/crates/fuchsia-zircon-sys/fuchsia-zircon-sys-%{version}.crate
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
Summary:        Low-level Rust bindings for the Zircon kernel
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
%files -n rust-fuchsia-zircon-sys-devel -f %{oreon_filedir}/rust-fuchsia-zircon-sys-devel.list

%changelog

%autochangelog
