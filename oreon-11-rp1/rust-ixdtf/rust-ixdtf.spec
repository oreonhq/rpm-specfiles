%global source0_hash 84de9d95a6d2547d9b77ee3f25fa0ee32e3c3a6484d47a55adebc0439c077992
%bcond check 1
%global debug_package %{nil}
%global crate ixdtf
Name:           rust-ixdtf
Version:        0.6.4
Release:        1%{?dist}
Summary:        Parser for Internet eXtended DateTime Format
License:        Unicode-3.0
URL:            https://crates.io/crates/ixdtf
Source0:        https://static.crates.io/crates/ixdtf/ixdtf-%{version}.crate
Patch:          ixdtf-fix-metadata.diff
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
Summary:        Parser for Internet eXtended DateTime Format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+duration-devel
Summary:        Parser for Internet eXtended DateTime Format
BuildArch:      noarch
%description -n %{name}+duration-devel

This package contains library source intended for building other packages which
use the "duration" feature of the "%{crate}" crate.

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
%files -n rust-ixdtf-devel -f %{oreon_filedir}/rust-ixdtf-devel.list

%changelog

%autochangelog
