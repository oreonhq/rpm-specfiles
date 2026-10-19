%global source0_hash 136c8c4c3823846e8ba6d4bda011b4e5d5827b8bb0ac26c31f9ab31abe9f54f2
%bcond check 1
%global debug_package %{nil}
%global crate comfy-table
Name:           rust-comfy-table
Version:        8.0.0
Release:        1%{?dist}
Summary:        Library for building beautiful tables with automatic content wrapping
License:        MIT
URL:            https://crates.io/crates/comfy-table
Source0:        https://static.crates.io/crates/comfy-table/comfy-table-%{version}.crate
Patch:          comfy-table-fix-metadata-auto.diff
Patch:          comfy-table-fix-metadata.diff
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
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-str-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+ansi-str-devel

This package contains library source intended for building other packages which
use the "ansi-str" feature of the "%{crate}" crate.

%package     -n %{name}+console-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+console-devel

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+custom_styling-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+custom_styling-devel

This package contains library source intended for building other packages which
use the "custom_styling" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+integration_test-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+integration_test-devel

This package contains library source intended for building other packages which
use the "integration_test" feature of the "%{crate}" crate.

%package     -n %{name}+reexport_crossterm-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+reexport_crossterm-devel

This package contains library source intended for building other packages which
use the "reexport_crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+tty-devel
Summary:        Library for building beautiful tables with automatic content wrapping
BuildArch:      noarch
%description -n %{name}+tty-devel

This package contains library source intended for building other packages which
use the "tty" feature of the "%{crate}" crate.

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
%files -n rust-comfy-table-devel -f %{oreon_filedir}/rust-comfy-table-devel.list

%changelog

%autochangelog
