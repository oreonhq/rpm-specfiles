%global source0_hash 696183c9b5fe81a7715d074fd632e8bd46f4ccc0231a3ed7fc580a80de5f7083
%bcond check 0
%global debug_package %{nil}
%global crate olpc-cjson
Name:           rust-olpc-cjson
Version:        0.1.4
Release:        1%{?dist}
Summary:        Serde_json Formatter to serialize as OLPC-style canonical JSON
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/olpc-cjson
Source0:        https://static.crates.io/crates/olpc-cjson/olpc-cjson-%{version}.crate
Patch:          olpc-cjson-fix-metadata.diff
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
Summary:        Serde_json Formatter to serialize as OLPC-style canonical JSON
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
%files -n rust-olpc-cjson-devel -f %{oreon_filedir}/rust-olpc-cjson-devel.list

%changelog

%autochangelog
