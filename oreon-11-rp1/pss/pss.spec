%global source0_hash d3896c0fc05cb08105f47d7b9f58dcffc72a87fe466effafe58baec1bcb0b021

Name:           pss
Version:        1.40
Release:        39%{?dist}
Summary:        A power-tool for searching inside source code files

# psslib/colorama is BSD-3-Clause
License:        Unlicense AND BSD-3-Clause
URL:            https://github.com/eliben/pss
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  python3-devel, python3-setuptools
BuildArch:      noarch

%description
pss is a power-tool for searching inside source code files. 
pss searches recursively within a directory tree, knows which 
extensions and file names to search and which to ignore, automatically 
skips directories you wouldn't want to search in (for example .svn or .git),
colors its output in a helpful way, and does much more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1  --root $RPM_BUILD_ROOT
#rm $RPM_BUILD_ROOT/usr/bin/pss.py

%files
%doc README.rst LICENSE CHANGES
%{_bindir}/pss
%{python3_sitelib}/pss*

%changelog
%autochangelog
