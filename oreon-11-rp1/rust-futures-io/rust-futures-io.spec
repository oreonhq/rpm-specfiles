%global source0_hash 53c0fa8157de1303bfffdaa1cc2a673bfffb60102f76b0ef4441659124373fed
%bcond check 1
%global debug_package %{nil}
%global crate futures-io
Name:           rust-futures-io
Version:        0.3.34
Release:        1%{?dist}
Summary:        AsyncRead, AsyncWrite, AsyncSeek, and AsyncBufRead traits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-io
Source0:        https://static.crates.io/crates/futures-io/futures-io-%{version}.crate
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
Summary:        AsyncRead, AsyncWrite, AsyncSeek, and AsyncBufRead traits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        AsyncRead, AsyncWrite, AsyncSeek, and AsyncBufRead traits
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        AsyncRead, AsyncWrite, AsyncSeek, and AsyncBufRead traits
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-futures-io-devel -f %{oreon_filedir}/rust-futures-io-devel.list

%changelog

%autochangelog
