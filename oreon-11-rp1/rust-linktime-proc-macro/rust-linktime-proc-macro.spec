%global source0_hash 7e57c38c1e860fd37c604281cdfb1dd2216977fd76a50f85ba2f388ef3219616
%bcond check 0
%global debug_package %{nil}
%global crate linktime-proc-macro
Name:           rust-linktime-proc-macro
Version:        0.2.3
Release:        1%{?dist}
Summary:        Proc-macro helpers for linktime crates (ctors, dtors, linker sections)
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/linktime-proc-macro
Source0:        https://static.crates.io/crates/linktime-proc-macro/linktime-proc-macro-%{version}.crate
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
Summary:        Proc-macro helpers for linktime crates (ctors, dtors, linker sections)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ctor-devel
Summary:        Proc-macro helpers for linktime crates (ctors, dtors, linker sections)
BuildArch:      noarch
%description -n %{name}+ctor-devel

This package contains library source intended for building other packages which
use the "ctor" feature of the "%{crate}" crate.

%package     -n %{name}+dtor-devel
Summary:        Proc-macro helpers for linktime crates (ctors, dtors, linker sections)
BuildArch:      noarch
%description -n %{name}+dtor-devel

This package contains library source intended for building other packages which
use the "dtor" feature of the "%{crate}" crate.

%package     -n %{name}+link_section-devel
Summary:        Proc-macro helpers for linktime crates (ctors, dtors, linker sections)
BuildArch:      noarch
%description -n %{name}+link_section-devel

This package contains library source intended for building other packages which
use the "link_section" feature of the "%{crate}" crate.

%package     -n %{name}+scattered_collect-devel
Summary:        Proc-macro helpers for linktime crates (ctors, dtors, linker sections)
BuildArch:      noarch
%description -n %{name}+scattered_collect-devel

This package contains library source intended for building other packages which
use the "scattered_collect" feature of the "%{crate}" crate.

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
%files -n rust-linktime-proc-macro-devel -f %{oreon_filedir}/rust-linktime-proc-macro-devel.list

%changelog

%autochangelog
