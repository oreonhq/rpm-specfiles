%global source0_hash 30d65c71f1ce40ab09135ce117d742b9f8a19ff91a41a8b57ed50bc2de59c427
%bcond check 0
%global debug_package %{nil}
%global crate mio
Name:           rust-mio
Version:        1.2.2
Release:        1%{?dist}
Summary:        Lightweight non-blocking I/O.
License:        MIT
URL:            https://crates.io/crates/mio
Source0:        https://static.crates.io/crates/mio/mio-%{version}.crate
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
Summary:        Lightweight non-blocking I/O.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Lightweight non-blocking I/O.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Lightweight non-blocking I/O.
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+os-ext-devel
Summary:        Lightweight non-blocking I/O.
BuildArch:      noarch
%description -n %{name}+os-ext-devel

This package contains library source intended for building other packages which
use the "os-ext" feature of the "%{crate}" crate.

%package     -n %{name}+os-poll-devel
Summary:        Lightweight non-blocking I/O.
BuildArch:      noarch
%description -n %{name}+os-poll-devel

This package contains library source intended for building other packages which
use the "os-poll" feature of the "%{crate}" crate.

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
%files -n rust-mio-devel -f %{oreon_filedir}/rust-mio-devel.list

%changelog

%autochangelog
