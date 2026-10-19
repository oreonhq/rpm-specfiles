%global source0_hash 54fe27f8037c58cb4b6d60fe0aacf7ee2c998633cedf4e989351c07d9a3a575d
%bcond check 0
%global debug_package %{nil}
%global crate gix-blame
Name:           rust-gix-blame
Version:        0.17.1
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dedicated to implementing a 'blame' a...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-blame
Source0:        https://static.crates.io/crates/gix-blame/gix-blame-%{version}.crate
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

%package     -n %{name}+blob-experimental-devel
Summary:        A crate of the gitoxide project dedicated to implementing a 'blame' a...
BuildArch:      noarch
%description -n %{name}+blob-experimental-devel

This package contains library source intended for building other packages which
use the "blob-experimental" feature of the "%{crate}" crate.

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
%files -n rust-gix-blame-devel -f %{oreon_filedir}/rust-gix-blame-devel.list

%changelog

%autochangelog
