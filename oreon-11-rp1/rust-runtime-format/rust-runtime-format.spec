%global source0_hash 09958d5b38bca768ede7928c767c89a08ba568144a7b61992aecae79b03c8c94
%bcond check 0
%global debug_package %{nil}
%global crate runtime-format
Name:           rust-runtime-format
Version:        0.1.3
Release:        1%{?dist}
Summary:        Rust library for formatting dynamic strings
License:        MIT
URL:            https://crates.io/crates/runtime-format
Source0:        https://static.crates.io/crates/runtime-format/runtime-format-%{version}.crate
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
Summary:        Rust library for formatting dynamic strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust library for formatting dynamic strings
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tinyvec-devel
Summary:        Rust library for formatting dynamic strings
BuildArch:      noarch
%description -n %{name}+tinyvec-devel

This package contains library source intended for building other packages which
use the "tinyvec" feature of the "%{crate}" crate.

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
%files -n rust-runtime-format-devel -f %{oreon_filedir}/rust-runtime-format-devel.list

%changelog

%autochangelog
