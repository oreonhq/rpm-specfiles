%global source0_hash 8067b404fe97c70829f082dec8bcf4f71225d7eaea1d8645349cb76fa06205cc
%bcond check 0
%global debug_package %{nil}
%global crate mio
Name:           rust-mio0.7
Version:        0.7.14
Release:        1%{?dist}
Summary:        Lightweight non-blocking IO
License:        MIT
URL:            https://crates.io/crates/mio
Source0:        https://static.crates.io/crates/mio/mio-%{version}.crate
Patch:          mio-fix-metadata-auto.diff
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
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+extra-docs-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+extra-docs-devel

This package contains library source intended for building other packages which
use the "extra-docs" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+os-ext-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+os-ext-devel

This package contains library source intended for building other packages which
use the "os-ext" feature of the "%{crate}" crate.

%package     -n %{name}+os-poll-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+os-poll-devel

This package contains library source intended for building other packages which
use the "os-poll" feature of the "%{crate}" crate.

%package     -n %{name}+os-util-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+os-util-devel

This package contains library source intended for building other packages which
use the "os-util" feature of the "%{crate}" crate.

%package     -n %{name}+pipe-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+pipe-devel

This package contains library source intended for building other packages which
use the "pipe" feature of the "%{crate}" crate.

%package     -n %{name}+tcp-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+tcp-devel

This package contains library source intended for building other packages which
use the "tcp" feature of the "%{crate}" crate.

%package     -n %{name}+udp-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+udp-devel

This package contains library source intended for building other packages which
use the "udp" feature of the "%{crate}" crate.

%package     -n %{name}+uds-devel
Summary:        Lightweight non-blocking IO
BuildArch:      noarch
%description -n %{name}+uds-devel

This package contains library source intended for building other packages which
use the "uds" feature of the "%{crate}" crate.

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
%files -n rust-mio0.7-devel -f %{oreon_filedir}/rust-mio0.7-devel.list

%changelog

%autochangelog
