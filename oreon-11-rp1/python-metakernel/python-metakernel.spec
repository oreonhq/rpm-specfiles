%global source0_hash 86333959451a241266f728a92fdf2f42eeb1033f0f11d5953cc04b95487308bb

Name:		python-metakernel
#		The python and echo subpackages have their own version
#		and release numbers - update below in each package section
#		Running rpmdev-bumpspec on this specfile will update all the
#		release tags automatically
Version:	0.32.0
Release:	1%{?dist}
%global pkgversion %{version}
%global pkgrelease %{release}
Summary:	Metakernel for Jupyter

License:	BSD-3-Clause
URL:		https://github.com/Calysto/metakernel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#		https://github.com/Calysto/metakernel/pull/356
Patch0:		0001-Clear-PS0-in-bash-REPL-wrapper.patch
BuildArch:	noarch

#		For testing:
BuildRequires:	python3dist(ipywidgets)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pytest-timeout)
BuildRequires:	python3dist(requests)
BuildRequires:	python3dist(ipyparallel)
BuildRequires:	python3dist(matplotlib)
BuildRequires:	python3dist(portalocker)
BuildRequires:	python3dist(pydot)
BuildRequires:	man
#		For documentation
BuildRequires:	make
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(sphinx-bootstrap-theme)
BuildRequires:	python3dist(myst-parser)
BuildRequires:	python3dist(numpydoc)
BuildRequires:	python3dist(recommonmark)

%description
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package -n python3-metakernel
Summary:	Metakernel for Jupyter
%py_provides	python3-metakernel
Obsoletes:	python3-metakernel-bash < 0.19.1-24
Obsoletes:	python3-metakernel-tests < 0.29.3-2
Obsoletes:	python3-metakernel+test < 0.31.0

%description -n python3-metakernel
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package doc
Summary:	Documentation for python-metakernel

%description doc
This package contains the documentation of python-metakernel.

%package -n python3-metakernel-python
Version:	0.19.1
Release:	82%{?dist}
Summary:	A Python kernel for Jupyter/IPython
%py_provides	python3-metakernel-python
Requires:	python3-metakernel = %{pkgversion}-%{pkgrelease}
Requires:	python-jupyter-filesystem

%description -n python3-metakernel-python
A Python kernel for Jupyter/IPython, based on MetaKernel.

%package -n python3-metakernel-echo
Version:	0.19.1
Release:	82%{?dist}
Summary:	A simple echo kernel for Jupyter/IPython
%py_provides	python3-metakernel-echo
Requires:	python3-metakernel = %{pkgversion}-%{pkgrelease}
Requires:	python-jupyter-filesystem

%description -n python3-metakernel-echo
A simple echo kernel for Jupyter/IPython, based on MetaKernel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n metakernel-%{pkgversion}
%patch -P0 -p1
# Allow older pytest versions
sed -e /minversion/d -e /strict/d -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd metakernel_python
%pyproject_wheel
popd

pushd metakernel_echo
%pyproject_wheel
popd

pushd docs
PYTHONPATH=.. make html
rm -f _build/html/.buildinfo
popd

%install
%pyproject_install
rm %{buildroot}%{python3_sitelib}/metakernel/magics/README.md

%check
# The completion magic test checks for the existence of ~/.bashrc
touch ~/.bashrc
PYTHONPATH=.:metakernel_python ipcluster start -n 3 --location localhost &
pid=$!
pytest -v --color=no
ipcluster stop
wait $pid

%files -n python3-metakernel
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/metakernel-*.*-info
%{python3_sitelib}/metakernel

%files doc
%license LICENSE.txt
%doc docs/_build/html

%files -n python3-metakernel-python
%{python3_sitelib}/metakernel_python-*.*-info
%{python3_sitelib}/metakernel_python
%{_datadir}/jupyter/kernels/metakernel_python

%files -n python3-metakernel-echo
%{python3_sitelib}/metakernel_echo-*.*-info
%{python3_sitelib}/metakernel_echo
%{_datadir}/jupyter/kernels/metakernel_echo

%changelog
%autochangelog
