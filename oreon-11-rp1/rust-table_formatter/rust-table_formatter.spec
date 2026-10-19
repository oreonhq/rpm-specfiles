%global source0_hash beef5d3fd5472c911d41286849de6a9aee93327f7fae9fb9148fe9ff0102c17d
%bcond check 1
%global debug_package %{nil}
%global crate table_formatter
Name:           rust-table_formatter
Version:        0.6.1
Release:        1%{?dist}
Summary:        Simple text table formatter written in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/table_formatter
Source0:        https://static.crates.io/crates/table_formatter/table_formatter-%{version}.crate
Patch:          table_formatter-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Simple text table formatter written in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f | xargs -r -t dos2unix --keepdate
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
%files -n rust-table_formatter-devel -f %{oreon_filedir}/rust-table_formatter-devel.list

%changelog

%autochangelog
