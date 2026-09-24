%global source0_hash f8be167aedf5670bd7c812ef515968ff4717c63cfc9cb4df5f34b54fd5649c37

%global upname sphinx-argparse
%global srcname sphinx_argparse

Name: python-%{upname}
Version: 0.6.1
Release: %autorelease
Summary: Sphinx extension that automatically documents argparse commands and options
BuildArch: noarch

License: MIT
Url: https://github.com/ashb/sphinx-argparse
Source: %{pypi_source %{srcname}}

BuildRequires:  python3-devel
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist lxml}

%description
Sphinx extension that automatically documents argparse commands and options

%package -n python3-%{upname}
Summary: %{summary}

%description -n python3-%{upname}
Sphinx extension that automatically documents argparse commands and options

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxarg

%check
%pytest

%files -n python3-%{upname} -f %{pyproject_files}
%license LICENCE.rst
%doc README.rst

%changelog
%autochangelog
