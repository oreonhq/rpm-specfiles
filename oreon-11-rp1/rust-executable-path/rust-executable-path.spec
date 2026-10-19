%global source0_hash ed24d6e921ad38aab6fd62771e8efb75ace61383312a663bcfcf268033d15d8b
%bcond check 1
%global debug_package %{nil}
%global crate executable-path
Name:           rust-executable-path
Version:        1.0.1
Release:        1%{?dist}
Summary:        Get the path of a binary target's executable
License:        CC0-1.0
URL:            https://crates.io/crates/executable-path
Source0:        https://static.crates.io/crates/executable-path/executable-path-%{version}.crate
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
Summary:        Get the path of a binary target's executable
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
%files -n rust-executable-path-devel -f %{oreon_filedir}/rust-executable-path-devel.list

%changelog

%autochangelog
