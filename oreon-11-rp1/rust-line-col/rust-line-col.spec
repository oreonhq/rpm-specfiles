%global source0_hash 9e69cdf6b85b5c8dce514f694089a2cf8b1a702f6cd28607bcb3cf296c9778db
%bcond check 0
%global debug_package %{nil}
%global crate line-col
Name:           rust-line-col
Version:        0.2.1
Release:        1%{?dist}
Summary:        Convert string slice indices into line/column numbers
License:        MIT
URL:            https://crates.io/crates/line-col
Source0:        https://static.crates.io/crates/line-col/line-col-%{version}.crate
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
Summary:        Convert string slice indices into line/column numbers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+grapheme-clusters-devel
Summary:        Convert string slice indices into line/column numbers
BuildArch:      noarch
%description -n %{name}+grapheme-clusters-devel

This package contains library source intended for building other packages which
use the "grapheme-clusters" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segmentation-devel
Summary:        Convert string slice indices into line/column numbers
BuildArch:      noarch
%description -n %{name}+unicode-segmentation-devel

This package contains library source intended for building other packages which
use the "unicode-segmentation" feature of the "%{crate}" crate.

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
%files -n rust-line-col-devel -f %{oreon_filedir}/rust-line-col-devel.list

%changelog

%autochangelog
