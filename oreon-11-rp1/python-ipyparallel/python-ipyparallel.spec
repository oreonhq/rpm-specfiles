%global source0_hash ecc81a1bfd2681eb571e361839d5defcbeec583ae3ee0503bc83b066106b88cd

Name:		python-ipyparallel
Version:	9.1.0
Release:	1%{?dist}
Summary:	Interactive Parallel Computing with IPython

License:	BSD-3-Clause
URL:		https://github.com/ipython/ipyparallel
Source0:	%pypi_source ipyparallel
BuildArch:	noarch

%description
IPython Parallel (ipyparallel) is a Python package and collection of
CLI scripts for controlling clusters of IPython processes, built on
the Jupyter protocol.

%package -n python3-ipyparallel
Summary:	Interactive Parallel Computing with IPython
%py_provides	python3-ipyparallel
Requires:	python-jupyter-filesystem >= 4.7.0-5
Obsoletes:	python-ipyparallel-doc <= 8.7.0

%description -n python3-ipyparallel
IPython Parallel (ipyparallel) is a Python package and collection of
CLI scripts for controlling clusters of IPython processes, built on
the Jupyter protocol.

%package -n python3-ipyparallel+test
Summary:	Tests for python3-ipyparallel
%py_provides	python3-ipyparallel+test
%py_provides	python3-ipyparallel-tests
Obsoletes:	python3-ipyparallel-tests < 8.4.1-3
Requires:	python3-ipyparallel = %{version}-%{release}

%description -n python3-ipyparallel+test
This package contains the tests of python3-ipyparallel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ipyparallel-%{version}

rm ipyparallel/labextension/schemas/ipyparallel-labextension/package.json.orig

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

for f in apps/iploggerapp.py cluster/app.py controller/app.py \
	 controller/heartmonitor.py engine/app.py ; do
  sed '/\/usr\/bin\/env/d' -i %{buildroot}%{python3_sitelib}/ipyparallel/${f}
  chmod -x %{buildroot}%{python3_sitelib}/ipyparallel/${f}
done

# Fix wrong install directory for configuraton files
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%check
%pytest -v --color=no

%files -n python3-ipyparallel
%license COPYING.md
%doc README.md
%{python3_sitelib}/ipyparallel-*.*-info
%dir %{python3_sitelib}/ipyparallel
%{python3_sitelib}/ipyparallel/*.py
%{python3_sitelib}/ipyparallel/__pycache__
%{python3_sitelib}/ipyparallel/apps
%{python3_sitelib}/ipyparallel/client
%{python3_sitelib}/ipyparallel/cluster
%{python3_sitelib}/ipyparallel/controller
%{python3_sitelib}/ipyparallel/engine
%{python3_sitelib}/ipyparallel/labextension
%{python3_sitelib}/ipyparallel/nbextension
%{python3_sitelib}/ipyparallel/serialize
%{_bindir}/ipcluster
%{_bindir}/ipcontroller
%{_bindir}/ipengine
%{_datadir}/jupyter/labextensions/ipyparallel-labextension
%{_datadir}/jupyter/nbextensions/ipyparallel
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/ipyparallel.json
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/ipyparallel.json
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/tree.d/ipyparallel.json

%files -n python3-ipyparallel+test
%ghost %{python3_sitelib}/ipyparallel-*.*-info
%{python3_sitelib}/ipyparallel/tests

%changelog
%autochangelog
