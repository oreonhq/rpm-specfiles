%global source0_hash ad5fd71b79026fb918650dde6d125000a233764f1c2f1659a1c71118e33ea08f
%bcond check 1
%global debug_package %{nil}
%global crate os_display
Name:           rust-os_display
Version:        0.1.4
Release:        1%{?dist}
Summary:        Display strings in a safe platform-appropriate way
License:        MIT
URL:            https://crates.io/crates/os_display
Source0:        https://static.crates.io/crates/os_display/os_display-%{version}.crate
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
Summary:        Display strings in a safe platform-appropriate way
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Display strings in a safe platform-appropriate way
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+native-devel
Summary:        Display strings in a safe platform-appropriate way
BuildArch:      noarch
%description -n %{name}+native-devel

This package contains library source intended for building other packages which
use the "native" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Display strings in a safe platform-appropriate way
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unix-devel
Summary:        Display strings in a safe platform-appropriate way
BuildArch:      noarch
%description -n %{name}+unix-devel

This package contains library source intended for building other packages which
use the "unix" feature of the "%{crate}" crate.

%package     -n %{name}+windows-devel
Summary:        Display strings in a safe platform-appropriate way
BuildArch:      noarch
%description -n %{name}+windows-devel

This package contains library source intended for building other packages which
use the "windows" feature of the "%{crate}" crate.

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
%files -n rust-os_display-devel -f %{oreon_filedir}/rust-os_display-devel.list

%changelog

%autochangelog
