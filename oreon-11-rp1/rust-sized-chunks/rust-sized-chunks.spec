%global source0_hash 16d69225bde7a69b235da73377861095455d298f2b970996eec25ddbb42b3d1e
%bcond check 0
%global debug_package %{nil}
%global crate sized-chunks
Name:           rust-sized-chunks
Version:        0.6.5
Release:        1%{?dist}
Summary:        Efficient sized chunk datatypes
License:        MPL-2.0+
URL:            https://crates.io/crates/sized-chunks
Source0:        https://static.crates.io/crates/sized-chunks/sized-chunks-%{version}.crate
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
Summary:        Efficient sized chunk datatypes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Efficient sized chunk datatypes
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+array-ops-devel
Summary:        Efficient sized chunk datatypes
BuildArch:      noarch
%description -n %{name}+array-ops-devel

This package contains library source intended for building other packages which
use the "array-ops" feature of the "%{crate}" crate.

%package     -n %{name}+refpool-devel
Summary:        Efficient sized chunk datatypes
BuildArch:      noarch
%description -n %{name}+refpool-devel

This package contains library source intended for building other packages which
use the "refpool" feature of the "%{crate}" crate.

%package     -n %{name}+ringbuffer-devel
Summary:        Efficient sized chunk datatypes
BuildArch:      noarch
%description -n %{name}+ringbuffer-devel

This package contains library source intended for building other packages which
use the "ringbuffer" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Efficient sized chunk datatypes
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
%files -n rust-sized-chunks-devel -f %{oreon_filedir}/rust-sized-chunks-devel.list

%changelog

%autochangelog
