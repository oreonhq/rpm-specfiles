%global source0_hash 7a5a4b21e1a62b67a2970e6831bc091d7b87e119e7f9791aef9702e3bef04448
%bcond check 0
%global debug_package %{nil}
%global crate y4m
Name:           rust-y4m
Version:        0.8.0
Release:        1%{?dist}
Summary:        YUV4MPEG2 (.y4m) Encoder/Decoder.
License:        MIT
URL:            https://crates.io/crates/y4m
Source0:        https://static.crates.io/crates/y4m/y4m-%{version}.crate
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
Summary:        YUV4MPEG2 (.y4m) Encoder/Decoder.
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
%files -n rust-y4m-devel -f %{oreon_filedir}/rust-y4m-devel.list

%changelog

%autochangelog
