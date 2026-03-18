Name:           python-sphinxcontrib-jquery
Version:        4.1
Release:        15%{?dist}
Summary:        Extension to include jQuery on newer Sphinx releases

# The project is 0BSD
# _sphinx_javascript_frameworks_compat.js is BSD-2-Clause
# jquery-3.6.0.js and jquery.js are MIT
License:        0BSD AND BSD-2-Clause AND MIT
URL:            https://github.com/sphinx-contrib/jquery/
Source:         %{url}/archive/v%{version}/sphinxcontrib-jquery-%{version}.tar.gz

# Make the tests pass with Sphinx 7.1+
# Based on the original work in https://github.com/sphinx-contrib/jquery/pull/26
Patch:          Fix-tests-failures-with-Sphinx-7.2.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
sphinxcontrib-jquery is a Sphinx extension that ensures that jQuery
is always installed for use in Sphinx themes or extensions.}


%description %_description

%package -n     python3-sphinxcontrib-jquery
Summary:        %{summary}

%description -n python3-sphinxcontrib-jquery %_description


%prep
%autosetup -p1 -n jquery-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'sphinxcontrib*'


%check
%pytest


%files -n python3-sphinxcontrib-jquery -f %{pyproject_files}
%doc README.rst
%license LICENCE


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1-15
- Prepare for Oreon 11 (RP1)
