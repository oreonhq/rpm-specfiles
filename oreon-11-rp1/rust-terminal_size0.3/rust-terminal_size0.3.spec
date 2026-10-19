%global source0_hash 21bebf2b7c9e0a515f6e0f8c51dc0f8e4696391e6f1ff30379559f8365fb0df7
%bcond check 0
%global debug_package %{nil}
%global crate terminal_size
Name:           rust-terminal_size0.3
Version:        0.3.0
Release:        1%{?dist}
Summary:        Gets the size of your Linux or Windows terminal
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/terminal_size
Source0:        https://static.crates.io/crates/terminal_size/terminal_size-%{version}.crate
Patch:          terminal_size-fix-metadata-auto.diff
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
Summary:        Gets the size of your Linux or Windows terminal
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

%cargo_test -- -- --skip unix::compare_with_stty
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-terminal_size0.3-devel -f %{oreon_filedir}/rust-terminal_size0.3-devel.list

%changelog

%autochangelog
