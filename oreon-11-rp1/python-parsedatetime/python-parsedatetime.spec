%global source0_hash 0cbf3fe4dee18c88df343bc568d35fdc67774846cb4aec2b2626d1bee7a0c6c5

%global realname parsedatetime

%bcond_without tests

Name:           python-%{realname}
Version:        2.6
Release:        22%{?dist}
Summary:        Parse human-readable date/time strings in Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/bear/%{realname}
Source0:        https://github.com/bear/%{realname}/archive/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
parsedatetime is a python module that can parse human-readable date/time\
strings.

%package -n python3-%{realname}
Summary:        Parse human-readable date/time strings in Python

%description -n python3-%{realname}
parsedatetime is a python module that can parse human-readable date/time
strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{realname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{realname}
# It makes no sense to ship all these tests in the package
# just use them during the build
rm -rf %{buildroot}%{python3_sitelib}/%{realname}/tests

%check
%pyproject_check_import

%if %{with tests}
py.test-3 -x tests/*.py
%endif

%files -n python3-%{realname} -f %{pyproject_files}
%doc AUTHORS.txt CHANGES.txt README.rst

%changelog
%autochangelog
