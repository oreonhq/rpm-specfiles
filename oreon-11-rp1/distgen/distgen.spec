%global source0_hash c3efda88bbf93424050f422d942f96cbd06ebc0fe774341c2dfe88c9bf6dac5e

Name:       distgen
Summary:    Templating system/generator for distributions
Version:    2.2
Release:    3%{?dist}
License:    GPL-2.0-or-later AND Apache-2.0
URL:        https://github.com/devexp-db/distgen
BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-pytest

Source0: https://pypi.org/packages/source/d/%name/%name-%version.tar.gz

%description
Based on given template specification (configuration for template), template
file and preexisting distribution metadata generate output file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -x pytest,pytest-catchlog,pytest-cov,coverage,flake8

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files distgen

%check
%pytest tests/unittests/

%files -f %{pyproject_files}
%license LICENSE
%doc NEWS
%doc docs/
%{_bindir}/dg
%{_mandir}/man1/*

%changelog
%autochangelog
