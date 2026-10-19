%global source0_hash c1ba14b08e4a5f5c31a302b7721239695b2f0f058d125bd5ce1ee36b9d9d3c3b
%global pypi_name python-magic
%global srcname magic
Name:           %{pypi_name}
Version:        0.4.27
Release:        1%{?dist}
Summary:        File type identification using libmagic
License:        MIT
URL:            https://github.com/ahupp/python-magic
Source0:        https://files.pythonhosted.org/packages/source/%/%{pypi_name/%{pypi_name-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%package -n     python3-%{srcname}
Summary:        File type identification using libmagic
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       file-libs
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import magic
%files -f %{oreon_filedir}/main.list
%files -n python3-magic -f %{oreon_filedir}/python3-magic.list

%changelog

%autochangelog
