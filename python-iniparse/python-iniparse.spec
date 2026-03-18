# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Name:           python-iniparse
Version:        0.5.1
Release:        7%{?dist}
Summary:        Accessing and Modifying INI files

# From LICENSE:
#   iniparse/compat.py and tests/test_compat.py contain code derived from
#   lib/python-2.3/ConfigParser.py and lib/python-2.3/test/test_cfgparse.py
#   respectively.  Other code may contain small snippets from those two files
#   as well.  The Python license (LICENSE-PSF) applies to that code.
License:        MIT AND Python-2.0.1
URL:            https://github.com/candlepin/python-iniparse
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Python 3.14 support: Avoid the multiprocessing forkserver method
Patch:          https://github.com/candlepin/python-iniparse/pull/38.patch

BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  python3-test

%global _description %{expand: \
iniparse is an INI parser for Python which is API compatible with the standard
library’s ConfigParser, preserves structure of INI files (order of sections &
options, indentation, comments, and blank lines are preserved when data is
updated), and is more convenient to use.}

%description
%{_description}

%package -n python3-iniparse
Summary:        %{summary}

%description -n python3-iniparse
%{_description}

%prep
%autosetup -p1
chmod -c -x html/index.html

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -vfr %{buildroot}%{_docdir}/*
%pyproject_save_files iniparse

%check
%{py3_test_envvars} %{python3} ./runtests.py

%files -n python3-iniparse -f %{pyproject_files}
# pyproject_files handles both license files; verify with “rpm -qL -p …”
%doc README.md Changelog html/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.1-7
- Prepare for Oreon 11 (RP1)
