%global source0_hash e57fef6bc5981e38c2ce2d63bfa546861309f875b8a75f092d1d54ae2d64f266
%bcond check 0
%global debug_package %{nil}
%global crate phf_shared
Name:           rust-phf_shared0.13
Version:        0.13.1
Release:        1%{?dist}
Summary:        Support code shared by PHF libraries
License:        MIT
URL:            https://crates.io/crates/phf_shared
Source0:        https://static.crates.io/crates/phf_shared/phf_shared-%{version}.crate
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
Summary:        Support code shared by PHF libraries
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Support code shared by PHF libraries
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+uncased-devel
Summary:        Support code shared by PHF libraries
BuildArch:      noarch
%description -n %{name}+uncased-devel

This package contains library source intended for building other packages which
use the "uncased" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Support code shared by PHF libraries
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

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
%files -n rust-phf_shared0.13-devel -f %{oreon_filedir}/rust-phf_shared0.13-devel.list

%changelog

%autochangelog
