%global source0_hash 6fe962d42e07c22aec2618191c3683412735b7e6dcd7bab2eec811ab4697c58e
%bcond check 0
%global debug_package %{nil}
%global crate cap-std-ext
Name:           rust-cap-std-ext
Version:        4.0.7
Release:        1%{?dist}
Summary:        Extension APIs for cap-std
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cap-std-ext
Source0:        https://static.crates.io/crates/cap-std-ext/cap-std-ext-%{version}.crate
Patch:          cap-std-ext-fix-metadata-auto.diff
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
Summary:        Extension APIs for cap-std
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fs_utf8-devel
Summary:        Extension APIs for cap-std
BuildArch:      noarch
%description -n %{name}+fs_utf8-devel

This package contains library source intended for building other packages which
use the "fs_utf8" feature of the "%{crate}" crate.

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
%files -n rust-cap-std-ext-devel -f %{oreon_filedir}/rust-cap-std-ext-devel.list

%changelog

%autochangelog
