%global source0_hash 03c881bbf23aa07bccf1b837005975993c4ab4427ba57f959afdd9d1a2386848

Name:           python-configobj
Version:        5.0.9
Release:        9%{?dist}
Summary:        Config file reading, writing, and validation
License:        BSD-3-Clause
URL:            http://configobj.readthedocs.org/
Source0:        https://pypi.python.org/packages/source/c/configobj/configobj-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
%global _description \
ConfigObj is a simple but powerful configuration file reader and writer: an ini\
file round tripper. Its main feature is that it is very easy to use, with a\
straightforward programmers interface and a simple syntax for config files. 
%description %_description

%package     -n python%{python3_pkgversion}-configobj
Summary:        %{summary}
%description -n python%{python3_pkgversion}-configobj %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n configobj-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l configobj validate

%check
%pyproject_check_import

export PYTHONPATH=$(pwd)/build/lib
%{__python3} src/tests/configobj_doctests.py
%{__python3} -m configobj.validate
%pytest -c setup.cfg --color=yes

%files -n python%{python3_pkgversion}-configobj -f %{pyproject_files}
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.9-9
- Prepare for Oreon 11 (RP1)
