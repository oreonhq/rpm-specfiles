%global source0_hash 5fda04ab3764e6cde78b9974eec4f779acaba7c4e84b36eca3cf77c581b85d27
%bcond check 0
%global debug_package %{nil}
%global crate lzma-sys
Name:           rust-lzma-sys
Version:        0.1.20
Release:        1%{?dist}
Summary:        Raw bindings to liblzma which contains an implementation of LZMA and...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lzma-sys
Source0:        https://static.crates.io/crates/lzma-sys/lzma-sys-%{version}.crate
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

%package     -n %{name}+static-devel
Summary:        Raw bindings to liblzma which contains an implementation of LZMA and...
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

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
%files -n rust-lzma-sys-devel -f %{oreon_filedir}/rust-lzma-sys-devel.list

%changelog

%autochangelog
