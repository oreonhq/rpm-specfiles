%global source0_hash 5e9072e8cdca889dac445c35c9362a22ccf758e97b00b79ff0d5a7ba3e11b618

%global pname colorspacious

Name: python-%{pname}
Version: 1.1.2
Release: 33%{?dist}
Summary: Perform colorspace conversions accurately and easily
License: MIT
URL: https://github.com/njsmith/colorspacious
Source: %url/archive/v%{version}/colorspacious-%{version}.tar.gz
Patch0: %{name}-1.1.2-sphinx.patch
Patch1: pytest.patch

# Documentation dependencies
BuildRequires: graphviz
BuildRequires: make
BuildRequires: python3-ipython
BuildRequires: python3-ipython-sphinx
BuildRequires: python3-jsonschema
BuildRequires: python3-matplotlib
BuildRequires: python3-mistune
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinxcontrib-bibtex
BuildRequires: texinfo
# Test dependency
BuildRequires: python3-pytest
# Build dependency
BuildRequires: python3-numpy
BuildArch: noarch

%global desc \
Colorspacious is a powerful, accurate, and easy-to-use library for\
performing colorspace conversions.\
\
In addition to the most common standard colorspaces (sRGB, XYZ, xyY,\
CIELab, CIELCh), we also include: color vision deficiency ("color\
blindness") simulations using the approach of Machado et al (2009);\
a complete implementation of CIECAM02; and the perceptually uniform\
CAM02-UCS / CAM02-LCD / CAM02-SCD spaces proposed by Luo et al (2006).

%description
%{desc}

%package -n python3-%{pname}
Summary: Perform colorspace conversions accurately and easily
BuildRequires: python3-devel

%description -n python3-%{pname}
%{desc}

This package contains the python3 module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pname}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd doc
PYTHONPATH=`realpath ../build/lib.linux*` make texinfo
pushd _build
pushd texinfo
makeinfo --docbook colorspacious.texi
popd
popd
popd

%install
%pyproject_install
%pyproject_save_files -l colorspacious

mkdir -p %{buildroot}%{_datadir}/help/en/colorspacious
install -m644 doc/_build/texinfo/colorspacious.xml %{buildroot}%{_datadir}/help/en/colorspacious
cp -p -r doc/_build/texinfo/colorspacious-figures %{buildroot}%{_datadir}/help/en/colorspacious/

%check
%pyproject_check_import
%pytest -v colorspacious/*.py

%files -n python3-%{pname} -f %{pyproject_files}
%doc README.rst
%dir %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/colorspacious

%changelog
%autochangelog
