%global source0_hash d89e7ee0cfbedfc4da3340218492196241d89eefb6dab27de5df917a6d2e78cf
%bcond check 0
%global debug_package %{nil}
%global crate md-5
Name:           rust-md-5
Version:        0.10.6
Release:        1%{?dist}
Summary:        MD5 hash function
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/md-5
Source0:        https://static.crates.io/crates/md-5/md-5-%{version}.crate
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
Summary:        MD5 hash function
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        MD5 hash function
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+force-soft-devel
Summary:        MD5 hash function
BuildArch:      noarch
%description -n %{name}+force-soft-devel

This package contains library source intended for building other packages which
use the "force-soft" feature of the "%{crate}" crate.

%package     -n %{name}+loongarch64_asm-devel
Summary:        MD5 hash function
BuildArch:      noarch
%description -n %{name}+loongarch64_asm-devel

This package contains library source intended for building other packages which
use the "loongarch64_asm" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        MD5 hash function
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        MD5 hash function
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
%files -n rust-md-5-devel -f %{oreon_filedir}/rust-md-5-devel.list

%changelog

%autochangelog
