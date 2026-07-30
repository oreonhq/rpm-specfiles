%global source0_hash 06abe2d73597523694542dc609f0c69780d99112070439fed99b5c261b7cba37

%bcond_without check

Name:           cargo2rpm
Version:        0.3.3
Release:        3%{?dist}
Summary:        Translation layer between cargo and RPM
License:        MIT
URL:            https://codeberg.org/rust2rpm/cargo2rpm
Source0:        https://codeberg.org/rust2rpm/cargo2rpm/archive/v%{version}.tar.gz
Patch0:         cargo2rpm-0.3.3-host-target-deps.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  python3-pytest
%endif

Requires:       cargo

%description
cargo2rpm implements a translation layer between cargo and RPM. It
provides a CLI interface (for implementing RPM macros and generators)
and a Python API (which rust2rpm is built upon).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cargo2rpm -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cargo2rpm

%check
%pyproject_check_import
%if %{with check}
%pytest
%endif

%files -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%{_bindir}/cargo2rpm

%changelog
%autochangelog
