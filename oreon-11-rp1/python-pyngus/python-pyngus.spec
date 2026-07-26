%global source0_hash 08cccdfb892dafe825e22c0d1740f7c0848910c3398b3a0f01f29a92ffe97998

%global srcname pyngus
%global commit 60b6f102e4dc2d976292aa974866c4acce492e27
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20200513

Name:          python-%{srcname}
# Uses the snapshot because the upstream does not provides the latest version from git.
# Please see: https://github.com/kgiusti/pyngus/issues/14
Version:       2.3.0^%{snapshotdate}git%{shortcommit}
Release:       12.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:       Callback API implemented over Proton

License:       Apache-2.0
URL:           https://github.com/kgiusti/%{srcname}
# Uses the commit because the upstream does not provides the latest version from git.
# Please see: https://github.com/kgiusti/pyngus/issues/14
Source:  https://github.com/kgiusti/pyngus/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz 

BuildArch:     noarch
BuildRequires: python3-devel
# Please see: https://bugzilla.redhat.com/show_bug.cgi?id=2245641
BuildRequires: python3dist(legacy-cgi)

# Explicitly requires.
Requires: python3dist(qpid-proton)

%global _description \
A connection oriented messaging framework using QPID Proton.\
It provides a callback-based API for message passing.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit} 

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%py3_shebang_fix setup.py
%pyproject_install
%py3_shebang_fix tests/test-runner tests/perf-test.py setup.py examples/perf-tool.py examples/rpc-server.py examples/server.py examples/send.py examples/recv.py examples/rpc-client.py

%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%py3_test_envvars PYTHONPATH=%{buildroot}:%{buildroot}/tests
PYTHONPATH=.:tests tests/test-runner -i "unit_tests.connection.CyrusTest.test_cyrus_sasl_ok" -i "unit_tests.connection.CyrusTest.test_cyrus_sasl_fail"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
