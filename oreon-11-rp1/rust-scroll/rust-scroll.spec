%global source0_hash c1257cd4248b4132760d6524d6dda4e053bc648c9070b960929bf50cfb1e7add
%bcond check 1
%global debug_package %{nil}
%global crate scroll
Name:           rust-scroll
Version:        0.13.0
Release:        1%{?dist}
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
License:        MIT
URL:            https://crates.io/crates/scroll
Source0:        https://static.crates.io/crates/scroll/scroll-%{version}.crate
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
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-scroll-devel -f %{oreon_filedir}/rust-scroll-devel.list

%changelog

%autochangelog
