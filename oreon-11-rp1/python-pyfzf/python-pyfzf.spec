%global source0_hash dd902e34cffeca9c3082f96131593dd20b4b3a9bba5b9dde1b0688e424b46bd2

%global srcname pyfzf

Summary:        Python wrapper for junegunn's fuzzyfinder (fzf)
Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source %{srcname}}
Patch:          pyfzf-0.3.1-test.patch
BuildArch:      noarch
BuildRequires:  fzf
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%global _description \
Python wrapper for junegunn's awesome fuzzyfinder (fzf), \
a general-purpose command-line fuzzy finder.
%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
Requires:       fzf
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' pyfzf/pyfzf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
