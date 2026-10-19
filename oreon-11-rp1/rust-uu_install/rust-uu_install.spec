%global source0_hash bb85e3e664799d5141bead58b55de3dd42e961744876ab1a27f6096a41bcdf78
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_install
Name:           rust-uu_install
Version:        0.7.0
Release:        1%{?dist}
Summary:        install - (uutils) copy files from SOURCE to DESTINATION
License:        MIT
URL:            https://crates.io/crates/uu_install
Source0:        https://static.crates.io/crates/uu_install/uu_install-%{version}.crate
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
Summary:        install - (uutils) copy files from SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        install - (uutils) copy files from SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

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
%files -n rust-uu_install-devel -f %{oreon_filedir}/rust-uu_install-devel.list

%changelog

%autochangelog
