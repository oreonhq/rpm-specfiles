%global source0_hash 06432fb54d3be7964ecd3649233cddf80db2832f47fec34c01f65b3d9d774983
%bcond check 1
%global debug_package %{nil}
%global crate io-lifetimes
Name:           rust-io-lifetimes2
Version:        2.0.4
Release:        1%{?dist}
Summary:        Low-level I/O ownership and borrowing library
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/io-lifetimes
Source0:        https://static.crates.io/crates/io-lifetimes/io-lifetimes-%{version}.crate
Patch:          io-lifetimes-fix-metadata-auto.diff
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
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+close-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+close-devel

This package contains library source intended for building other packages which
use the "close" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+mio-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+mio-devel

This package contains library source intended for building other packages which
use the "mio" feature of the "%{crate}" crate.

%package     -n %{name}+os_pipe-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+os_pipe-devel

This package contains library source intended for building other packages which
use the "os_pipe" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-io-lifetimes2-devel -f %{oreon_filedir}/rust-io-lifetimes2-devel.list

%changelog

%autochangelog
