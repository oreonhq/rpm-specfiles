%global source0_hash 0144c58b55af0133ec3963ce5e4d07aad866e3bbcfdcddbf4590dbd7ad6ff557
%bcond check 1
%global debug_package %{nil}
%global crate argmax
Name:           rust-argmax
Version:        0.4.0
Release:        1%{?dist}
Summary:        Rust library to deal with 'argument too long' errors
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/argmax
Source0:        https://static.crates.io/crates/argmax/argmax-%{version}.crate
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
Summary:        Rust library to deal with 'argument too long' errors
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
%files -n rust-argmax-devel -f %{oreon_filedir}/rust-argmax-devel.list

%changelog

%autochangelog
