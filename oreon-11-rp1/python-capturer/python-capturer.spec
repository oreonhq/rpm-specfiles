%global source0_hash eb8998be7bec4397aa187b56a314b8999e71e25cf9f3f8d6671893a12aa7ede8

%global srcname capturer

Name:           python-%{srcname}
Version:        3.0
Release:        23%{?dist}
Summary:        Easily capture stdout/stderr of the current process and subprocesses

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Submitted upstream as xolox/python-capturer#16
Patch0:         prefer-multiprocessing-fork-start-method.patch

BuildArch:      noarch

%description
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.

%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Don't install the tests.py
mv capturer/tests.py ./tests.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l capturer

%check
%pytest tests.py

%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
