%global source0_hash 05cf4f8dfefe995d09078cd3d747c8f04dcf17d6004fc7bb542049a55f2238d9
Name:           python-libgravatar
Version:        1.0.4
Release:        1%{?dist}
Summary:        Python interface for the Gravatar APIs
License:        GPL-3.0-or-later
URL:            https://github.com/pabluk/libgravatar
BuildArch:      noarch
Source0:        https://files.pythonhosted.org/packages/source/l/libgravatar/libgravatar-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libgravatar = %{version}-%{release}
# /oreon:deps
%description
Python interface for the Gravatar API.

%package -n python3-libgravatar
Summary:        Python 3 interface for the Gravatar API
%description -n python3-libgravatar
Python 3 interface for the Gravatar API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libgravatar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-libgravatar usr/lib/python3*/site-packages/libgravatar* usr/lib64/python3*/site-packages/libgravatar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libgravatar* usr/lib64/python3*/site-packages/libgravatar* usr/bin/*

%check

%py3_check_import libgravatar
%files
%files -n python3-libgravatar -f %{oreon_filedir}/python3-libgravatar.list

%changelog

%autochangelog
