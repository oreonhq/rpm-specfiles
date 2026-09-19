%global source0_hash 58f6cdceac7345e3fbce809c40079323d99033be0e5dce79f2f60de0f7d35858

# Created by pyp2rpm-3.2.1
%global srcname ndjson-testrunner
%global srcname_ ndjson_testrunner

Name:           python-%{srcname}
Version:        1.1.3
Release:        %autorelease
Summary:        A test runner that outputs newline delimited JSON results

License:        GPL-3.0-or-later
URL:            https://github.com/flying-sheep/ndjson-testrunner
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

%global _description %{expand:
A unittest TestRunner that outputs ndjson, one JSON record per test result. To
be used for test result storage or interprocess communication.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname_}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
%{py3_test_envvars} %{python3} -m unittest discover -vv -s tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
