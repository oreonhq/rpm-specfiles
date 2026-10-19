%global source0_hash a252f5e20f038fe7b4ea53e073e65398d652c864cc162fc77c56c2f13717b888
%bcond check 0
%global debug_package %{nil}
%global crate ruzstd
Name:           rust-ruzstd0.9
Version:        0.9.0
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

%package     -n %{name}+dict_builder-devel
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+dict_builder-devel

This package contains library source intended for building other packages which
use the "dict_builder" feature of the "%{crate}" crate.

%package     -n %{name}+fuzz_exports-devel
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+fuzz_exports-devel

This package contains library source intended for building other packages which
use the "fuzz_exports" feature of the "%{crate}" crate.

%package     -n %{name}+hash-devel
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+hash-devel

This package contains library source intended for building other packages which
use the "hash" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        Decoder for the zstd compression format
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

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
%files -n rust-ruzstd0.9-devel -f %{oreon_filedir}/rust-ruzstd0.9-devel.list

%changelog

%autochangelog
