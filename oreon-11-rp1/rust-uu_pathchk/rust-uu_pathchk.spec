%global source0_hash be9bc47993de7229717a577c7c4fe1f3919d8acc6d1dd5cb216a8a7eeebb8222
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_pathchk
Name:           rust-uu_pathchk
Version:        0.12.0
Release:        1%{?dist}
Summary:        pathchk ~ (uutils) diagnose invalid or non-portable PATHNAME
License:        MIT
URL:            https://crates.io/crates/uu_pathchk
Source0:        https://static.crates.io/crates/uu_pathchk/uu_pathchk-%{version}.crate
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
Summary:        pathchk ~ (uutils) diagnose invalid or non-portable PATHNAME
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
%files -n rust-uu_pathchk-devel -f %{oreon_filedir}/rust-uu_pathchk-devel.list

%changelog

%autochangelog
