%global source0_hash 4910941b420c3a31aa11a4eec7859b513fd6697ca59d2175b1b583c882b20b6b
%bcond check 0
%global debug_package %{nil}
%global crate crc-any
Name:           rust-crc-any
Version:        3.0.1
Release:        1%{?dist}
Summary:        Compute CRC values
License:        MIT
URL:            https://crates.io/crates/crc-any
Source0:        https://static.crates.io/crates/crc-any/crc-any-%{version}.crate
Patch:          crc-any-fix-metadata.diff
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
Summary:        Compute CRC values
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Compute CRC values
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+development-devel
Summary:        Compute CRC values
BuildArch:      noarch
%description -n %{name}+development-devel

This package contains library source intended for building other packages which
use the "development" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Compute CRC values
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Compute CRC values
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
%files -n rust-crc-any-devel -f %{oreon_filedir}/rust-crc-any-devel.list

%changelog

%autochangelog
