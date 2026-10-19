%global source0_hash e4eba85ea1d0a966a983acd07deee566e67395d2d96b6fb39e62b5a833f1eb0b
%bcond check 0
%global debug_package %{nil}
%global crate glob
Name:           rust-glob
Version:        0.3.4
Release:        1%{?dist}
Summary:        Support for matching file paths against Unix shell style patterns
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/glob
Source0:        https://static.crates.io/crates/glob/glob-%{version}.crate
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
Summary:        Support for matching file paths against Unix shell style patterns
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
%files -n rust-glob-devel -f %{oreon_filedir}/rust-glob-devel.list

%changelog

%autochangelog
