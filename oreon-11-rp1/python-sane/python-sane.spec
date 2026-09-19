%global source0_hash 0863c0c4e935e6404d53317b74dfc3b58f7da14ffc97086327f1a51c7ab60062

%global srcname sane

Name:           python-%{srcname}
Version:        2.9.2
Release:        5%{?dist}
Summary:        Python SANE interface

License:        MIT
URL:            https://github.com/python-pillow/Sane
Source0:        https://github.com/python-pillow/Sane/archive/v%{version}/Sane-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  sane-backends-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%filter_provides_in %{python3_sitearch}
%filter_setup

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

%autosetup -p1 -n Sane-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sane

# Build doc in %%install so that we can use the installed sane module for generating the docs
PYTHONPATH=%{buildroot}%{python3_sitearch} make -C doc html SPHINXBUILD=sphinx-build-%python3_version
rm -f doc/_build_py3/html/.buildinfo

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst sanedoc.txt example.py doc/_build/html
%license COPYING
%{python3_sitearch}/_sane.cpython*.so

%changelog
%autochangelog
