%global source0_hash 3e6a7bc7438da9743b4dae9a13a327513941d9af777b9dbfcf576b36976617d7
%bcond check 0
Name:           rust2rpm
Version:        28.1.0
Release:        1%{?dist}
Summary:        Generate RPM spec files for Rust crates
License:        MIT
URL:            https://codeberg.org/rust2rpm/rust2rpm
Source0:        https://codeberg.org/%{name}/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
%if %{with check}
%endif
Requires:       cargo
Requires:       cargo-rpm-macros
Recommends:     rust2rpm-helper >= 0.1.2
Obsoletes:      cargo-inspector < 24
%py_provides    python3-rust2rpm
Obsoletes:      python3-rust2rpm < 24
Obsoletes:      python3-rust2rpm-core < 24
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rust2rpm = %{version}-%{release}
# /oreon:deps
%description
rust2rpm is a tool that automates the generation of RPM spec files for
Rust crates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rust2rpm
%oreon_prep
%build

%pyproject_wheel
pushd docs
asciidoctor -b manpage rust2rpm.1.asciidoc
asciidoctor -b manpage rust2rpm.conf.5.asciidoc
asciidoctor -b manpage rust2rpm.toml.5.asciidoc
popd
%install
%pyproject_install
install -Dpm 644 docs/rust2rpm.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 644 docs/rust2rpm.conf.5 -t %{buildroot}/%{_mandir}/man5/
install -Dpm 644 docs/rust2rpm.toml.5 -t %{buildroot}/%{_mandir}/man5/
%oreon_autofiles main

%check

%pyproject_check_import
%if %{with check}
%tox
%endif
%files

%changelog

%autochangelog
