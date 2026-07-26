%global source0_hash fbdee7351a7423e7907fb8a9c3b77305f6b5678cb2e6fd0db36a8825e42955ec

%global modname pygal

Name:               python-pygal
Version:            3.1.0
Release:            %autorelease
Summary:            A python svg graph plotting library

License:            LGPL-3.0-or-later
URL:                https://pypi.io/project/pygal
Source0:            https://pypi.io/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

# Remove pytest-runner
# https://github.com/Kozea/pygal/pull/578
Patch:              https://github.com/Kozea/pygal/pull/578.patch

BuildArch:          noarch

BuildRequires:      python3-devel
# Test requirements
BuildRequires:      python3-pytest
BuildRequires:      python3-pyquery

%global _description\
A python svg graph plotting library.

%description %_description

%package -n python3-pygal
Summary:            A python svg graph plotting library

Requires:           python3-lxml

%description -n python3-pygal
A python svg graph plotting library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pygal

%check
%pytest

%files -n python3-pygal -f %{pyproject_files}
%doc README.md
%{_bindir}/pygal_gen.py

%changelog
%autochangelog
