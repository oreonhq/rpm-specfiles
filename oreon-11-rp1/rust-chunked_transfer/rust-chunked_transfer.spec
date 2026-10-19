%global source0_hash 6e4de3bc4ea267985becf712dc6d9eed8b04c953b3fcfb339ebc87acd9804901
%bcond check 0
%global debug_package %{nil}
%global crate chunked_transfer
Name:           rust-chunked_transfer
Version:        1.5.0
Release:        1%{?dist}
Summary:        Encoder and decoder for HTTP chunked transfer coding (RFC 7230 § 4.1)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chunked_transfer
Source0:        https://static.crates.io/crates/chunked_transfer/chunked_transfer-%{version}.crate
Patch:          chunked_transfer-fix-metadata.diff
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
Summary:        Encoder and decoder for HTTP chunked transfer coding (RFC 7230 § 4.1)
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
%files -n rust-chunked_transfer-devel -f %{oreon_filedir}/rust-chunked_transfer-devel.list

%changelog

%autochangelog
