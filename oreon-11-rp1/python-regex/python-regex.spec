%global source0_hash a729e47d418ea11d03469f321aaf67cdee8954cde3ff2cf8403ab87951ad10f2

%global srcname regex

Name:           python-%{srcname}
Version:        2026.2.28
Release:        %autorelease
Summary:        Alternative regular expression module, to replace re
# see also https://code.google.com/p/mrab-regex-hg/issues/detail?id=124
# Automatically converted from old format: Python and CNRI - review is highly recommended.
License:        LicenseRef-Callaway-Python AND CNRI-Python
URL:            https://bitbucket.org/mrabarnett/mrab-regex
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  gcc
# needed for processing README.rst
BuildRequires:  /usr/bin/rst2html
BuildRequires:  python3-pygments

%global _description %{expand:
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# rebuild the HTML doc
rst2html docs/UnicodeProperties.rst > docs/UnicodeProperties.html
rst2html README.rst > README.html

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.html
%doc docs/Features.html
%doc docs/UnicodeProperties.html

%changelog
%autochangelog
