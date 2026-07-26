%global source0_hash 62e302ddef0a778a0096b3ca59df065e98451d348f4b2208ba7c89615e913a8f

%bcond check 0

Name:           rust2rpm
Version:        28.0.0
Release:        %autorelease
Summary:        Generate RPM spec files for Rust crates
License:        MIT

URL:            https://codeberg.org/rust2rpm/rust2rpm
Source:         %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  /usr/bin/asciidoctor

%if %{with check}
BuildRequires:  cargo
BuildRequires:  rust2rpm-helper >= 0.1.2
%endif

Requires:       cargo
Requires:       cargo-rpm-macros
Recommends:     rust2rpm-helper >= 0.1.2

# obsolete old provides (removed in Fedora 38)
Obsoletes:      cargo-inspector < 24

# obsolete and / or provide removed Python subpackages (removed in Fedora 38)
%py_provides    python3-rust2rpm
Obsoletes:      python3-rust2rpm < 24
Obsoletes:      python3-rust2rpm-core < 24

%description
rust2rpm is a tool that automates the generation of RPM spec files for
Rust crates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n rust2rpm -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-t}

%build
%pyproject_wheel
# build man pages
pushd docs
asciidoctor -b manpage rust2rpm.1.asciidoc
asciidoctor -b manpage rust2rpm.conf.5.asciidoc
asciidoctor -b manpage rust2rpm.toml.5.asciidoc
popd

%install
%pyproject_install
%pyproject_save_files rust2rpm
# install man pages
install -Dpm 644 docs/rust2rpm.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 644 docs/rust2rpm.conf.5 -t %{buildroot}/%{_mandir}/man5/
install -Dpm 644 docs/rust2rpm.toml.5 -t %{buildroot}/%{_mandir}/man5/

%check
%pyproject_check_import
%if %{with check}
%tox
%endif

%files -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%{_bindir}/rust2rpm
%{_mandir}/man1/rust2rpm.1*
%{_mandir}/man5/rust2rpm.{conf,toml}.5*

%changelog
%autochangelog
