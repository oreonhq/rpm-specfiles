%global source0_hash 1df593470e3ef502e48cb0cfc9a3a61e5f61e967b78e1ed35a67ac615cfbd208
%bcond check 0
%global debug_package %{nil}
%global crate print-positions
Name:           rust-print-positions
Version:        0.6.1
Release:        1%{?dist}
Summary:        String segmentation library for grapheme clusters and ANSI escape sequences
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/print-positions
Source0:        https://static.crates.io/crates/print-positions/print-positions-%{version}.crate
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
Summary:        String segmentation library for grapheme clusters and ANSI escape sequences
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
%files -n rust-print-positions-devel -f %{oreon_filedir}/rust-print-positions-devel.list

%changelog

%autochangelog
