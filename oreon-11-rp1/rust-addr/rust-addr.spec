%global source0_hash a93b8a41dbe230ad5087cc721f8d41611de654542180586b315d9f4cf6b72bef
%bcond check 1
%global debug_package %{nil}
%global crate addr
Name:           rust-addr
Version:        0.15.6
Release:        1%{?dist}
Summary:        Library for parsing domain names
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/addr
Source0:        https://static.crates.io/crates/addr/addr-%{version}.crate
Patch:          addr-fix-metadata.diff
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
Summary:        Library for parsing domain names
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+idna-devel
Summary:        Library for parsing domain names
BuildArch:      noarch
%description -n %{name}+idna-devel

This package contains library source intended for building other packages which
use the "idna" feature of the "%{crate}" crate.

%package     -n %{name}+psl-devel
Summary:        Library for parsing domain names
BuildArch:      noarch
%description -n %{name}+psl-devel

This package contains library source intended for building other packages which
use the "psl" feature of the "%{crate}" crate.

%package     -n %{name}+publicsuffix-devel
Summary:        Library for parsing domain names
BuildArch:      noarch
%description -n %{name}+publicsuffix-devel

This package contains library source intended for building other packages which
use the "publicsuffix" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for parsing domain names
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for parsing domain names
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
%files -n rust-addr-devel -f %{oreon_filedir}/rust-addr-devel.list

%changelog

%autochangelog
