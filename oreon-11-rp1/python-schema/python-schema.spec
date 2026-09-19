%global source0_hash e86cc08edd6fe6e2522648f4e47e3a31920a76e82cce8937535422e310862ab5

%global modname schema

Name:           python-%{modname}
Version:        0.7.8
Release:        2%{?dist}
Summary:        Simple data validation library

License:        MIT
URL:            https://github.com/keleshev/schema
Source0:        %pypi_source schema

BuildArch:      noarch

%global _description \
schema is a library for validating Python data structures, such as those\
obtained from config-files, forms, external services or command-line parsing,\
converted from JSON/YAML (or something else) to Python data-types.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}
sed -i -e /contextlib2/d requirements.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l schema

%check
py.test-%{python3_version} -v

%files -n python3-%{modname} -f %pyproject_files
%doc README.rst

%changelog
%autochangelog
