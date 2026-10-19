%global source0_hash c4b770629624640cf1d22d90d22f0db76318cf3769115e513ec4d7c51ff3538c
%bcond check 1
%global crate rust2rpm-helper
Name:           rust2rpm-helper
Version:        0.1.9
Release:        1%{?dist}
Summary:        Helper program for rust2rpm
SourceLicense:  MIT
License:        MIT AND Apache-2.0 AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://codeberg.org/rust2rpm/rust2rpm-helper
Source0:        https://codeberg.org/rust2rpm/%{name}/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
Helper program for rust2rpm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm 0755 target/rpm/rust2rpm-helper -t %{buildroot}/%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
