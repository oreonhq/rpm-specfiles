%global source0_hash eb8998be7bec4397aa187b56a314b8999e71e25cf9f3f8d6671893a12aa7ede8
%global srcname capturer
Name:           python-%{srcname}
Version:        3.0
Release:        1%{?dist}
Summary:        Easily capture stdout/stderr of the current process and subprocesses
License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         prefer-multiprocessing-fork-start-method.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-capturer = %{version}-%{release}
# /oreon:deps
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
Summary:        Easily capture stdout/stderr of the current process and subprocesses
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
%description -n python%{python3_pkgversion}-%{srcname}
The capturer package makes it easy to capture the stdout and stderr streams of
the current process and subprocesses. Output can be relayed to the terminal in
real time but is also available to the Python program for additional processing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Don't install the tests.py
mv capturer/tests.py ./tests.py

%build

%pyproject_wheel
sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo
%install
%pyproject_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/capturer* usr/lib64/python3*/site-packages/capturer* usr/bin/*

%check

%pytest tests.py
%files
%files -n python-capturer-doc -f %{oreon_filedir}/python-capturer-doc.list
%files -n python3-capturer -f %{oreon_filedir}/python3-capturer.list

%changelog

%autochangelog
