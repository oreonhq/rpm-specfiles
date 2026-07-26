%global source0_hash 2e5f0162052248946b9f0970a40e9e124236bf86c82b70821143a6fc1dea2574

%global modname unidiff
%global pypi_name unidiff

Name:           python-%{modname}
Version:        0.7.5
Release:        12%{?dist}
Summary:        Python library to parse and interact with unified diffs (patches)
License:        MIT
URL:            http://github.com/matiasb/python-unidiff
Source0:        %pypi_source
BuildArch:      noarch

# use setuptools console_scripts for /usr/bin/unidiff
Patch1: 0001-use-setuptools-console_scripts-for-usr-bin-unidiff.patch

%description
python-unidiff is a Python library to parse and interact with unified diffs 
(patches).

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{modname}
python-unidiff is a Python library to parse and interact with unified diffs 
(patches).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1
rm -r unidiff.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest discover -s tests/

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst HISTORY
%{_bindir}/%{modname}

%changelog
%autochangelog
