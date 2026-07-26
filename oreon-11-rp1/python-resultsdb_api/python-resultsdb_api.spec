%global source0_hash 064ff845dfab78ecbc678a52fc3572b51f5578f53aedeb2738e83b71b3a36145

Name:           python-resultsdb_api
# NOTE: if you update version, *make sure* to also update `setup.py`
Version:        2.1.5
Release:        21%{?dist}
Summary:        Interface api to ResultsDB

License:        GPL-2.0-or-later
URL:            https://pagure.io/taskotron/resultsdb_api
Source0:        https://qa.fedoraproject.org/releases/resultsdb_api/resultsdb_api-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Interface api to ResultsDB

%package -n python3-resultsdb_api
Summary: %summary
Requires:       python3-simplejson
Requires:       python3-requests

%description -n python3-resultsdb_api
Python3 interface to resultsdb.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n resultsdb_api-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files resultsdb_api

%check
%pytest

%files -n python3-resultsdb_api -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
