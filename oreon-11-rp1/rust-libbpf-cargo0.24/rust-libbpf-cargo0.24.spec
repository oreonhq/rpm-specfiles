%global source0_hash 704727a07f185a76c58faa7b8ed08fba3194661c212183aea1174fe2970ee185
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate libbpf-cargo
Name:           rust-libbpf-cargo0.24
Version:        0.24.8
Release:        1%{?dist}
Summary:        Cargo plugin to build bpf programs
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://crates.io/crates/libbpf-cargo
Source0:        https://static.crates.io/crates/libbpf-cargo/libbpf-cargo-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  rustc
BuildRequires:  rustfmt
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang
Requires:       rustfmt
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cargo plugin to build bpf programs
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
%files -n rust-libbpf-cargo0.24-devel -f %{oreon_filedir}/rust-libbpf-cargo0.24-devel.list

%changelog

%autochangelog
