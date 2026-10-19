%global source0_hash cfc320937d09e6de266b31b9afb480f197d7a861be86be7cb2ea7e5d1bfffc5e
%bcond check 0
%global debug_package %{nil}
%global crate combine
Name:           rust-combine
Version:        4.6.8
Release:        1%{?dist}
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
License:        MIT
URL:            https://crates.io/crates/combine
Source0:        https://static.crates.io/crates/combine/combine-%{version}.crate
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
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+bytes_05-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+bytes_05-devel

This package contains library source intended for building other packages which
use the "bytes_05" feature of the "%{crate}" crate.

%package     -n %{name}+futures-03-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+futures-03-devel

This package contains library source intended for building other packages which
use the "futures-03" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-03-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+futures-core-03-devel

This package contains library source intended for building other packages which
use the "futures-core-03" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-03-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+futures-io-03-devel

This package contains library source intended for building other packages which
use the "futures-io-03" feature of the "%{crate}" crate.

%package     -n %{name}+mp4-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+mp4-devel

This package contains library source intended for building other packages which
use the "mp4" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+pin-project-devel

This package contains library source intended for building other packages which
use the "pin-project" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-02-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-02-devel

This package contains library source intended for building other packages which
use the "tokio-02" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-02-dep-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-02-dep-devel

This package contains library source intended for building other packages which
use the "tokio-02-dep" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-03-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-03-devel

This package contains library source intended for building other packages which
use the "tokio-03" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-03-dep-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-03-dep-devel

This package contains library source intended for building other packages which
use the "tokio-03-dep" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-dep-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-dep-devel

This package contains library source intended for building other packages which
use the "tokio-dep" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Fast parser combinators on arbitrary streams with zero-copy support.
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

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
%files -n rust-combine-devel -f %{oreon_filedir}/rust-combine-devel.list

%changelog

%autochangelog
