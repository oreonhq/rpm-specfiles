%global source0_hash 43f613e4fa046e69818dd287fdc4bc78175ff20331479dab6e1b0f98d57062de
%bcond check 1
%global debug_package %{nil}
%global crate unicode-normalization-alignments
Name:           rust-unicode-normalization-alignments
Version:        0.1.12
Release:        1%{?dist}
Summary:        Unicode character composition and decomposition utilities with alignment
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-normalization-alignments
Source0:        https://static.crates.io/crates/unicode-normalization-alignments/unicode-normalization-alignments-%{version}.crate
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
Summary:        Unicode character composition and decomposition utilities with alignment
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r scripts/
rm -r benches/
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
%files -n rust-unicode-normalization-alignments-devel -f %{oreon_filedir}/rust-unicode-normalization-alignments-devel.list

%changelog

%autochangelog
