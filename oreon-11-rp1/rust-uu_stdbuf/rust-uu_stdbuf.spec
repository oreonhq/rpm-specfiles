%global source0_hash 9a0d6846f7cd7d65b10fbac3214721ef0bbf71e1860a4bf28124da2b118bb7d0
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_stdbuf
Name:           rust-uu_stdbuf
Version:        0.7.0
Release:        1%{?dist}
Summary:        stdbuf ~ (uutils) run COMMAND with modified standard stream buffering
License:        MIT
URL:            https://crates.io/crates/uu_stdbuf
Source0:        https://static.crates.io/crates/uu_stdbuf/uu_stdbuf-%{version}.crate
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
Summary:        stdbuf ~ (uutils) run COMMAND with modified standard stream buffering
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+feat_external_libstdbuf-devel
Summary:        stdbuf ~ (uutils) run COMMAND with modified standard stream buffering
BuildArch:      noarch
%description -n %{name}+feat_external_libstdbuf-devel

This package contains library source intended for building other packages which
use the "feat_external_libstdbuf" feature of the "%{crate}" crate.

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
%files -n rust-uu_stdbuf-devel -f %{oreon_filedir}/rust-uu_stdbuf-devel.list

%changelog

%autochangelog
