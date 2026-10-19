%global source0_hash 41dfc780fdec9373c01bae43289ea34c972e40ee3c9f6b3c8801a35f35586ce7
%bcond check 0
%global debug_package %{nil}
%global crate hyper
Name:           rust-hyper0.14
Version:        0.14.32
Release:        1%{?dist}
Summary:        A fast and correct HTTP library.
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
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__internal_happy_eyeballs_tests-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+__internal_happy_eyeballs_tests-devel

This package contains library source intended for building other packages which
use the "__internal_happy_eyeballs_tests" feature of the "%{crate}" crate.

%package     -n %{name}+backports-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+backports-devel

This package contains library source intended for building other packages which
use the "backports" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+deprecated-devel

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+ffi-devel

This package contains library source intended for building other packages which
use the "ffi" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+h2-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+h2-devel

This package contains library source intended for building other packages which
use the "h2" feature of the "%{crate}" crate.

%package     -n %{name}+http1-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+http1-devel

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+tcp-devel
Summary:        A fast and correct HTTP library.
BuildArch:      noarch
%description -n %{name}+tcp-devel

This package contains library source intended for building other packages which
use the "tcp" feature of the "%{crate}" crate.

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
%files -n rust-hyper0.14-devel -f %{oreon_filedir}/rust-hyper0.14-devel.list

%changelog

%autochangelog
