%global source9_hash d201d14804d3bcd3b944147173175e4abfbd838b7c8069b6bd3452496bf13e6c
%global source8_hash d30047bca3b516639339a3c279bb84c3483124fb5a9dafe3c75056a85090e745
%global source7_hash c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
%global source0_hash 29ce2c8a9384ad323cf564b67da86e21d3cfdff87908bc1223ed5c99bc792713
%bcond check 1
%global debug_package %{nil}
%global crate zune-jpeg
Name:           rust-zune-jpeg0.4
Version:        0.4.21
Release:        1%{?dist}
Summary:        Fast, correct and safe jpeg decoder
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/zune-jpeg
Source0:        https://static.crates.io/crates/zune-jpeg/zune-jpeg-%{version}.crate
Source7:        https://github.com/etemesi254/zune-image/raw/24603fe/LICENSE-APACHE
Source8:        https://github.com/etemesi254/zune-image/raw/24603fe/LICENSE-MIT
Source9:        https://github.com/etemesi254/zune-image/raw/24603fe/LICENSE-ZLIB
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
Summary:        Fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+neon-devel
Summary:        Fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+neon-devel

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+x86-devel
Summary:        Fast, correct and safe jpeg decoder
BuildArch:      noarch
%description -n %{name}+x86-devel

This package contains library source intended for building other packages which
use the "x86" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE7} %{SOURCE8} %{SOURCE9} .
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
%files -n rust-zune-jpeg0.4-devel -f %{oreon_filedir}/rust-zune-jpeg0.4-devel.list

%changelog

%autochangelog
