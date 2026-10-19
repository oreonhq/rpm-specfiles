%global source0_hash 6ab8598aa408498679922eff7fa985c25d58a90771bd6be794434c5277eab1a6
%bcond check 1
%global debug_package %{nil}
%global crate scroll
Name:           rust-scroll0.12
Version:        0.12.0
Release:        1%{?dist}
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
License:        MIT
URL:            https://crates.io/crates/scroll
Source0:        https://static.crates.io/crates/scroll/scroll-%{version}.crate
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
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Powerful, extensible, generic, endian-aware Read/Write traits for byte buffers
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-scroll0.12-devel -f %{oreon_filedir}/rust-scroll0.12-devel.list

%changelog

%autochangelog
