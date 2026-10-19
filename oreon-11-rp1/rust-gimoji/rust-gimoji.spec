%global source0_hash c9bf0c522347a6f47943877785f2a809db35ee5eb2bba8827d4a6bb3ba244feb
%bcond check 1
%global crate gimoji
Name:           rust-gimoji
Version:        1.4.0
Release:        1%{?dist}
Summary:        Easily add emojis to your git commit messages 🎉
License:        MIT
URL:            https://crates.io/crates/gimoji
Source0:        https://static.crates.io/crates/gimoji/gimoji-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Easily add emojis to your git commit messages 🎉
License:        %{shrink:
    MIT
    AND Apache-2.0
    AND Unicode-DFS-2016
    AND Zlib
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
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
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gimoji -f %{oreon_filedir}/gimoji.list

%changelog

%autochangelog
