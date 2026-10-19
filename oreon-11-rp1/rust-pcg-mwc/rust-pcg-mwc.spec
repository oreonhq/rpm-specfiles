%global source2_hash 0444c6991eead6822f7b9102e654448d51624431119546492e8b231db42c48bb
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash 2216858633c58b11bee47f9c8e9ff520bef76074d8ca893ac3f1a0d1d1bfcc7c
%bcond check 0
%global debug_package %{nil}
%global crate pcg-mwc
Name:           rust-pcg-mwc
Version:        0.2.1
Release:        1%{?dist}
Summary:        Fast non-cryptographic psudo random number generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pcg-mwc
Source0:        https://static.crates.io/crates/pcg-mwc/pcg-mwc-%{version}.crate
Source1:        https://raw.githubusercontent.com/tkaitchuck/Mwc256XXA64/f668e18bdb055c6ae2c3ca74ff587732ff64532c/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/tkaitchuck/Mwc256XXA64/f668e18bdb055c6ae2c3ca74ff587732ff64532c/LICENSE-MIT
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
Summary:        Fast non-cryptographic psudo random number generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Fast non-cryptographic psudo random number generator
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Fast non-cryptographic psudo random number generator
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-pcg-mwc-devel -f %{oreon_filedir}/rust-pcg-mwc-devel.list

%changelog

%autochangelog
