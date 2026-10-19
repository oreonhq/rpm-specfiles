%global source0_hash 0bc85448a6006dd2ba26a385a564a8a0f1f2c7e78c70f1a70b2e0f4af286b823
%bcond check 0
%global debug_package %{nil}
%global crate mmap
Name:           rust-mmap
Version:        0.1.1
Release:        1%{?dist}
Summary:        A library for dealing with memory-mapped I/O
License:        MIT
URL:            https://crates.io/crates/mmap
Source0:        https://static.crates.io/crates/mmap/mmap-%{version}.crate
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
Summary:        A library for dealing with memory-mapped I/O
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
%files -n rust-mmap-devel -f %{oreon_filedir}/rust-mmap-devel.list

%changelog

%autochangelog
