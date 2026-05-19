%global modname ply

%bcond_without tests

Name:           python-%{modname}
Summary:        Python Lex-Yacc
Version:        3.11
Release:        32%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/dabeaz/ply
Source0:        %{pypi_source %{modname} %{version}}
# Fix build against Python 3.11
# https://github.com/dabeaz/ply/pull/262
Patch0:		262.patch
# Fix build against Python 3.15
# https://github.com/dabeaz/ply/pull/318
Patch1:		python-ply-py315-fix.patch
BuildArch:      noarch

%description
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system. 

%package -n python3-%{modname}
Summary:        Python Lex-Yacc
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
PLY is a straightforward lex/yacc implementation. Here is a list of its 
essential features:
* It is implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger 
  grammars.
* PLY provides most of the standard lex/yacc features including support 
  for empty productions, precedence rules, error recovery, and support 
  for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc 
  functionality. In other words, it's not a large parsing framework or a 
  component of some larger system.

Python 3 version.

%prep
%setup -n %{modname}-%{version}
%patch -P0 -p1 -b .262
%patch -P1 -p1 -b .py315
find example/ -type f -executable -exec chmod -x {} ';'
find example/ -type f -name '*.py' -exec sed -i \
  -e '1{\@^#!/usr/bin/env python@d}' -e '1{\@^#!/usr/local/bin/python@d}' \
  {} ';'
rm -rf *.egg-info
# extract license block from beginning of README.md
grep -B1000 "POSSIBILITY OF SUCH DAMAGE" README.md > LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{modname}

%if %{with tests}
%check
pushd test
  ./cleanup.sh
  %{__python3} testlex.py
  %{__python3} testyacc.py
popd
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%doc CHANGES README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.11-32
- Prepare for Oreon 11 (RP1)
