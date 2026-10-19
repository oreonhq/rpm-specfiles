%global source0_hash c6f5d3c3b1bf09027a88a6bc961fc00497d651009560b5463668dc81b0fa87a8
%bcond check 0
%global debug_package %{nil}
%global crate unicode-segmentation
Name:           rust-unicode-segmentation
Version:        1.13.3
Release:        1%{?dist}
Summary:        Grapheme Cluster, Word and Sentence boundaries
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-segmentation
Source0:        https://static.crates.io/crates/unicode-segmentation/unicode-segmentation-%{version}.crate
Patch:          unicode-segmentation-fix-metadata.diff
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
Summary:        Grapheme Cluster, Word and Sentence boundaries
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Grapheme Cluster, Word and Sentence boundaries
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

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
%files -n rust-unicode-segmentation-devel -f %{oreon_filedir}/rust-unicode-segmentation-devel.list

%changelog

%autochangelog
