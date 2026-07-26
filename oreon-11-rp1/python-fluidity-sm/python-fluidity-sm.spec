%global source0_hash b578e9fb4e8f728102357764b19e2b4ea4a926b357ccb657805c8ba4ef1ec997

Name:		python-fluidity-sm
Version:	0.2.0
Release:	42%{?dist}
Summary:	State machine implementation for Python objects
License:	MIT
URL:		https://github.com/nsi-iff/fluidity
Source0:	https://github.com/nsi-iff/fluidity/archive/%{version}/fluidity-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
# For test suite
BuildRequires:	python3-should_dsl

%description
State machine implementation for Python objects.

%package -n python3-fluidity-sm
Summary:	State machine implementation for Python objects

%description -n python3-fluidity-sm
State machine implementation for Python objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fluidity-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{py3_test_envvars} %{python3} -m unittest spec/*.py

%files -n python3-fluidity-sm
%license LICENSE
%doc CHANGELOG README.rst
%{python3_sitelib}/fluidity/
%{python3_sitelib}/fluidity_sm-%{version}.dist-info/

%changelog
%autochangelog
