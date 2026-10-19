%global source0_hash f64083bd3a16a353d9d62335808e8e13d0552d2a2b83fdb084496192dcfa9fcd
%bcond check 1
%global debug_package %{nil}
%global crate pyo3-log
Name:           rust-pyo3-log
Version:        0.13.4
Release:        1%{?dist}
Summary:        Logging bridge from pyo3 native extension to python
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pyo3-log
Source0:        https://static.crates.io/crates/pyo3-log/pyo3-log-%{version}.crate
Patch:          pyo3-log-fix-metadata.diff
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
Summary:        Logging bridge from pyo3 native extension to python
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+kv-devel
Summary:        Logging bridge from pyo3 native extension to python
BuildArch:      noarch
%description -n %{name}+kv-devel

This package contains library source intended for building other packages which
use the "kv" feature of the "%{crate}" crate.

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
%files -n rust-pyo3-log-devel -f %{oreon_filedir}/rust-pyo3-log-devel.list

%changelog

%autochangelog
