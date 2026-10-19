%global source0_hash 0863c0c4e935e6404d53317b74dfc3b58f7da14ffc97086327f1a51c7ab60062
%global srcname sane
Name:           python-%{srcname}
Version:        2.9.2
Release:        1%{?dist}
Summary:        Python SANE interface
License:        MIT
URL:            https://github.com/python-pillow/Sane
Source0:        https://github.com/python-pillow/Sane/archive/v%{version}/Sane-%{version}.tar.gz
%filter_provides_in %{python3_sitearch}
%filter_setup
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 67.8
Requires:       python3-sane = %{version}-%{release}
# /oreon:deps
%description
This package contains the sane module for Python which provides access to
various raster scanning devices such as flatbed scanners and digital cameras.

%package -n python3-%{srcname}
Summary:        Python 3 module for using scanners
Requires:       python3-pillow
Requires:       python3-numpy
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
This package contains the sane module for Python which provides access to
various raster scanning devices such as flatbed scanners and digital cameras.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Sane-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
PYTHONPATH=%{buildroot}%{python3_sitearch} make -C doc html SPHINXBUILD=sphinx-build-%python3_version
rm -f doc/_build_py3/html/.buildinfo
%oreon_autofiles main usr/lib/python3*/site-packages/sane* usr/lib64/python3*/site-packages/sane* usr/bin/*

%files
%files -n python3-sane -f %{oreon_filedir}/python3-sane.list

%changelog

%autochangelog
