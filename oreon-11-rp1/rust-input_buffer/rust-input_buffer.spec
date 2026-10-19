%global source0_hash acee673b88a760f5d1f7b2677a90ab797878282ca36ebd0ed8d560361bee9810
%bcond check 0
%global debug_package %{nil}
%global crate input_buffer
Name:           rust-input_buffer
Version:        0.5.0
Release:        1%{?dist}
Summary:        Peekable FIFO-like buffer for receiving network data efficiently
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/input_buffer
Source0:        https://static.crates.io/crates/input_buffer/input_buffer-%{version}.crate
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
Summary:        Peekable FIFO-like buffer for receiving network data efficiently
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
%files -n rust-input_buffer-devel -f %{oreon_filedir}/rust-input_buffer-devel.list

%changelog

%autochangelog
