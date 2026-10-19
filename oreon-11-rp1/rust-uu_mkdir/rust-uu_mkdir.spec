%global source0_hash d8cdba0fed9c1c12d0a0c954e447cc75a50b466b001f1a814921ee702fafff7a
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_mkdir
Name:           rust-uu_mkdir
Version:        0.7.0
Release:        1%{?dist}
Summary:        mkdir ~ (uutils) create DIRECTORY
License:        MIT
URL:            https://crates.io/crates/uu_mkdir
Source0:        https://static.crates.io/crates/uu_mkdir/uu_mkdir-%{version}.crate
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
Summary:        mkdir ~ (uutils) create DIRECTORY
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        mkdir ~ (uutils) create DIRECTORY
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%package     -n %{name}+smack-devel
Summary:        mkdir ~ (uutils) create DIRECTORY
BuildArch:      noarch
%description -n %{name}+smack-devel

This package contains library source intended for building other packages which
use the "smack" feature of the "%{crate}" crate.

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
%files -n rust-uu_mkdir-devel -f %{oreon_filedir}/rust-uu_mkdir-devel.list

%changelog

%autochangelog
