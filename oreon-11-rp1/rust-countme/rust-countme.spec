%global source0_hash 7704b5fdd17b18ae31c4c1da5a2e0305a2bf17b5249300a9ee9ed7b72114c636
%bcond check 0
%global debug_package %{nil}
%global crate countme
Name:           rust-countme
Version:        3.0.1
Release:        1%{?dist}
Summary:        Counts the number of live instances of types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/countme
Source0:        https://static.crates.io/crates/countme/countme-%{version}.crate
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
Summary:        Counts the number of live instances of types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        Counts the number of live instances of types
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+enable-devel
Summary:        Counts the number of live instances of types
BuildArch:      noarch
%description -n %{name}+enable-devel

This package contains library source intended for building other packages which
use the "enable" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        Counts the number of live instances of types
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+print_at_exit-devel
Summary:        Counts the number of live instances of types
BuildArch:      noarch
%description -n %{name}+print_at_exit-devel

This package contains library source intended for building other packages which
use the "print_at_exit" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-hash-devel
Summary:        Counts the number of live instances of types
BuildArch:      noarch
%description -n %{name}+rustc-hash-devel

This package contains library source intended for building other packages which
use the "rustc-hash" feature of the "%{crate}" crate.

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
%files -n rust-countme-devel -f %{oreon_filedir}/rust-countme-devel.list

%changelog

%autochangelog
