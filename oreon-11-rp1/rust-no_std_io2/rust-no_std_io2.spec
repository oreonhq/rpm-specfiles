%global source0_hash 418abd1b6d34fbf6cae440dc874771b0525a604428704c76e48b29a5e67b8003
%bcond check 0
%global debug_package %{nil}
%global crate no_std_io2
Name:           rust-no_std_io2
Version:        0.9.4
Release:        1%{?dist}
Summary:        The bare essentials of std::io for use in no_std. Alloc support is op...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/no_std_io2
Source0:        https://static.crates.io/crates/no_std_io2/no_std_io2-%{version}.crate
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
Summary:        The bare essentials of std::io for use in no_std. Alloc support is op...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        The bare essentials of std::io for use in no_std. Alloc support is op...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        The bare essentials of std::io for use in no_std. Alloc support is op...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        The bare essentials of std::io for use in no_std. Alloc support is op...
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
%files -n rust-no_std_io2-devel -f %{oreon_filedir}/rust-no_std_io2-devel.list

%changelog

%autochangelog
