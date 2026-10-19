%global source0_hash 1e91099d4268b0e11973f036e885d652fb0b21fedcf69738c627f94db6a44f42
%bcond check 0
%global debug_package %{nil}
%global crate path-slash
Name:           rust-path-slash
Version:        0.2.1
Release:        1%{?dist}
Summary:        Conversion to/from a file path from/to slash path
License:        MIT
URL:            https://crates.io/crates/path-slash
Source0:        https://static.crates.io/crates/path-slash/path-slash-%{version}.crate
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
Summary:        Conversion to/from a file path from/to slash path
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
%files -n rust-path-slash-devel -f %{oreon_filedir}/rust-path-slash-devel.list

%changelog

%autochangelog
