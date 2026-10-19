%global source0_hash ab7c3f5d4ee3bf5472d4d23707a6903d03544586827385340220a89e4f32904a
%bcond check 1
%global crate rpm-sequoia
Name:           rust-rpm-sequoia
Version:        1.10.3
Release:        1%{?dist}
Summary:        Implementation of the RPM PGP interface using Sequoia
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/rpm-sequoia
Source0:        https://static.crates.io/crates/rpm-sequoia/rpm-sequoia-%{version}.crate
Patch:          rpm-sequoia-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Implementation of the RPM PGP interface using Sequoia
License:        %{shrink:
    LGPL-2.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
%description -n %{crate}

%package     -n %{crate}-devel
Summary:        Implementation of the RPM PGP interface using Sequoia
Requires:       %{crate}%{?_isa} = %{version}-%{release}
%description -n %{crate}-devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

export PREFIX="%{_prefix}"
export LIBDIR="%{_libdir}"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
mkdir -p %{buildroot}/%{_libdir}
cp -pav target/release/librpm_sequoia.so %{buildroot}/%{_libdir}/librpm_sequoia.so.1
ln -s librpm_sequoia.so.1 %{buildroot}/%{_libdir}/librpm_sequoia.so
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cp -pav target/release/rpm-sequoia.pc %{buildroot}/%{_libdir}/pkgconfig/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

export TEST_DONT_BUILD_LIB=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rpm-sequoia -f %{oreon_filedir}/rpm-sequoia.list
%files -n rpm-sequoia-devel -f %{oreon_filedir}/rpm-sequoia-devel.list

%changelog

%autochangelog
