%global source0_hash cf5a574dadd7941adeaa71823ecba5e28331b8313fb2e1c6a5c7e5981ea53ad6
%bcond check 1
%global debug_package %{nil}
%global crate never-say-never
Name:           rust-never-say-never
Version:        6.6.666
Release:        1%{?dist}
Summary:        Never type (the true one!) in stable Rust
License:        Zlib OR MIT OR Apache-2.0
URL:            https://crates.io/crates/never-say-never
Source0:        https://static.crates.io/crates/never-say-never/never-say-never-%{version}.crate
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
Summary:        Never type (the true one!) in stable Rust
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
%files -n rust-never-say-never-devel -f %{oreon_filedir}/rust-never-say-never-devel.list

%changelog

%autochangelog
