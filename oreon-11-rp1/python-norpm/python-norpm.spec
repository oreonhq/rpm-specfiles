%global source0_hash 21ea7acfaab99725129f741ae34225fe82d15e13318b7ffa26b7714a209fa302

Name:           python-norpm
Version:        1.9
Release:        1%?dist
Summary:        RPM Macro Expansion in Python

License:        LGPL-2.1-or-later
URL:            https://github.com/praiskup/norpm
Source:         %pypi_source norpm

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Parse RPM macro and spec files, expanding macros safely—without any potential
Turing-complete side effects.

This is a standalone library and set of tools that depend only on the standard
Python library and PLY (used for expression parsing).
}

%description %_description

%package -n     python3-norpm
Summary:        %summary

%description -n python3-norpm %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n norpm-%version

%if 0%{?rhel} == 9
cat > setup.py <<EOF
from setuptools import setup
setup(
    name='norpm',
    version='%version',
    packages=['norpm', 'norpm.cli'],
    install_requires=['lark-parser'],
    entry_points={
        'console_scripts': [
            'norpm-expand-specfile = norpm.cli.expand_specfile:_main',
            'norpm-conditions-for-arch-statements = norpm.cli.conditions_for_arch_statements:_main',
        ],
    },
)
EOF
%endif

%generate_buildrequires
%pyproject_buildrequires -g test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l norpm

%check
%pyproject_check_import
%pytest

%files -n python3-norpm -f %pyproject_files
%doc README.md
%_bindir/norpm-conditions-for-arch-statements
%_bindir/norpm-expand-specfile

%changelog
%autochangelog
