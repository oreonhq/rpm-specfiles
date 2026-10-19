%global source0_hash 16f5094c54661b38d03bd7e50df373292118db60b585c08a411c6d840017fe7d
%bcond check 0
%global debug_package %{nil}
%global crate directories
Name:           rust-directories
Version:        6.0.0
Release:        1%{?dist}
Summary:        A tiny mid-level library that provides platform-specific standard loc...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/directories
Source0:        https://static.crates.io/crates/directories/directories-%{version}.crate
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
Summary:        A tiny mid-level library that provides platform-specific standard loc...
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
%files -n rust-directories-devel -f %{oreon_filedir}/rust-directories-devel.list

%changelog

%autochangelog
