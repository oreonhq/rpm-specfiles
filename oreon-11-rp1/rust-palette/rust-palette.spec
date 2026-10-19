%global source0_hash ddeed8580d347d2abf3dcf06a5f0b3dc020258338526b277847cd4248a70fc64
%bcond check 0
%global debug_package %{nil}
%global crate palette
Name:           rust-palette
Version:        0.7.7
Release:        1%{?dist}
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/palette
Source0:        https://static.crates.io/crates/palette/palette-%{version}.crate
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
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+approx-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+approx-devel

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+find-crate-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+find-crate-devel

This package contains library source intended for building other packages which
use the "find-crate" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+named-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+named-devel

This package contains library source intended for building other packages which
use the "named" feature of the "%{crate}" crate.

%package     -n %{name}+named_from_str-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+named_from_str-devel

This package contains library source intended for building other packages which
use the "named_from_str" feature of the "%{crate}" crate.

%package     -n %{name}+phf-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+phf-devel

This package contains library source intended for building other packages which
use the "phf" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+random-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+random-devel

This package contains library source intended for building other packages which
use the "random" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serializing-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+serializing-devel

This package contains library source intended for building other packages which
use the "serializing" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+wide-devel
Summary:        Convert and manage colors with a focus on correctness, flexibility an...
BuildArch:      noarch
%description -n %{name}+wide-devel

This package contains library source intended for building other packages which
use the "wide" feature of the "%{crate}" crate.

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
%files -n rust-palette-devel -f %{oreon_filedir}/rust-palette-devel.list

%changelog

%autochangelog
