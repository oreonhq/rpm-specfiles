%global source0_hash 9048a889effe34a5cddee0af7f53285198b16dca3be510858d38dfdb3e62a04e
%bcond check 0
%global debug_package %{nil}
%global crate termina
Name:           rust-termina
Version:        0.3.3
Release:        1%{?dist}
Summary:        A cross-platform VT manipulation library
License:        MIT OR MPL-2.0
URL:            https://crates.io/crates/termina
Source0:        https://static.crates.io/crates/termina/termina-%{version}.crate
Patch:          termina-fix-metadata-auto.diff
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
Summary:        A cross-platform VT manipulation library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+event-stream-devel
Summary:        A cross-platform VT manipulation library
BuildArch:      noarch
%description -n %{name}+event-stream-devel

This package contains library source intended for building other packages which
use the "event-stream" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        A cross-platform VT manipulation library
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+windows-legacy-devel
Summary:        A cross-platform VT manipulation library
BuildArch:      noarch
%description -n %{name}+windows-legacy-devel

This package contains library source intended for building other packages which
use the "windows-legacy" feature of the "%{crate}" crate.

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
%files -n rust-termina-devel -f %{oreon_filedir}/rust-termina-devel.list

%changelog

%autochangelog
