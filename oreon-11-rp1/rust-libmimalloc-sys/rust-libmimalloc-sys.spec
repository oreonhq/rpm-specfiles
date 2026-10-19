%global source0_hash 6a45a52f43e1c16f667ccfe4dd8c85b7f7c204fd5e3bf46c5b0db9a5c3c0b8e9
%bcond check 1
%global debug_package %{nil}
%global crate libmimalloc-sys
Name:           rust-libmimalloc-sys
Version:        0.1.49
Release:        1%{?dist}
Summary:        Sys crate wrapping the mimalloc allocator
License:        MIT
URL:            https://crates.io/crates/libmimalloc-sys
Source0:        https://static.crates.io/crates/libmimalloc-sys/libmimalloc-sys-%{version}.crate
Provides:       bundled(mimalloc) = 2.2.4
Provides:       bundled(mimalloc) = 3.1.5
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
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arena-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+arena-devel

This package contains library source intended for building other packages which
use the "arena" feature of the "%{crate}" crate.

%package     -n %{name}+cty-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+cty-devel

This package contains library source intended for building other packages which
use the "cty" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+debug_in_debug-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+debug_in_debug-devel

This package contains library source intended for building other packages which
use the "debug_in_debug" feature of the "%{crate}" crate.

%package     -n %{name}+extended-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+extended-devel

This package contains library source intended for building other packages which
use the "extended" feature of the "%{crate}" crate.

%package     -n %{name}+local_dynamic_tls-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+local_dynamic_tls-devel

This package contains library source intended for building other packages which
use the "local_dynamic_tls" feature of the "%{crate}" crate.

%package     -n %{name}+no_thp-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+no_thp-devel

This package contains library source intended for building other packages which
use the "no_thp" feature of the "%{crate}" crate.

%package     -n %{name}+override-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+override-devel

This package contains library source intended for building other packages which
use the "override" feature of the "%{crate}" crate.

%package     -n %{name}+secure-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+secure-devel

This package contains library source intended for building other packages which
use the "secure" feature of the "%{crate}" crate.

%package     -n %{name}+v3-devel
Summary:        Sys crate wrapping the mimalloc allocator
BuildArch:      noarch
%description -n %{name}+v3-devel

This package contains library source intended for building other packages which
use the "v3" feature of the "%{crate}" crate.

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
%files -n rust-libmimalloc-sys-devel -f %{oreon_filedir}/rust-libmimalloc-sys-devel.list

%changelog

%autochangelog
