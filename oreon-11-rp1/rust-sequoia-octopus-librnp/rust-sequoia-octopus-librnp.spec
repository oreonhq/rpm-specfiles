%global source0_hash 7cec5eac6fa7fa05b1eb301901bf5aa16bf950d352a98799157dd12af910e342
%bcond check 1
%global crate sequoia-octopus-librnp
%global tb_plugindir %{_libdir}/thunderbird
%global __provides_exclude_from ^%{tb_plugindir}/.*\\.so$
Name:           rust-sequoia-octopus-librnp
Version:        1.11.1
Release:        1%{?dist}
Summary:        Reimplementation of RNP's interface using Sequoia for use with Thunderbird
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-octopus-librnp
Source0:        https://static.crates.io/crates/sequoia-octopus-librnp/sequoia-octopus-librnp-%{version}.crate
Patch:          sequoia-octopus-librnp-fix-metadata-auto.diff
Patch:          sequoia-octopus-librnp-fix-metadata.diff
Patch:          0001-drop-broken-build-script-based-git-versioning.patch
ExcludeArch:    %{ix86} %{arm} s390x
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Reimplementation of RNP's interface using Sequoia for use with Thunderbird
License:        %{shrink:
    LGPL-2.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (MIT OR LGPL-3.0-or-later) AND
    (Unlicense OR MIT)
}
Requires:       thunderbird%{?_isa}
Provides:       thunderbird-librnp
Provides:       thunderbird-librnp%{?_isa}
Conflicts:      thunderbird-librnp%{?_isa}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
mkdir -p %{buildroot}/%{tb_plugindir}
cp -pav target/release/libsequoia_octopus_librnp.so %{buildroot}/%{tb_plugindir}/librnp.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-octopus-librnp -f %{oreon_filedir}/sequoia-octopus-librnp.list

%changelog

%autochangelog
