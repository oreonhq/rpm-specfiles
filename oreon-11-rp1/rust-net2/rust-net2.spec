%global source0_hash b13b648036a2339d06de780866fbdfda0dde886de7b3af2ddeba8b14f4ee34ac
%bcond check 0
%global debug_package %{nil}
%global crate net2
Name:           rust-net2
Version:        0.2.39
Release:        1%{?dist}
Summary:        Extensions to the standard library's networking types as proposed in...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/net2
Source0:        https://static.crates.io/crates/net2/net2-%{version}.crate
Patch:          net2-fix-metadata-auto.diff
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
Summary:        Extensions to the standard library's networking types as proposed in...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+duration-devel
Summary:        Extensions to the standard library's networking types as proposed in...
BuildArch:      noarch
%description -n %{name}+duration-devel

This package contains library source intended for building other packages which
use the "duration" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Extensions to the standard library's networking types as proposed in...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-net2-devel -f %{oreon_filedir}/rust-net2-devel.list

%changelog

%autochangelog
