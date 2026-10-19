%global source0_hash 13b81a4a7a33a7d6c4de85b908911c48849050fbaab596aeeceac78eaf067149
Name:           pss
Version:        1.45
Release:        1%{?dist}
Summary:        A power-tool for searching inside source code files
License:        Unlicense AND BSD-3-Clause
URL:            https://github.com/eliben/pss
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
