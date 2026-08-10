%global source0_hash 9f289d4a27cb94eaa4ecf91cdcdb2508ba38db655ba3f43e018f88e1750b8915
%global pypi_name wrapt

Name:           python-wrapt
Version:        2.1.2
Release:        %autorelease
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD-2-Clause
URL:            https://github.com/GrahamDumpleton/wrapt
Source:         %{url}/archive/%{version}/wrapt-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.}

%description %{common_description}

%package -n python3-wrapt
Summary:        %{summary}
Obsoletes:      python-wrapt-doc < 1.16.0-8

%description -n python3-wrapt %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n wrapt-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wrapt
rm -f '%{buildroot}%{python3_sitearch}/wrapt/_wrappers.c'
sed -r -i 's@^.*/wrapt/_wrappers\.c$@# &@' %{pyproject_files} || :

%check
ignore="${ignore-} --ignore=tests/conftest.py"
%pytest ${ignore-} -v
WRAPT_DISABLE_EXTENSIONS=true %pytest ${ignore-} -v

%files -n python3-wrapt -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
