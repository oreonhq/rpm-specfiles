%global source0_hash b98191911ff3b4144ef8ad53e776a2d0ad24bd508a905c6ce523597c40022773

%global pypi_name smartypants

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        28%{?dist}
Summary:        plug-in that easily translates ASCII punctuation characters into smart entities

License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/leohemsted/smartypants.py
Source0:        https://github.com/leohemsted/smartypants.py/archive/v2.0.1/smartypants-2.0.1.tar.gz
BuildArch:      noarch

# https://github.com/leohemsted/smartypants.py/pull/21
Patch:          0001-Fix-regexps-and-tests-for-python3.12.patch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx


%description
SmartyPants is a free web publishing plug-in for Movable
Type, Blosxom, and BBEdit that easily translates plain ASCII
punctuation characters into “smart” typographic punctuation HTML
entities.


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name}
SmartyPants is a free web publishing plug-in for Movable
Type, Blosxom, and BBEdit that easily translates plain ASCII
punctuation characters into “smart” typographic punctuation HTML
entities.


%package -n python-%{pypi_name}-doc
Summary:        python-smartypants documentation
%description -n python-%{pypi_name}-doc
Documentation for python-smartypants


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1 -n %{pypi_name}.py-%{version}
# This is automatically on scripts in %%{_bindir}, but the tests run this
# script from the working directory so we need to fix it earlier.
%py3_shebang_fix smartypants


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# generate html documentation
cd docs
make html
# remove the sphinx-build leftovers
rm -rf _build/html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%{py3_test_envvars} %{python3} -m unittest discover --verbose --start-directory tests


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%doc CHANGES.rst
%{_bindir}/%{pypi_name}


%files -n python-%{pypi_name}-doc
%doc docs/_build/html
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-28
- Prepare for Oreon 11 (RP1)
