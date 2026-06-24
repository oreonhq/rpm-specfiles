%global source0_hash none

%global srcname natsort

Name:           python-%{srcname}
Version:        8.4.0
Release:        10%{?dist}
Summary:        Python library that sorts lists using the "natural order" sort

License:        MIT
URL:            https://github.com/SethMMorton/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

Suggests:       python3-pyicu

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  glibc-langpack-en
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(semver)

%global _description \
Python module which provides "natural sorting".\
\
Under natural sorting, numeric sub-strings are compared numerically,\
and the other word characters are compared lexically.\
\
Example:\
unsorted:           ['a2', 'a9', 'a1', 'a4', 'a10']\
lexicographic sort: ['a1', 'a10', 'a2', 'a4', 'a9']\
natural sort:       ['a1', 'a2', 'a4', 'a9', 'a10']

%description %{_description}

%package -n python3-%{srcname}
Summary:	%{summary}
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{srcname}

%changelog
%autochangelog

