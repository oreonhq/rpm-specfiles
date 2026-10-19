%global source0_hash 7d8fae84b431384b68627d0f9b3b1245fcf9f46f6c0e3dc902e9dce64edd1967
%bcond check 1
%global debug_package %{nil}
%global crate os_pipe
Name:           rust-os_pipe
Version:        1.2.3
Release:        1%{?dist}
Summary:        a cross-platform library for opening OS pipes
License:        MIT
URL:            https://crates.io/crates/os_pipe
Source0:        https://static.crates.io/crates/os_pipe/os_pipe-%{version}.crate
Patch:          os_pipe-fix-metadata-auto.diff
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
Summary:        a cross-platform library for opening OS pipes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+io_safety-devel
Summary:        a cross-platform library for opening OS pipes
BuildArch:      noarch
%description -n %{name}+io_safety-devel

This package contains library source intended for building other packages which
use the "io_safety" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
rm -f %{buildroot}%{_bindir}/cat
rm -f %{buildroot}%{_bindir}/cat_both
rm -f %{buildroot}%{_bindir}/swap
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-os_pipe-devel -f %{oreon_filedir}/rust-os_pipe-devel.list

%changelog

%autochangelog
