%global source0_hash d075ab8a203a6ab4bc1bce0a4b9fe486a72bf8b939037f4b78d95386384bc80a
%bcond check 1
%global debug_package %{nil}
%global crate opendal
Name:           rust-opendal
Version:        0.55.0
Release:        1%{?dist}
Summary:        Apache OpenDAL: One Layer, All Storage
License:        Apache-2.0
URL:            https://crates.io/crates/opendal
Source0:        https://static.crates.io/crates/opendal/opendal-%{version}.crate
Patch:          opendal-fix-metadata-auto.diff
Patch:          opendal-fix-metadata.diff
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
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+executors-tokio-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+executors-tokio-devel

This package contains library source intended for building other packages which
use the "executors-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+internal-tokio-rt-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+internal-tokio-rt-devel

This package contains library source intended for building other packages which
use the "internal-tokio-rt" feature of the "%{crate}" crate.

%package     -n %{name}+services-fs-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+services-fs-devel

This package contains library source intended for building other packages which
use the "services-fs" feature of the "%{crate}" crate.

%package     -n %{name}+services-memcached-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+services-memcached-devel

This package contains library source intended for building other packages which
use the "services-memcached" feature of the "%{crate}" crate.

%package     -n %{name}+services-memory-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+services-memory-devel

This package contains library source intended for building other packages which
use the "services-memory" feature of the "%{crate}" crate.

%package     -n %{name}+services-webdav-devel
Summary:        Apache OpenDAL: One Layer, All Storage
BuildArch:      noarch
%description -n %{name}+services-webdav-devel

This package contains library source intended for building other packages which
use the "services-webdav" feature of the "%{crate}" crate.

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

%cargo_test -- --lib -- --skip tests::assert_size
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-opendal-devel -f %{oreon_filedir}/rust-opendal-devel.list

%changelog

%autochangelog
