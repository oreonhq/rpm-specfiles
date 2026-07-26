%global source0_hash 4e7e6fcf65bcf58e9e7ec7b278b8921f34fd7b1884ab9c7b32a91beec29412fc

%{?python_enable_dependency_generator}
%define modname pywt
%define pkgname PyWavelets

Name:           python-%{modname}
Version:        1.8.0
Release:        4%{?dist}
Summary:        PyWavelets, wavelet transform module
License:        MIT
URL:            https://pywavelets.readthedocs.io/en/latest
Source0:        https://github.com/PyWavelets/pywt/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xorg-x11-server-Xvfb

%description
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

%package doc
Summary:        Documentation for %{name}
BuildRequires:  python3-sphinx

%description doc
Documentation for %{name}.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{modname}
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

sed -i '1{\@^#!/usr/bin/env python@d}' %{modname}/tests/*.py  %{modname}/data/create_dat.py
# These are unpackaged deps and apparently not needed
sed -i -e '/jupyterlite_sphinx/d' -e '/sphinx_togglebutton/d' doc/source/conf.py
sed -i -e '/jupyterlite-pyodide-kernel/d' -e '/jupyterlite-sphinx/d' -e '/sphinx-togglebutton/d' -e '/docutils/s/<.*//' util/readthedocs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -p util/readthedocs/requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{modname}

# Doc build needs an installed version of pywt so we do it here
PYTHONPATH=%{buildroot}%{python3_sitearch} make -C doc html
# sphinx-build -b html -W --keep-going -d _build/doctrees doc/source doc/build
find -name '.buildinfo' -delete

%check
mkdir -p matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=`pwd`
pushd %{buildroot}/%{python3_sitearch}
  %py3_test_envvars xvfb-run -a %__pytest pywt/tests --verbose -p no:cacheprovider \
%ifarch ppc64le
  -k 'not test_cwt_complex and not test_cwt_method_fft and not test_accuracy_precomputed_cwt'
  # see https://github.com/PyWavelets/pywt/issues/508
%endif
# Need a line here due to continuation above
popd

%files doc
%doc doc/build/html

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
