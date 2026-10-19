%global source0_hash bfc23178584a12c7cd7266c77c9a187ebfff4fd761738d9c838203bb17020f1f
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_sha384sum
Name:           rust-uu_sha384sum
Version:        0.7.0
Release:        1%{?dist}
Summary:        sha384sum ~ (uutils) Print or check the SHA384 checksums
License:        MIT
URL:            https://crates.io/crates/uu_sha384sum
Source0:        https://static.crates.io/crates/uu_sha384sum/uu_sha384sum-%{version}.crate
Patch:          uu_sha384sum-fix-metadata.diff
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
Summary:        sha384sum ~ (uutils) Print or check the SHA384 checksums
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
%files -n rust-uu_sha384sum-devel -f %{oreon_filedir}/rust-uu_sha384sum-devel.list

%changelog

%autochangelog
