%global source0_hash fad23fae12b089423cfa27a66e1ecb57d36a898bbd17f6cf8248ba1c0450835c
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_env
Name:           rust-uu_env
Version:        0.7.0
Release:        1%{?dist}
Summary:        env ~ (uutils) set each NAME to VALUE in the environment and run COMMAND
License:        MIT
URL:            https://crates.io/crates/uu_env
Source0:        https://static.crates.io/crates/uu_env/uu_env-%{version}.crate
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
Summary:        env ~ (uutils) set each NAME to VALUE in the environment and run COMMAND
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

%cargo_test -- -- --exact --skip tests::test_error_cases
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-uu_env-devel -f %{oreon_filedir}/rust-uu_env-devel.list

%changelog

%autochangelog
