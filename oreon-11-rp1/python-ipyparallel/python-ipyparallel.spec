%global source0_hash 2b31bb4e94708e7ffb4ee6501d7f5f664df7e1c4c572e91e9e0d12484c6a6910
Name:           python-ipyparallel
Version:        9.2.0
Release:        1%{?dist}
Summary:        Interactive Parallel Computing with IPython
License:        ...
URL:            https://ipython.org
Source0:        https://files.pythonhosted.org/packages/source/i/ipyparallel/ipyparallel-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 0.25
BuildRequires:  python3dist(jupyterlab) == 4.*
Requires:       python3-ipyparallel = %{version}-%{release}
# /oreon:deps
%package -n       python3-ipyparallel+nbext
Summary:        Metapackage for python3-ipyparallel nbext extras
Requires:       python3-ipyparallel = %{version}-%{release}
Provides:       python3dist(ipyparallel[nbext]) = %{version}-%{release}

%description -n python3-ipyparallel+nbext
Metapackage for python3-ipyparallel nbext extras.

%package -n       python3-ipyparallel+serverextension
Summary:        Metapackage for python3-ipyparallel serverextension extras
Requires:       python3-ipyparallel = %{version}-%{release}
Provides:       python3dist(ipyparallel[serverextension]) = %{version}-%{release}

%description -n python3-ipyparallel+serverextension
Metapackage for python3-ipyparallel serverextension extras.

%package -n       python3-ipyparallel+labextension
Summary:        Metapackage for python3-ipyparallel labextension extras
Requires:       python3-ipyparallel = %{version}-%{release}
Requires:       python3dist(jupyterlab) >= 3
Provides:       python3dist(ipyparallel[labextension]) = %{version}-%{release}

%description -n python3-ipyparallel+labextension
Metapackage for python3-ipyparallel labextension extras.

%package -n       python3-ipyparallel+retroextension
Summary:        Metapackage for python3-ipyparallel retroextension extras
Requires:       python3-ipyparallel = %{version}-%{release}
Provides:       python3dist(ipyparallel[retroextension]) = %{version}-%{release}

%description -n python3-ipyparallel+retroextension
Metapackage for python3-ipyparallel retroextension extras.

%package -n       python3-ipyparallel+benchmark
Summary:        Metapackage for python3-ipyparallel benchmark extras
Requires:       python3-ipyparallel = %{version}-%{release}
Provides:       python3dist(ipyparallel[benchmark]) = %{version}-%{release}

%description -n python3-ipyparallel+benchmark
Metapackage for python3-ipyparallel benchmark extras.

%package -n       python3-ipyparallel+test
Summary:        Metapackage for python3-ipyparallel test extras
Requires:       python3-ipyparallel = %{version}-%{release}
Provides:       python3dist(ipyparallel[test]) = %{version}-%{release}

%description -n python3-ipyparallel+test
Metapackage for python3-ipyparallel test extras.

%description

%package -n     python3-ipyparallel
Summary:        Interactive Parallel Computing with IPython
# oreon:reqs
Requires:       python3dist(ipykernel) >= 6.9.1
Requires:       python3dist(ipython) >= 5
Requires:       python3dist(jupyter-client) >= 7
Requires:       python3dist(python-dateutil) >= 2.1
Requires:       python3dist(pyzmq) >= 25
Requires:       python3dist(tornado) >= 6.1
Requires:       python3dist(traitlets) >= 5
# /oreon:reqs
%description -n python3-ipyparallel

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ipyparallel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ipyparallel usr/lib/python3*/site-packages/ipyparallel* usr/lib64/python3*/site-packages/ipyparallel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ipyparallel* usr/lib64/python3*/site-packages/ipyparallel* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ipyparallel -f %{oreon_filedir}/python3-ipyparallel.list

%changelog

%autochangelog
