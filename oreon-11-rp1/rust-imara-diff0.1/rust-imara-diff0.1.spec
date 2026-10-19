%global source0_hash 17d34b7d42178945f775e84bc4c36dde7c1c6cdfea656d3354d009056f2bb3d2
%bcond check 0
%global debug_package %{nil}
%global crate imara-diff
Name:           rust-imara-diff0.1
Version:        0.1.8
Release:        1%{?dist}
Summary:        High performance library for computing diffs
License:        Apache-2.0
URL:            https://crates.io/crates/imara-diff
Source0:        https://static.crates.io/crates/imara-diff/imara-diff-%{version}.crate
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
Summary:        High performance library for computing diffs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unified_diff-devel
Summary:        High performance library for computing diffs
BuildArch:      noarch
%description -n %{name}+unified_diff-devel

This package contains library source intended for building other packages which
use the "unified_diff" feature of the "%{crate}" crate.

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
%files -n rust-imara-diff0.1-devel -f %{oreon_filedir}/rust-imara-diff0.1-devel.list

%changelog

%autochangelog
