%global source0_hash a8e5a1cc9461322be76cee9bd91fd546d64bbb2fd78dce8acaea9c424ade0db2
Summary:        Grep-like tool for source code
Name:          grin
Version:       1.3.0
Release:        1%{?dist}
License:       LicenseRef-Callaway-BSD
URL:           http://pypi.python.org/pypi/grin
Source0:        https://files.pythonhosted.org/packages/source/g/grin/grin-%{version}.tar.gz
Requires:      python3-setuptools
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-grin = %{version}-%{release}
# /oreon:deps
%description
grin is a similar in function to GNU grep, however it is has modified
behaviour to make it simpler to use when grepping source code.

Some features grin feature are:

  * recurse directories by default
  * do not go into directories with specified names
  * do not search files with specified extensions
  * be able to show context lines before and after matched lines
  * Python regex syntax
  * unless suppressed via a command line option, display the filename 
    regardless of the number of files
  * accept a file (or stdin) with a list of newline-separated filenames
  * grep through gzipped text files
  * be useful as a library to build custom tools quickly

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i -e '1d' grin.py

%build

%{pyproject_wheel}
%install
%{pyproject_install}
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
