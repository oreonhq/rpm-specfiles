%global source0_hash 225bff33b2141874fe80d71e07d6eec4f85c5c216453dd96388240f96e1acc14
%bcond check 0
%global debug_package %{nil}
%global crate bzip2-sys
%global crate_version 0.1.13+1.0.8
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-bzip2-sys
Version:        0.1.13
Release:        1%{?dist}
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bzip2-sys
Source0:        https://static.crates.io/crates/bzip2-sys/bzip2-sys-%{version}.crate
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

%package     -n %{name}+__disabled-devel
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as
BuildArch:      noarch
%description -n %{name}+__disabled-devel

This package contains library source intended for building other packages which
use the "__disabled" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-bzip2-sys-devel -f %{oreon_filedir}/rust-bzip2-sys-devel.list

%changelog

%autochangelog
