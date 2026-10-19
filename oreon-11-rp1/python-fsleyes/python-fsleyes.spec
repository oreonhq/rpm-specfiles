%global source0_hash b4edb1ae5940bfb059cb0db14e7b619a18dbb02e2328448fc373931d750ec8e0
Name:           python-fsleyes
Version:        1.20.2
Release:        1%{?dist}
Summary:        FSLeyes, the FSL image viewer
License:        ...
URL:            https://git.fmrib.ox.ac.uk/fsl/fsleyes/fsleyes/
Source0:        https://files.pythonhosted.org/packages/source/f/fsleyes/fsleyes-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-fsleyes = %{version}-%{release}
# /oreon:deps
%package -n       python3-fsleyes+darwin
Summary:        Metapackage for python3-fsleyes darwin extras
Requires:       python3-fsleyes = %{version}-%{release}
Requires:       python3dist(appnope) == 0.1.*
Provides:       python3dist(fsleyes[darwin]) = %{version}-%{release}

%description -n python3-fsleyes+darwin
Metapackage for python3-fsleyes darwin extras.

%package -n       python3-fsleyes+extra
Summary:        Metapackage for python3-fsleyes extra extras
Requires:       python3-fsleyes = %{version}-%{release}
Requires:       python3dist(indexed-gzip) >= 0.7.0
Requires:       python3dist(ipykernel) >= 4.8
Requires:       python3dist(ipython) >= 5
Requires:       python3dist(jupyter-client) >= 5.3.1
Requires:       python3dist(pyzmq) >= 17.0
Requires:       python3dist(rtree) >= 0.8.3
Requires:       python3dist(tornado) >= 5.0
Requires:       python3dist(trimesh) >= 2.37.29
Requires:       python3dist(wxnatpy) >= 0.4.0
Requires:       python3dist(xnat) >= 0.3.3
Provides:       python3dist(fsleyes[extra]) = %{version}-%{release}

%description -n python3-fsleyes+extra
Metapackage for python3-fsleyes extra extras.

%package -n       python3-fsleyes+doc
Summary:        Metapackage for python3-fsleyes doc extras
Requires:       python3-fsleyes = %{version}-%{release}
Provides:       python3dist(fsleyes[doc]) = %{version}-%{release}

%description -n python3-fsleyes+doc
Metapackage for python3-fsleyes doc extras.

%package -n       python3-fsleyes+test
Summary:        Metapackage for python3-fsleyes test extras
Requires:       python3-fsleyes = %{version}-%{release}
Provides:       python3dist(fsleyes[test]) = %{version}-%{release}

%description -n python3-fsleyes+test
Metapackage for python3-fsleyes test extras.

%package -n       python3-fsleyes+style
Summary:        Metapackage for python3-fsleyes style extras
Requires:       python3-fsleyes = %{version}-%{release}
Provides:       python3dist(fsleyes[style]) = %{version}-%{release}

%description -n python3-fsleyes+style
Metapackage for python3-fsleyes style extras.

%description

%package -n     python3-fsleyes
Summary:        FSLeyes, the FSL image viewer
# oreon:reqs
Requires:       python3dist(fsleyes-props) >= 1.13
Requires:       python3dist(fsleyes-widgets) >= 0.17
Requires:       python3dist(fslpy) >= 3.22
Requires:       python3dist(jinja2) >= 2
Requires:       python3dist(matplotlib) >= 3.5
Requires:       python3dist(nibabel) >= 2.3
Requires:       python3dist(numpy) >= 1.14
Requires:       python3dist(pillow) >= 3.2.0
Requires:       python3dist(pyopengl) >= 3.1.0
Requires:       python3dist(pyparsing) >= 3
Requires:       python3dist(scipy) >= 0.18
Requires:       python3dist(trx-python) >= 0.4
Requires:       python3dist(wxpython) >= 4
# /oreon:reqs
%description -n python3-fsleyes

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fsleyes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fsleyes usr/lib/python3*/site-packages/fsleyes* usr/lib64/python3*/site-packages/fsleyes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fsleyes* usr/lib64/python3*/site-packages/fsleyes* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fsleyes -f %{oreon_filedir}/python3-fsleyes.list

%changelog

%autochangelog
