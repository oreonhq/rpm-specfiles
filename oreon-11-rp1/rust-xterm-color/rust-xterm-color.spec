%global source0_hash 7008a9d8ba97a7e47d9b2df63fcdb8dade303010c5a7cd5bf2469d4da6eba673
%bcond check 1
%global debug_package %{nil}
%global crate xterm-color
Name:           rust-xterm-color
Version:        1.0.2
Release:        1%{?dist}
Summary:        Parses subset of X11 Color Strings for OSC color queries
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/xterm-color
Source0:        https://static.crates.io/crates/xterm-color/xterm-color-%{version}.crate
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
Summary:        Parses subset of X11 Color Strings for OSC color queries
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-xterm-color-devel -f %{oreon_filedir}/rust-xterm-color-devel.list

%changelog

%autochangelog
