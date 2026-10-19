%global source0_hash fe5c30ade05e61656247b2e334a031dfd0cc466fadef865bdcdea8d537951bf1
%bcond check 0
%global debug_package %{nil}
%global crate yansi-term
Name:           rust-yansi-term
Version:        0.1.2
Release:        1%{?dist}
Summary:        Library for ANSI terminal colours and styles (bold, underline)
License:        MIT
URL:            https://crates.io/crates/yansi-term
Source0:        https://static.crates.io/crates/yansi-term/yansi-term-%{version}.crate
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

%package     -n %{name}+derive_serde_style-devel
Summary:        Library for ANSI terminal colours and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+derive_serde_style-devel

This package contains library source intended for building other packages which
use the "derive_serde_style" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for ANSI terminal colours and styles (bold, underline)
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-yansi-term-devel -f %{oreon_filedir}/rust-yansi-term-devel.list

%changelog

%autochangelog
