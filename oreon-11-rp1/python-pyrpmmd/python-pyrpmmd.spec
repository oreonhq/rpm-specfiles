%global source0_hash 5c3ba481aa5e3027d0e54b2814302de717b2af4eed6da96a56f6960051b44b2b

%global srcname pyrpmmd

%global sum Python module for reading rpm-md repo data

%global desc \
pyrpmmd is an independent Python module for reading \
rpm-md repository metadata. The code is derived from \
the repomd parsing code from Yum.

Name:           python-%{srcname}
Version:        0.1.1
Release:        33%{?dist}
Summary:        %{sum}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/%{srcname}
Source0:        https://releases.pagure.org/%{srcname}/%{srcname}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description %{desc}

%package     -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-six

%description -n python3-%{srcname} %{desc}

This package provides the Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README.md ChangeLog
%{python3_sitelib}/rpmmd/
%{python3_sitelib}/%{srcname}-%{version}*/

%changelog
%autochangelog
