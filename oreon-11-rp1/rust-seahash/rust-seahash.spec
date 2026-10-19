%global source0_hash 1c107b6f4780854c8b126e228ea8869f4d7b71260f962fefb57b996b8959ba6b
%bcond check 0
%global debug_package %{nil}
%global crate seahash
Name:           rust-seahash
Version:        4.1.0
Release:        1%{?dist}
Summary:        A blazingly fast, portable hash function with proven statistical guar...
License:        MIT
URL:            https://crates.io/crates/seahash
Source0:        https://static.crates.io/crates/seahash/seahash-%{version}.crate
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
Summary:        A blazingly fast, portable hash function with proven statistical guar...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        A blazingly fast, portable hash function with proven statistical guar...
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

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
%files -n rust-seahash-devel -f %{oreon_filedir}/rust-seahash-devel.list

%changelog

%autochangelog
