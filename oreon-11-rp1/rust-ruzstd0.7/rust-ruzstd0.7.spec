%global source0_hash fad02996bfc73da3e301efe90b1837be9ed8f4a462b6ed410aa35d00381de89f
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate ruzstd
Name:           rust-ruzstd0.7
Version:        0.7.3
Release:        1%{?dist}
Summary:        Decoder for the zstd compression format
License:        MIT
URL:            https://crates.io/crates/ruzstd
Source0:        https://static.crates.io/crates/ruzstd/ruzstd-%{version}.crate
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
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hash-devel
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+hash-devel

This package contains library source intended for building other packages which
use the "hash" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ruzstd0.7-devel -f %{oreon_filedir}/rust-ruzstd0.7-devel.list

%changelog

%autochangelog
