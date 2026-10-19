%global source0_hash f7b04335adc473de877f5117e26d5f1142f4c9f7cd765408f0877757be5afbf4
Name:           python-daemon
Version:        3.1.2
Release:        1%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process
License:        Apache-2.0
URL:            https://pagure.io/python-daemon
Source0:        https://files.pythonhosted.org/packages/source/p/python_daemon/python_daemon-%{version}.tar.gz
Patch:          drop-dependencies-and-fix-dynamic-version.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.4.0
Requires:       python3-daemon = %{version}-%{release}
# /oreon:deps
%package -n       python3-daemon+doc
Summary:        Metapackage for python3-daemon doc extras
Requires:       python3-daemon = %{version}-%{release}
Provides:       python3dist(daemon[doc]) = %{version}-%{release}

%description -n python3-daemon+doc
Metapackage for python3-daemon doc extras.

%package -n       python3-daemon+static-analysis
Summary:        Metapackage for python3-daemon static-analysis extras
Requires:       python3-daemon = %{version}-%{release}
Requires:       python3dist(pycodestyle) >= 2.12
Requires:       python3dist(pydocstyle) >= 6.3
Requires:       python3dist(pyupgrade) >= 3.17
Requires:       python3dist(isort) >= 5.13
Provides:       python3dist(daemon[static-analysis]) = %{version}-%{release}

%description -n python3-daemon+static-analysis
Metapackage for python3-daemon static-analysis extras.

%package -n       python3-daemon+build
Summary:        Metapackage for python3-daemon build extras
Requires:       python3-daemon = %{version}-%{release}
Provides:       python3dist(daemon[build]) = %{version}-%{release}

%description -n python3-daemon+build
Metapackage for python3-daemon build extras.

%package -n       python3-daemon+test
Summary:        Metapackage for python3-daemon test extras
Requires:       python3-daemon = %{version}-%{release}
Requires:       python3dist(testscenarios) >= 0.4
Provides:       python3dist(daemon[test]) = %{version}-%{release}

%description -n python3-daemon+test
Metapackage for python3-daemon test extras.

%package -n       python3-daemon+dist
Summary:        Metapackage for python3-daemon dist extras
Requires:       python3-daemon = %{version}-%{release}
Provides:       python3dist(daemon[dist]) = %{version}-%{release}

%description -n python3-daemon+dist
Metapackage for python3-daemon dist extras.

%package -n       python3-daemon+devel
Summary:        Metapackage for python3-daemon devel extras
Requires:       python3-daemon = %{version}-%{release}
Provides:       python3dist(daemon[devel]) = %{version}-%{release}

%description -n python3-daemon+devel
Metapackage for python3-daemon devel extras.

%description

%package -n python3-daemon
Summary:        Library to implement a well-behaved Unix daemon process
# oreon:reqs
Requires:       python3dist(lockfile) >= 0.10
# /oreon:reqs
%description -n python3-daemon

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python_daemon-%{version}
# See the patch removing dependencies above
# - insert the actual version
sed -i "s/VERSION_PLACEHOLDER/%{version}/" pyproject.toml
# - setup.py is not needed, everything that remains is in pyproject.toml
# - test_setup.py tests importing of setup.py
# - test_util_* are not testing the libraty but packaging and other tools
rm setup.py test/test_setup.py test/test_util_metadata.py test/test_util_packaging.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-daemon usr/lib/python3*/site-packages/daemon* usr/lib64/python3*/site-packages/daemon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/daemon* usr/lib64/python3*/site-packages/daemon* usr/bin/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m unittest discover
%files
%files -n python3-daemon -f %{oreon_filedir}/python3-daemon.list

%changelog

%autochangelog
