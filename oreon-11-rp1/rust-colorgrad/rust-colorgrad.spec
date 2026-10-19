%global source0_hash aee94de557db6ddae3ca7b37b5fbe77ed6f159219f1815a8c2c1a9854c73087e
%bcond check 1
%global debug_package %{nil}
%global crate colorgrad
Name:           rust-colorgrad
Version:        0.8.0
Release:        1%{?dist}
Summary:        Color scales library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/colorgrad
Source0:        https://static.crates.io/crates/colorgrad/colorgrad-%{version}.crate
Patch:          colorgrad-fix-metadata.diff
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
Summary:        Color scales library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ggr-devel
Summary:        Color scales library
BuildArch:      noarch
%description -n %{name}+ggr-devel

This package contains library source intended for building other packages which
use the "ggr" feature of the "%{crate}" crate.

%package     -n %{name}+lab-devel
Summary:        Color scales library
BuildArch:      noarch
%description -n %{name}+lab-devel

This package contains library source intended for building other packages which
use the "lab" feature of the "%{crate}" crate.

%package     -n %{name}+named-colors-devel
Summary:        Color scales library
BuildArch:      noarch
%description -n %{name}+named-colors-devel

This package contains library source intended for building other packages which
use the "named-colors" feature of the "%{crate}" crate.

%package     -n %{name}+preset-devel
Summary:        Color scales library
BuildArch:      noarch
%description -n %{name}+preset-devel

This package contains library source intended for building other packages which
use the "preset" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Color scales library
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
%files -n rust-colorgrad-devel -f %{oreon_filedir}/rust-colorgrad-devel.list

%changelog

%autochangelog
