%global source0_hash 6bd648925ebf9ddcbc200d663d895d85eb5e54748384448996ec7f281f71fba7
Name:           python-pari-jupyter
Version:        1.4.3
Release:        1%{?dist}
Summary:        Jupyter kernel for PARI/GP
License:        GPL-3.0-or-later
URL:            https://github.com/sagemath/pari-jupyter
VCS:            git:%{url}.git
Source0:        https://github.com/sagemath/pari-jupyter/archive/%{version}/pari-jupyter-%{version}.tar.gz
Patch:          %{name}-pari.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29
Requires:       python3-pari-jupyter = %{version}-%{release}
# /oreon:deps
%description
This package contains a Jupyter kernel for PARI/GP.

%package     -n python3-pari-jupyter
Summary:        Jupyter kernel for PARI/GP
Requires:       pari-gp
Requires:       python-jupyter-filesystem
%py_provides python3-PARIKernel
%description -n python3-pari-jupyter
This package contains a Jupyter kernel for PARI/GP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pari-jupyter-%{version}
%oreon_prep
%build

%pyproject_wheel
rst2html --no-datestamp README.rst README.html
%install
%pyproject_install
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig
mv %{buildroot}%{_prefix}%{_sysconfdir}/jupyter/nbconfig/notebook.d \
   %{buildroot}%{_sysconfdir}/jupyter/nbconfig
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}
%oreon_autofiles python3-pari-jupyter usr/lib/python3*/site-packages/pari_jupyter* usr/lib64/python3*/site-packages/pari_jupyter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pari_jupyter* usr/lib64/python3*/site-packages/pari_jupyter* usr/bin/*

%check

export IPYTHONDIR=$PWD/.ipython
mkdir .ipython
ln -s %{buildroot}%{_datadir}/jupyter/kernels .ipython
ln -s %{buildroot}%{_datadir}/jupyter/nbextensions .ipython
cd test
%{py3_test_envvars} %{python3} test_pari_jupyter_kernel.py
cd -
rm -fr .ipython
%files
%files -n python3-pari-jupyter -f %{oreon_filedir}/python3-pari-jupyter.list

%changelog

%autochangelog
