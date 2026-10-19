%global source0_hash 051eb1abcf10076295e815102942cc58f9d5e3b4560e46e53c21e8ff6f3af7b1
%bcond check 0
%global debug_package %{nil}
%global crate virtue
Name:           rust-virtue0.0.18
Version:        0.0.18
Release:        1%{?dist}
Summary:        A sinless derive macro helper
License:        MIT
URL:            https://crates.io/crates/virtue
Source0:        https://static.crates.io/crates/virtue/virtue-%{version}.crate
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

%package     -n %{name}+proc-macro2-devel
Summary:        A sinless derive macro helper
BuildArch:      noarch
%description -n %{name}+proc-macro2-devel

This package contains library source intended for building other packages which
use the "proc-macro2" feature of the "%{crate}" crate.

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
%files -n rust-virtue0.0.18-devel -f %{oreon_filedir}/rust-virtue0.0.18-devel.list

%changelog

%autochangelog
