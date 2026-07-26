%global source0_hash 6812c2db62d3fae71a4addbe5a8a0a16c97eb491f3cd63fe34b4ed7e07236f33

%global pypi_name sphinx-click

Name:           python-%{pypi_name}
Version:        5.1.0
Release:        %autorelease
Summary:        Sphinx extension that automatically documents Click applications

License:        MIT
URL:            https://github.com/click-contrib/sphinx-click
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# pytest is not an upstream dependency, we use it here out of convenience
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros

%global package_desc \
sphinx-click is a Sphinx plugin that allows you to automatically extract\
documentation from a click-based application and include it in your docs.

%description
%{package_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# The doc subpackage was removed, obsolete it to have clean upgrade path
# This was added in Fedora 35 and can be removed in Fedora 37
Obsoletes:      python-%{pypi_name}-doc < 2.7.1-1

%description -n python3-%{pypi_name}
%{package_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_click

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst ChangeLog

%changelog
%autochangelog
