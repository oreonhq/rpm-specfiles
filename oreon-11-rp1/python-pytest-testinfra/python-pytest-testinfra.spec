%global source0_hash 537fd5eb88da618c1f461248aa20594cf8d44512e8519b239837e83875e1e9cd
Name:           python-pytest-testinfra
Version:        10.2.2
Release:        1%{?dist}
Summary:        Unit testing for config-managed server state
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-testinfra
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_testinfra/pytest_testinfra-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-testinfra = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-testinfra+ansible
Summary:        Metapackage for python3-pytest-testinfra ansible extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[ansible]) = %{version}-%{release}

%description -n python3-pytest-testinfra+ansible
Metapackage for python3-pytest-testinfra ansible extras.

%package -n       python3-pytest-testinfra+paramiko
Summary:        Metapackage for python3-pytest-testinfra paramiko extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[paramiko]) = %{version}-%{release}

%description -n python3-pytest-testinfra+paramiko
Metapackage for python3-pytest-testinfra paramiko extras.

%package -n       python3-pytest-testinfra+salt
Summary:        Metapackage for python3-pytest-testinfra salt extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[salt]) = %{version}-%{release}

%description -n python3-pytest-testinfra+salt
Metapackage for python3-pytest-testinfra salt extras.

%package -n       python3-pytest-testinfra+winrm
Summary:        Metapackage for python3-pytest-testinfra winrm extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[winrm]) = %{version}-%{release}

%description -n python3-pytest-testinfra+winrm
Metapackage for python3-pytest-testinfra winrm extras.

%package -n       python3-pytest-testinfra+test
Summary:        Metapackage for python3-pytest-testinfra test extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[test]) = %{version}-%{release}

%description -n python3-pytest-testinfra+test
Metapackage for python3-pytest-testinfra test extras.

%package -n       python3-pytest-testinfra+typing
Summary:        Metapackage for python3-pytest-testinfra typing extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[typing]) = %{version}-%{release}

%description -n python3-pytest-testinfra+typing
Metapackage for python3-pytest-testinfra typing extras.

%package -n       python3-pytest-testinfra+lint
Summary:        Metapackage for python3-pytest-testinfra lint extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[lint]) = %{version}-%{release}

%description -n python3-pytest-testinfra+lint
Metapackage for python3-pytest-testinfra lint extras.

%package -n       python3-pytest-testinfra+doc
Summary:        Metapackage for python3-pytest-testinfra doc extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.1
Requires:       python3dist(sphinx) < 7.2
Requires:       python3dist(alabaster) >= 0.7.2
Provides:       python3dist(pytest-testinfra[doc]) = %{version}-%{release}

%description -n python3-pytest-testinfra+doc
Metapackage for python3-pytest-testinfra doc extras.

%package -n       python3-pytest-testinfra+dev
Summary:        Metapackage for python3-pytest-testinfra dev extras
Requires:       python3-pytest-testinfra = %{version}-%{release}
Provides:       python3dist(pytest-testinfra[dev]) = %{version}-%{release}

%description -n python3-pytest-testinfra+dev
Metapackage for python3-pytest-testinfra dev extras.

%description

%package -n     python3-pytest-testinfra
Summary:        Unit testing for config-managed server state
Suggests:       python3-pytest-testinfra+ansible
Suggests:       python3-pytest-testinfra+paramiko
Suggests:       python3-pytest-testinfra+salt
Suggests:       python3-pytest-testinfra+winrm
Provides:       python3-testinfra = %{version}-%{release}
# oreon:reqs
Requires:       python3dist(pytest) >= 6
# /oreon:reqs
%description -n python3-pytest-testinfra

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_testinfra-%{version}

# types-paramiko package is not available and is not needed for build tests
sed -i '/types-paramiko/d' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-testinfra usr/lib/python3*/site-packages/pytest_testinfra* usr/lib64/python3*/site-packages/pytest_testinfra* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_testinfra* usr/lib64/python3*/site-packages/pytest_testinfra* usr/bin/*

%check

%pyproject_check_import
%tox
%files
%files -n python3-pytest-testinfra -f %{oreon_filedir}/python3-pytest-testinfra.list

%changelog

%autochangelog
