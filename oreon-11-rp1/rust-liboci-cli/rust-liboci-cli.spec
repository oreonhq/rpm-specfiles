%global source0_hash 03af901723a58d7b4ddf8faffe1dbd386dde949d51fe40e2d918c32e23be4d2f
%bcond check 0
%global debug_package %{nil}
%global crate liboci-cli
Name:           rust-liboci-cli
Version:        0.3.3
Release:        1%{?dist}
Summary:        Parse command line arguments for OCI container runtimes
License:        Apache-2.0
URL:            https://crates.io/crates/liboci-cli
Source0:        https://static.crates.io/crates/liboci-cli/liboci-cli-%{version}.crate
Patch:          liboci-cli-fix-metadata.diff
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
Summary:        Parse command line arguments for OCI container runtimes
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
%files -n rust-liboci-cli-devel -f %{oreon_filedir}/rust-liboci-cli-devel.list

%changelog

%autochangelog
