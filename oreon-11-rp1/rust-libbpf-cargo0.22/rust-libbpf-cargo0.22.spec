%global source0_hash 9a58dfb8194a9b8ff960890a8d71e905b4635aa89c3dad4ce6c1a99c2eec759f
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate libbpf-cargo
Name:           rust-libbpf-cargo0.22
Version:        0.22.1
Release:        1%{?dist}
Summary:        Cargo plugin to build bpf programs
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://crates.io/crates/libbpf-cargo
Source0:        https://static.crates.io/crates/libbpf-cargo/libbpf-cargo-%{version}.crate
Patch:          libbpf-cargo-fix-finding-libbpf-rs.diff
Patch:          libbpf-cargo-fix-metadata.diff
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

%package     -n %{name}+novendor-devel
Summary:        Cargo plugin to build bpf programs
BuildArch:      noarch
%description -n %{name}+novendor-devel

This package contains library source intended for building other packages which
use the "novendor" feature of the "%{crate}" crate.

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
%files -n rust-libbpf-cargo0.22-devel -f %{oreon_filedir}/rust-libbpf-cargo0.22-devel.list

%changelog

%autochangelog
