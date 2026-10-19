%global source0_hash c711928715f1fe0fe509c53b43e993a9a557babc2d0a3567d0a3006f1ac931a0
%bcond check 1
%global debug_package %{nil}
%global crate string_cache_codegen
Name:           rust-string_cache_codegen
Version:        0.5.4
Release:        1%{?dist}
Summary:        Codegen library for string-cache, developed as part of the Servo project
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/string_cache_codegen
Source0:        https://static.crates.io/crates/string_cache_codegen/string_cache_codegen-%{version}.crate
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
Summary:        Codegen library for string-cache, developed as part of the Servo project
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
%files -n rust-string_cache_codegen-devel -f %{oreon_filedir}/rust-string_cache_codegen-devel.list

%changelog

%autochangelog
