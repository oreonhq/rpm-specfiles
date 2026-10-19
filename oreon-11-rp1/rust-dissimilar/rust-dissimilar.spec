%global source0_hash aeda16ab4059c5fd2a83f2b9c9e9c981327b18aa8e3b313f7e6563799d4f093e
%bcond check 1
%global debug_package %{nil}
%global crate dissimilar
Name:           rust-dissimilar
Version:        1.0.11
Release:        1%{?dist}
Summary:        Diff library with semantic cleanup, based on Google's diff-match-patch
License:        Apache-2.0
URL:            https://crates.io/crates/dissimilar
Source0:        https://static.crates.io/crates/dissimilar/dissimilar-%{version}.crate
Patch:          dissimilar-fix-metadata.diff
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
Summary:        Diff library with semantic cleanup, based on Google's diff-match-patch
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
%files -n rust-dissimilar-devel -f %{oreon_filedir}/rust-dissimilar-devel.list

%changelog

%autochangelog
