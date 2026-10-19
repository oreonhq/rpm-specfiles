%global source0_hash 206fdffcfa2df7cbe15601ef46c813fce0965eb3286db6b56c583b814b51c81c
%bcond check 0
%global debug_package %{nil}
%global crate bytes
Name:           rust-bytes0.4
Version:        0.4.12
Release:        1%{?dist}
Summary:        Types and traits for working with bytes
License:        MIT
URL:            https://crates.io/crates/bytes
Source0:        https://static.crates.io/crates/bytes/bytes-%{version}.crate
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

%package     -n %{name}+either-devel
Summary:        Types and traits for working with bytes
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+i128-devel
Summary:        Types and traits for working with bytes
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Types and traits for working with bytes
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
%files -n rust-bytes0.4-devel -f %{oreon_filedir}/rust-bytes0.4-devel.list

%changelog

%autochangelog
