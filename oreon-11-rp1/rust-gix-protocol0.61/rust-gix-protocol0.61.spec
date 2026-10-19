%global source0_hash aa4bee82db63ec635996b96efae71cf467c155fa3f34a556184373224a26c4fd
%bcond check 0
%global debug_package %{nil}
%global crate gix-protocol
Name:           rust-gix-protocol0.61
Version:        0.61.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project for implementing git protocols
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-protocol
Source0:        https://static.crates.io/crates/gix-protocol/gix-protocol-%{version}.crate
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

%package     -n %{name}+async-client-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+async-client-devel

This package contains library source intended for building other packages which
use the "async-client" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-client-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+blocking-client-devel

This package contains library source intended for building other packages which
use the "blocking-client" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+fetch-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+fetch-devel

This package contains library source intended for building other packages which
use the "fetch" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+futures-lite-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+futures-lite-devel

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%package     -n %{name}+gix-credentials-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-credentials-devel

This package contains library source intended for building other packages which
use the "gix-credentials" feature of the "%{crate}" crate.

%package     -n %{name}+gix-lock-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-lock-devel

This package contains library source intended for building other packages which
use the "gix-lock" feature of the "%{crate}" crate.

%package     -n %{name}+gix-negotiate-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-negotiate-devel

This package contains library source intended for building other packages which
use the "gix-negotiate" feature of the "%{crate}" crate.

%package     -n %{name}+gix-object-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-object-devel

This package contains library source intended for building other packages which
use the "gix-object" feature of the "%{crate}" crate.

%package     -n %{name}+gix-refspec-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-refspec-devel

This package contains library source intended for building other packages which
use the "gix-refspec" feature of the "%{crate}" crate.

%package     -n %{name}+gix-revwalk-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-revwalk-devel

This package contains library source intended for building other packages which
use the "gix-revwalk" feature of the "%{crate}" crate.

%package     -n %{name}+gix-trace-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+gix-trace-devel

This package contains library source intended for building other packages which
use the "gix-trace" feature of the "%{crate}" crate.

%package     -n %{name}+handshake-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+handshake-devel

This package contains library source intended for building other packages which
use the "handshake" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

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
%files -n rust-gix-protocol0.61-devel -f %{oreon_filedir}/rust-gix-protocol0.61-devel.list

%changelog

%autochangelog
