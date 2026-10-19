%global source0_hash 9d7d4243b2ebc0cfba8f61afcbde07e2fbb3fc85bfe5c9a4073f9c4d42569e1c
%global srcname fedfind
Name:           fedfind
Version:        6.1.4
Release:        1%{?dist}
Summary:        Fedora compose and image finder
License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/quality/fedfind
Source0:        https://files.pythonhosted.org/packages/source/f/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-fedfind
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-fedfind = %{version}-%{release}
# /oreon:deps
%description
Fedora Finder finds Fedora. For now, that means it finds Fedora images
- for stable releases, milestone pre-releases, candidate composes, and
nightly composes. The fedfind package provides a simple CLI for showing
image URLs.

%package -n python%{python3_pkgversion}-fedfind
Summary:        Fedora Finder finds Fedora (using Python 3)
%{?python_provide:%python_provide python%{python3_pkgversion}-fedfind}
%description -n python%{python3_pkgversion}-fedfind
Fedora Finder finds Fedora. For now, that means it finds Fedora images
- for stable releases, milestone pre-releases, candidate composes, and
nightly composes. The fedfind library provides a handy interface for
interacting with Fedora composes and discovering various properties of
them, along with some miscellaneous helper functions. This is the
Python 3 library package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# setuptools-scm is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-scm"..g' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/fedfind* usr/lib64/python3*/site-packages/fedfind* usr/bin/*

%check

%tox
%files
%files -n python3-fedfind -f %{oreon_filedir}/python3-fedfind.list

%changelog

%autochangelog
