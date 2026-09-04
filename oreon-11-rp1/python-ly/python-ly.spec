%global source0_hash 18ef058b4d0fa235768b6669041174370f553d6c84eb7a4495f95bb315e0f18a

Name:           python-ly
Version:        0.9.10
Release:        1%{?dist}
Summary:        Tool and library for manipulating LilyPond files

License:        GPL-2.0-or-later
URL:            https://pypi.python.org/pypi/python-ly
Source0:        https://pypi.python.org/packages/source/p/python-ly/python_ly-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: python3-devel

%global _description\
This package provides a Python library ly containing various Python modules\
to parse, manipulate or create documents in LilyPond format. A command line\
program ly is also provided that can be used to do various manipulations\
with LilyPond files.

%description %_description

%package -n python3-ly
Summary:        Tool and library for manipulating LilyPond files
Requires:       python3-setuptools
Requires:       python3-tkinter

%description -n python3-ly
This package provides a Python library ly containing various Python modules
to parse, manipulate or create documents in LilyPond format. A command line
program ly is also provided that can be used to do various manipulations
with LilyPond files.

This package allows for use of python-ly with Python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn python_ly-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*'

%files -n python3-ly -f %{pyproject_files}
%doc CHANGELOG.md README.rst
%{_bindir}/ly
%{_bindir}/ly-server

%changelog
%autochangelog
