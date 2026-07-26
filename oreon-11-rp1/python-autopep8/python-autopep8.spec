%global source0_hash 89440a4f969197b69a995e4ce0661b031f455a9f776d2c5ba3dbd83466931758

%global pypi_name autopep8
%global py3_name python3-%{pypi_name}

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        %autorelease
Summary:        Automatically formats Python code to conform to the PEP 8 style guide

License:        MIT
URL:            http://pypi.python.org/pypi/autopep8
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	pyproject-rpm-macros

%py_provides python3-%{pypi_name}

%description
The package autopep8 automatically formats Python code to conform to the PEP 8 
style guide. It uses the pycodestyle utility to determine what parts of the 
code needs to be formatted. autopep8 is capable of fixing most of the 
formatting issues that can be reported by pycodestyle.

%package -n %{py3_name}
Summary:        The package autopep8 formats Python code based on the output of the pep8 utility

%description -n %{py3_name}
autopep8 formats Python code based on the output of the pep8 utility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n autopep8-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

pushd %{buildroot}%{_bindir}
ln -s %{pypi_name} %{pypi_name}-3
ln -s %{pypi_name} %{pypi_name}-%{python3_version}	
popd

%check
%pytest -v -k "not (SystemTests or CommandLineTests or ExperimentalSystemTests)"

%files -n %{py3_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-3
%{_bindir}/%{pypi_name}-%{python3_version}

%changelog
%autochangelog
