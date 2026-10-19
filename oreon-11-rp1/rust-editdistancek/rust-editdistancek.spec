%global source0_hash 3e02df23d5b1c6f9e69fa603b890378123b93073df998a21e6e33b9db0a32613
%bcond check 1
%global debug_package %{nil}
%global crate editdistancek
Name:           rust-editdistancek
Version:        1.0.2
Release:        1%{?dist}
Summary:        Fast algorithm for computing edit distance
License:        MIT
URL:            https://crates.io/crates/editdistancek
Source0:        https://static.crates.io/crates/editdistancek/editdistancek-%{version}.crate
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
Summary:        Fast algorithm for computing edit distance
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
%files -n rust-editdistancek-devel -f %{oreon_filedir}/rust-editdistancek-devel.list

%changelog

%autochangelog
