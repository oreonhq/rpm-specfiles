%global source0_hash 705236bc14fbd5682fd6744b3065224d71267b08bf9707a21c707fa1843e0561
%global srcname sen
%global sum Terminal User Interface for docker engine
%bcond_without tests
Name:           %{srcname}
Version:        0.8.1
Release:        1%{?dist}
Summary:        Terminal User Interface for docker engine
License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-%{srcname}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
Requires:       python3-sen = %{version}-%{release}
# /oreon:deps
%description
sen enables you to manage your containers and images interactively directly
from command line. Interface is similar to htop, alot or tig.

%package -n python3-%{srcname}
Requires:       python3-urwid
Requires:       python3-urwidtrees
Requires:       python3-docker
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-flexmock
BuildRequires:  python3-urwid
BuildRequires:  python3-urwidtrees
BuildRequires:  python3-docker
%endif  # tests
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
sen enables you to manage your containers and images interactively directly
from command line. Interface is similar to htop, alot or tig.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
sed -i 1d sen/cli.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/sen* usr/lib64/python3*/site-packages/sen* usr/bin/*

%check

%if %{with tests}
py.test-%{python3_version} -vv tests || :
%endif  # tests
%files
%files -n python3-sen -f %{oreon_filedir}/python3-sen.list

%changelog

%autochangelog
