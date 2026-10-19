%global source0_hash 167e064d8a4b20ef56d66ab231a9d2200d139cee1dfd3d7bd5f800d5cad2e978
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_mkfifo
Name:           rust-uu_mkfifo
Version:        0.12.0
Release:        1%{?dist}
Summary:        mkfifo ~ (uutils) create FIFOs (named pipes)
License:        MIT
URL:            https://crates.io/crates/uu_mkfifo
Source0:        https://static.crates.io/crates/uu_mkfifo/uu_mkfifo-%{version}.crate
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
Summary:        mkfifo ~ (uutils) create FIFOs (named pipes)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        mkfifo ~ (uutils) create FIFOs (named pipes)
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%package     -n %{name}+smack-devel
Summary:        mkfifo ~ (uutils) create FIFOs (named pipes)
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
%files -n rust-uu_mkfifo-devel -f %{oreon_filedir}/rust-uu_mkfifo-devel.list

%changelog

%autochangelog
