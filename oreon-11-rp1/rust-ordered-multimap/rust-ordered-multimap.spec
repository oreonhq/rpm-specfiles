%global source0_hash ccd746e37177e1711c20dd619a1620f34f5c8b569c53590a72dedd5344d8924a
%bcond check 0
%global debug_package %{nil}
%global crate ordered-multimap
Name:           rust-ordered-multimap
Version:        0.4.3
Release:        1%{?dist}
Summary:        Insertion ordered multimap
License:        MIT
URL:            https://crates.io/crates/ordered-multimap
Source0:        https://static.crates.io/crates/ordered-multimap/ordered-multimap-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        Insertion ordered multimap
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
%files -n rust-ordered-multimap-devel -f %{oreon_filedir}/rust-ordered-multimap-devel.list

%changelog

%autochangelog
