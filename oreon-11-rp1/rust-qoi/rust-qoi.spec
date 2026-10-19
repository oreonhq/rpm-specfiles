%global source0_hash 7f6d64c71eb498fe9eae14ce4ec935c555749aef511cca85b5568910d6e48001
%bcond check 0
%global debug_package %{nil}
%global crate qoi
Name:           rust-qoi
Version:        0.4.1
Release:        1%{?dist}
Summary:        VERY fast encoder/decoder for QOI (Quite Okay Image) format
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/qoi
Source0:        https://static.crates.io/crates/qoi/qoi-%{version}.crate
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
Summary:        VERY fast encoder/decoder for QOI (Quite Okay Image) format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        VERY fast encoder/decoder for QOI (Quite Okay Image) format
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+reference-devel
Summary:        VERY fast encoder/decoder for QOI (Quite Okay Image) format
BuildArch:      noarch
%description -n %{name}+reference-devel

This package contains library source intended for building other packages which
use the "reference" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        VERY fast encoder/decoder for QOI (Quite Okay Image) format
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
%files -n rust-qoi-devel -f %{oreon_filedir}/rust-qoi-devel.list

%changelog

%autochangelog
