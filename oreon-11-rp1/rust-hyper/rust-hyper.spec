%global source0_hash 27b501faa50e7a26c3d3560ca625132f4078a17771f4810baf70475ae48cbe43
%bcond check 0
%global debug_package %{nil}
%global crate hyper
Name:           rust-hyper
Version:        1.11.1
Release:        1%{?dist}
Summary:        A protective and efficient HTTP library for all.
License:        MIT
URL:            https://crates.io/crates/hyper
Source0:        https://static.crates.io/crates/hyper/hyper-%{version}.crate
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
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+ffi-devel

This package contains library source intended for building other packages which
use the "ffi" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+http1-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+http1-devel

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        A protective and efficient HTTP library for all.
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-hyper-devel -f %{oreon_filedir}/rust-hyper-devel.list

%changelog

%autochangelog
