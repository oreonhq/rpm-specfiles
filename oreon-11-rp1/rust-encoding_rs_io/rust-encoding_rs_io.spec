%global source0_hash fba3fe847045ecff794b9c138293a80db914678c453ad63fbf0c6a9eb6e00b22
%bcond check 0
%global debug_package %{nil}
%global crate encoding_rs_io
Name:           rust-encoding_rs_io
Version:        0.1.8
Release:        1%{?dist}
Summary:        Streaming transcoding for encoding_rs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/encoding_rs_io
Source0:        https://static.crates.io/crates/encoding_rs_io/encoding_rs_io-%{version}.crate
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
Summary:        Streaming transcoding for encoding_rs
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
%files -n rust-encoding_rs_io-devel -f %{oreon_filedir}/rust-encoding_rs_io-devel.list

%changelog

%autochangelog
