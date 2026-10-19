%global source0_hash 0bf760ebf69878d9fd8f110c89703d90ce35095324d1f1edcb595c63945ee757
%bcond check 0
%global debug_package %{nil}
%global crate globwalk
Name:           rust-globwalk
Version:        0.9.1
Release:        1%{?dist}
Summary:        Glob-matched recursive file system walking.
License:        MIT
URL:            https://crates.io/crates/globwalk
Source0:        https://static.crates.io/crates/globwalk/globwalk-%{version}.crate
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
Summary:        Glob-matched recursive file system walking.
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
%files -n rust-globwalk-devel -f %{oreon_filedir}/rust-globwalk-devel.list

%changelog

%autochangelog
