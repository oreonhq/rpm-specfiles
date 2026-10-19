%global source0_hash c28284f834fe0083db924efe590a684fe81c661c6269fc536ae964ab01adc111
%bcond check 1
%global debug_package %{nil}
%global crate gvdb
Name:           rust-gvdb
Version:        0.10.1
Release:        1%{?dist}
Summary:        Implementation of the glib gvdb file format
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gvdb
Source0:        https://static.crates.io/crates/gvdb/gvdb-%{version}.crate
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
Summary:        Implementation of the glib gvdb file format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+glib-devel
Summary:        Implementation of the glib gvdb file format
BuildArch:      noarch
%description -n %{name}+glib-devel

This package contains library source intended for building other packages which
use the "glib" feature of the "%{crate}" crate.

%package     -n %{name}+gresource-devel
Summary:        Implementation of the glib gvdb file format
BuildArch:      noarch
%description -n %{name}+gresource-devel

This package contains library source intended for building other packages which
use the "gresource" feature of the "%{crate}" crate.

%package     -n %{name}+mmap-devel
Summary:        Implementation of the glib gvdb file format
BuildArch:      noarch
%description -n %{name}+mmap-devel

This package contains library source intended for building other packages which
use the "mmap" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-gvdb-devel -f %{oreon_filedir}/rust-gvdb-devel.list

%changelog

%autochangelog
