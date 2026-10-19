%global source0_hash bbaa233e1dcd9c13a5d3e3a8a2c0f5a727bac380398345dbcb31db4597edc86b
%bcond check 1
%global debug_package %{nil}
%global crate cssparser-color
Name:           rust-cssparser-color0.5
Version:        0.5.0
Release:        1%{?dist}
Summary:        Color implementation based on cssparser
License:        MPL-2.0
URL:            https://crates.io/crates/cssparser-color
Source0:        https://static.crates.io/crates/cssparser-color/cssparser-color-%{version}.crate
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
Summary:        Color implementation based on cssparser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Color implementation based on cssparser
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-cssparser-color0.5-devel -f %{oreon_filedir}/rust-cssparser-color0.5-devel.list

%changelog

%autochangelog
