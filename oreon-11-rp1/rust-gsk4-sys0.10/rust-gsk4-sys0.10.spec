%global source0_hash 7ce91472391146f482065f1041876d8f869057b195b95399414caa163d72f4f7
%bcond check 0
%global debug_package %{nil}
%global crate gsk4-sys
Name:           rust-gsk4-sys0.10
Version:        0.10.3
Release:        1%{?dist}
Summary:        FFI bindings of GSK 4
License:        MIT
URL:            https://crates.io/crates/gsk4-sys
Source0:        https://static.crates.io/crates/gsk4-sys/gsk4-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.0.0
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+broadway-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
%description -n %{name}+broadway-devel

This package contains library source intended for building other packages which
use the "broadway" feature of the "%{crate}" crate.

%package     -n %{name}+v4_10-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.10
%description -n %{name}+v4_10-devel

This package contains library source intended for building other packages which
use the "v4_10" feature of the "%{crate}" crate.

%package     -n %{name}+v4_14-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.14
%description -n %{name}+v4_14-devel

This package contains library source intended for building other packages which
use the "v4_14" feature of the "%{crate}" crate.

%package     -n %{name}+v4_16-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.16
%description -n %{name}+v4_16-devel

This package contains library source intended for building other packages which
use the "v4_16" feature of the "%{crate}" crate.

%package     -n %{name}+v4_18-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.18
%description -n %{name}+v4_18-devel

This package contains library source intended for building other packages which
use the "v4_18" feature of the "%{crate}" crate.

%package     -n %{name}+v4_2-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.2
%description -n %{name}+v4_2-devel

This package contains library source intended for building other packages which
use the "v4_2" feature of the "%{crate}" crate.

%package     -n %{name}+v4_20-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.19
%description -n %{name}+v4_20-devel

This package contains library source intended for building other packages which
use the "v4_20" feature of the "%{crate}" crate.

%package     -n %{name}+v4_4-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.4
%description -n %{name}+v4_4-devel

This package contains library source intended for building other packages which
use the "v4_4" feature of the "%{crate}" crate.

%package     -n %{name}+v4_6-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
Requires:       pkgconfig(gtk4) >= 4.6
%description -n %{name}+v4_6-devel

This package contains library source intended for building other packages which
use the "v4_6" feature of the "%{crate}" crate.

%package     -n %{name}+vulkan-devel
Summary:        FFI bindings of GSK 4
BuildArch:      noarch
%description -n %{name}+vulkan-devel

This package contains library source intended for building other packages which
use the "vulkan" feature of the "%{crate}" crate.

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
%files -n rust-gsk4-sys0.10-devel -f %{oreon_filedir}/rust-gsk4-sys0.10-devel.list

%changelog

%autochangelog
