%global source0_hash ae857c3cde962a1ade2b981f7e01cf95e9fa05d5c5f95f94cf5f35394c1bf899
Name:           sudo-rs
Version:        0.2.15
Release:        1%{?dist}
Summary:        Memory safe implementation of sudo and su
SourceLicense:  Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://github.com/trifectatechfoundation/sudo-rs
Source0:        https://github.com/trifectatechfoundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/pkill
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pam-devel
BuildRequires:  rustc
# /oreon:deps
%description
A memory safe implementation of sudo and su.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n sudo-rs-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f pam-login
%{cargo_license_summary -f pam-login}
%{cargo_license -f pam-login} > LICENSE.dependencies
%install
install -Dpm 0755 target/rpm/su -T %{buildroot}/%{_bindir}/su-rs
install -Dpm 0755 target/rpm/sudo -T %{buildroot}/%{_bindir}/sudo-rs
install -Dpm 0755 target/rpm/visudo -T %{buildroot}/%{_bindir}/visudo-rs
%oreon_autofiles main
%if %{with check}
%check

%cargo_test -f pam-login -- -- --exact --skip common::context::tests::test_build_run_context
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
