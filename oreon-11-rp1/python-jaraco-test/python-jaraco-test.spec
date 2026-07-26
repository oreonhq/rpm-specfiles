%global source0_hash f9fb6e3f1c3410958fc57134fc0f25152eb28e3c0116ffdc7a383e5939b6367a

Name:           python-jaraco-test
Version:        5.6.0
Release:        %autorelease
Summary:        Testing support by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.test
Source:         %{pypi_source jaraco_test}

BuildArch:      noarch
BuildRequires:  python3-devel
# needs test module which is part of python stdlib
BuildRequires:  python3-test

%global _description %{expand:
Testing support by jaraco.}

%description %_description

%package -n     python3-jaraco-test
Summary:        %{summary}
Requires:       python3-test

%description -n python3-jaraco-test %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jaraco_test-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jaraco

%check
%{py3_test_envvars} %{python3} -m pytest -v

%files -n python3-jaraco-test -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
