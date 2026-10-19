%global source0_hash 420fafe9f26223a14dd62544d158fe1452e79889eefdb53d022444745422e8a0
%bcond check 0
%global crate python-launcher
Name:           rust-python-launcher
Version:        1.0.1
Release:        1%{?dist}
Summary:        Python launcher for Unix
License:        MIT
URL:            https://crates.io/crates/python-launcher
Source0:        https://static.crates.io/crates/python-launcher/python-launcher-%{version}.crate
Patch:          python-launcher-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Python launcher for Unix
License:        MIT AND Apache-2.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
Provides:       py = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       py%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Python launcher for Unix
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav man-page/py.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{fish_completions_dir}
cp -pav completions/py.fish %{buildroot}/%{fish_completions_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n python-launcher -f %{oreon_filedir}/python-launcher.list
%files -n rust-python-launcher-devel -f %{oreon_filedir}/rust-python-launcher-devel.list

%changelog

%autochangelog
