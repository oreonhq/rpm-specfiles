%global source0_hash f8a38289608bcc13010f8ef444a583b04c82cdf8932a90ade88321cbeb610df0
%bcond check 1
%global debug_package %{nil}
%global crate below-render
%global unsupported_arches %{ix86}
Name:           rust-below-render
Version:        0.9.0
Release:        1%{?dist}
Summary:        Render crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-render
Source0:        https://static.crates.io/crates/below-render/below-render-%{version}.crate
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
Summary:        Render crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-render-devel -f %{oreon_filedir}/rust-below-render-devel.list

%changelog

%autochangelog
