%global source0_hash 309217bc53e2c691c314389c7fa91f9cd1a998cda19e25544ea47d94103880c3
%bcond check 0
%global debug_package %{nil}
%global crate grep
Name:           rust-grep
Version:        0.4.1
Release:        1%{?dist}
Summary:        Fast line oriented regex searching as a library
License:        Unlicense OR MIT
URL:            https://crates.io/crates/grep
Source0:        https://static.crates.io/crates/grep/grep-%{version}.crate
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
Summary:        Fast line oriented regex searching as a library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+grep-pcre2-devel
Summary:        Fast line oriented regex searching as a library
BuildArch:      noarch
%description -n %{name}+grep-pcre2-devel

This package contains library source intended for building other packages which
use the "grep-pcre2" feature of the "%{crate}" crate.

%package     -n %{name}+pcre2-devel
Summary:        Fast line oriented regex searching as a library
BuildArch:      noarch
%description -n %{name}+pcre2-devel

This package contains library source intended for building other packages which
use the "pcre2" feature of the "%{crate}" crate.

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
%files -n rust-grep-devel -f %{oreon_filedir}/rust-grep-devel.list

%changelog

%autochangelog
