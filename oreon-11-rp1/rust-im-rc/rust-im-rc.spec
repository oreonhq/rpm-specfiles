%global source0_hash af1955a75fa080c677d3972822ec4bad316169ab1cfc6c257a942c2265dbe5fe
%bcond check 0
%global debug_package %{nil}
%global crate im-rc
Name:           rust-im-rc
Version:        15.1.0
Release:        2%{?dist}
Summary:        Immutable collection datatypes (the fast but not thread safe version)
License:        MPL-2.0+
URL:            https://crates.io/crates/im-rc
Source0:        https://static.crates.io/crates/im-rc/im-rc-%{version}.crate
Patch:          im-rc-fix-metadata.diff
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
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+pool-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+pool-devel

This package contains library source intended for building other packages which
use the "pool" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+refpool-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+refpool-devel

This package contains library source intended for building other packages which
use the "refpool" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Immutable collection datatypes (the fast but not thread safe version)
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-im-rc-devel -f %{oreon_filedir}/rust-im-rc-devel.list

%changelog

%autochangelog
