%global source0_hash 46bed4611fb53edc731aadeb64b28308bcb848f4cc150c60c948d078f7108721

%define modname zope_deprecation

Name:           python-zope-deprecation
Version:        5.1
Release:        %autorelease
Summary:        Zope 3 Deprecation Infrastructure

License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.deprecation
Source0:        https://files.pythonhosted.org/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
This package provides a simple function called 'deprecated(names, reason)' to\
deprecate the previously mentioned Python objects.

%description %_description

%package -n python3-zope-deprecation
Summary:        Zope 3 Deprecation Infrastructure
%{?python_provide:%python_provide python3-zope-deprecation}

%description -n python3-zope-deprecation
This package provides a simple function called 'deprecated(names, reason)' to
deprecate the previously mentioned Python objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

# Allow newer setuptools
sed -i 's/"setuptools .*"/"setuptools"/' pyproject.toml
sed -i 's/setuptools <=.*/setuptools/'  tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zope

%check
%tox

%files -n python3-zope-deprecation -f %{pyproject_files}
%doc README.rst LICENSE.txt
%{python3_sitelib}/zope.deprecation-5.1-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
