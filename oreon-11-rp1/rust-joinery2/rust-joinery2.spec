%global source0_hash 72167d68f5fce3b8655487b8038691a3c9984ee769590f93f2a631f4ad64e4f5
%bcond check 0
%global debug_package %{nil}
%global crate joinery
Name:           rust-joinery2
Version:        2.1.0
Release:        1%{?dist}
Summary:        Small crate for generically joining iterators with a separator
License:        MIT
URL:            https://crates.io/crates/joinery
Source0:        https://static.crates.io/crates/joinery/joinery-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Small crate for generically joining iterators with a separator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Small crate for generically joining iterators with a separator
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro2-devel
Summary:        Small crate for generically joining iterators with a separator
BuildArch:      noarch
%description -n %{name}+proc-macro2-devel

This package contains library source intended for building other packages which
use the "proc-macro2" feature of the "%{crate}" crate.

%package     -n %{name}+quote-devel
Summary:        Small crate for generically joining iterators with a separator
BuildArch:      noarch
%description -n %{name}+quote-devel

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

%package     -n %{name}+syn-devel
Summary:        Small crate for generically joining iterators with a separator
BuildArch:      noarch
%description -n %{name}+syn-devel

This package contains library source intended for building other packages which
use the "syn" feature of the "%{crate}" crate.

%package     -n %{name}+token-stream-devel
Summary:        Small crate for generically joining iterators with a separator
BuildArch:      noarch
%description -n %{name}+token-stream-devel

This package contains library source intended for building other packages which
use the "token-stream" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
for f in src/lib.rs CHANGELOG.md README.md; do
touch -r $f $f.tstamp
dos2unix $f
touch -r $f.tstamp $f
rm $f.tstamp
done
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
%files -n rust-joinery2-devel -f %{oreon_filedir}/rust-joinery2-devel.list

%changelog

%autochangelog
