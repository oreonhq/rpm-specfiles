%global source0_hash 0c9285db09c8e3b66f884a0448dc2ae78737e228f69bfe9dfde1faa1d4f1c945

%global modname pypng

Name:               python-pypng
Version:            0.0.21
Release:            16%{?dist}
Summary:            Pure Python PNG image encoder/decoder

License:            MIT
URL:                http://pypi.python.org/pypi/pypng
Source0:            https://github.com/drj11/%{modname}/archive/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest

%global _description\
PyPNG allows PNG image files to be read and written using pure Python.\
\
It's available from github.com https://github.com/drj11/pypng\
\
Documentation is kindly hosted by PyPI http://pythonhosted.org/pypng/

%description %_description

%package -n python3-pypng
Summary:            Pure Python PNG image encoder/decoder
%{?python_provide:%python_provide python3-pypng}

%description -n python3-pypng
PyPNG allows PNG image files to be read and written using pure Python.

It's available from github.com https://github.com/drj11/pypng

Documentation is kindly hosted by PyPI http://pythonhosted.org/pypng/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Remove the shebang from the main lib
lib=code/png.py
sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
touch -r $lib $lib.new &&
mv $lib.new $lib

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files png*

%check
%pytest

%files -n python3-pypng -f %{pyproject_files}
%doc README.md LICENCE
%{_bindir}/prichunkpng
%{_bindir}/priditherpng
%{_bindir}/priforgepng
%{_bindir}/prigreypng
%{_bindir}/pripalpng
%{_bindir}/pripamtopng
%{_bindir}/pripnglsch
%{_bindir}/pripngtopam
%{_bindir}/priweavepng

%changelog
%autochangelog
