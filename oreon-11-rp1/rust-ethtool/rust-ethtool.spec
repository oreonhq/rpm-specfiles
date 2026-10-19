%global source0_hash f09def780eb764a5ec8678e6f2af2be8ee82c41b6a433b4dc800cc1e17aeb691
%bcond check 0
%global debug_package %{nil}
%global crate ethtool
Name:           rust-ethtool
Version:        0.3.0
Release:        1%{?dist}
Summary:        Linux Ethtool Communication Library
License:        MIT
URL:            https://crates.io/crates/ethtool
Source0:        https://static.crates.io/crates/ethtool/ethtool-%{version}.crate
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
Summary:        Linux Ethtool Communication Library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Linux Ethtool Communication Library
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+smol_socket-devel
Summary:        Linux Ethtool Communication Library
BuildArch:      noarch
%description -n %{name}+smol_socket-devel

This package contains library source intended for building other packages which
use the "smol_socket" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Linux Ethtool Communication Library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_socket-devel
Summary:        Linux Ethtool Communication Library
BuildArch:      noarch
%description -n %{name}+tokio_socket-devel

This package contains library source intended for building other packages which
use the "tokio_socket" feature of the "%{crate}" crate.

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
%files -n rust-ethtool-devel -f %{oreon_filedir}/rust-ethtool-devel.list

%changelog

%autochangelog
