%global source0_hash eebe8daea8726802f6d25d16dfbb0585ab62b380447a0ec753dd8d6161c3aa7a
%global pypi_name conu
Name:           %{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        library which makes it easy to write tests for your containers
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-modularity/conu
Source0:        https://files.pythonhosted.org/packages/source/c/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    ppc64
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-docker
BuildRequires:  python3-kubernetes
BuildRequires:  python3-pyxattr
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
# /oreon:deps
%description
`conu` is a library which makes it easy to write tests for your containers
and is handy when playing with containers inside your code.
It defines an API to access and manipulate containers,
images and provides more, very helpful functions.

%package -n     python3-%{pypi_name}
Summary:        library which makes it easy to write tests for your containers
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-kubernetes
BuildRequires:  python3-docker
BuildRequires:  python3-requests
BuildRequires:  python3-pyxattr
BuildRequires:  python3-six
Requires:       python3-kubernetes
Requires:       python3-docker
Requires:       python3-requests
Requires:       python3-pyxattr
Requires:       python3-six
Recommends:     moby-engine
Recommends:     source-to-image
Recommends:     acl
Recommends:     libselinux-utils
%description -n python3-%{pypi_name}
`conu` is a library which makes it easy to write tests for your containers
and is handy when playing with containers inside your code.
It defines an API to access and manipulate containers,
images and provides more, very helpful functions.

%package -n     python3-%{pypi_name}-pytest
Summary:        fixtures which can be utilized via pytest
%{?python_provide:%python_provide python3-%{pypi_name}-pytest}
Requires:       python3-pytest
Requires:       python3-%{pypi_name}
%description -n python3-%{pypi_name}-pytest
fixtures which can be utilized via pytest

%package -n %{pypi_name}-doc
Summary:        conu documentation
BuildRequires:  python3-sphinx
%description -n %{pypi_name}-doc
Documentation for conu.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs/source html
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles python3-conu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-conu-pytest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles conu-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-conu -f %{oreon_filedir}/python3-conu.list
%files -n python3-conu-pytest -f %{oreon_filedir}/python3-conu-pytest.list
%files -n conu-doc -f %{oreon_filedir}/conu-doc.list

%changelog

%autochangelog
