%global source0_hash ed5725a3379c44dc0adf3437af87cf21c10df473ed858d654b12603dea102508
%bcond check 1
%global debug_package %{nil}
%global crate norm
Name:           rust-norm
Version:        0.1.1
Release:        1%{?dist}
Summary:        Collection of distance metrics on strings
License:        MIT
URL:            https://crates.io/crates/norm
Source0:        https://static.crates.io/crates/norm/norm-%{version}.crate
Patch:          norm-fix-metadata.diff
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
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__any-metric-devel
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+__any-metric-devel

This package contains library source intended for building other packages which
use the "__any-metric" feature of the "%{crate}" crate.

%package     -n %{name}+__benches-devel
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+__benches-devel

This package contains library source intended for building other packages which
use the "__benches" feature of the "%{crate}" crate.

%package     -n %{name}+__into-score-devel
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+__into-score-devel

This package contains library source intended for building other packages which
use the "__into-score" feature of the "%{crate}" crate.

%package     -n %{name}+__tests-devel
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+__tests-devel

This package contains library source intended for building other packages which
use the "__tests" feature of the "%{crate}" crate.

%package     -n %{name}+fzf-v1-devel
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+fzf-v1-devel

This package contains library source intended for building other packages which
use the "fzf-v1" feature of the "%{crate}" crate.

%package     -n %{name}+fzf-v2-devel
Summary:        Collection of distance metrics on strings
BuildArch:      noarch
%description -n %{name}+fzf-v2-devel

This package contains library source intended for building other packages which
use the "fzf-v2" feature of the "%{crate}" crate.

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
%files -n rust-norm-devel -f %{oreon_filedir}/rust-norm-devel.list

%changelog

%autochangelog
