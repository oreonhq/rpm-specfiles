%global source0_hash 47dd0d0ebdf834b0cc5d1fdbe6b73d718549cffa489e47f68f638a4add20b65d
Name:           python-hdmf
Version:        6.2.0
Release:        1%{?dist}
Summary:        A hierarchical data modeling framework for modern science data standards
License:        BSD-3-Clause
URL:            https://github.com/hdmf-dev/hdmf
Source0:        https://files.pythonhosted.org/packages/source/h/hdmf/hdmf-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hdmf = %{version}-%{release}
# /oreon:deps
%package -n       python3-hdmf+tqdm
Summary:        Metapackage for python3-hdmf tqdm extras
Requires:       python3-hdmf = %{version}-%{release}
Requires:       python3dist(tqdm) >= 4.41.0
Provides:       python3dist(hdmf[tqdm]) = %{version}-%{release}

%description -n python3-hdmf+tqdm
Metapackage for python3-hdmf tqdm extras.

%package -n       python3-hdmf+zarr
Summary:        Metapackage for python3-hdmf zarr extras
Requires:       python3-hdmf = %{version}-%{release}
Requires:       python3dist(zarr) >= 2.12.0
Requires:       python3dist(zarr) < 3
Requires:       python3dist(numcodecs) < 0.16.0
Requires:       python3dist(hdmf-zarr) >= 0.12.0
Provides:       python3dist(hdmf[zarr]) = %{version}-%{release}

%description -n python3-hdmf+zarr
Metapackage for python3-hdmf zarr extras.

%package -n       python3-hdmf+sparse
Summary:        Metapackage for python3-hdmf sparse extras
Requires:       python3-hdmf = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.7.2
Provides:       python3dist(hdmf[sparse]) = %{version}-%{release}

%description -n python3-hdmf+sparse
Metapackage for python3-hdmf sparse extras.

%package -n       python3-hdmf+termset
Summary:        Metapackage for python3-hdmf termset extras
Requires:       python3-hdmf = %{version}-%{release}
Requires:       python3dist(linkml-runtime) >= 1.5.5
Requires:       python3dist(schemasheets) >= 0.4.0rc1
Requires:       python3dist(oaklib) >= 0.5.12
Requires:       python3dist(pyyaml) >= 6.0.1
Provides:       python3dist(hdmf[termset]) = %{version}-%{release}

%description -n python3-hdmf+termset
Metapackage for python3-hdmf termset extras.

%package -n       python3-hdmf+all
Summary:        Metapackage for python3-hdmf all extras
Requires:       python3-hdmf = %{version}-%{release}
Provides:       python3dist(hdmf[all]) = %{version}-%{release}

%description -n python3-hdmf+all
Metapackage for python3-hdmf all extras.

%description

%package -n     python3-hdmf
Summary:        A hierarchical data modeling framework for modern science data standards
# oreon:reqs
Requires:       python3dist(h5py) >= 3.6.0
Requires:       python3dist(jsonschema) >= 3.2.0
Requires:       python3dist(numpy) >= 1.22.0
Requires:       python3dist(pandas) >= 1.4.0
Requires:       python3dist(ruamel.yaml) >= 0.16
# /oreon:reqs
%description -n python3-hdmf

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir hdmf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hdmf usr/lib/python3*/site-packages/hdmf* usr/lib64/python3*/site-packages/hdmf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hdmf* usr/lib64/python3*/site-packages/hdmf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hdmf -f %{oreon_filedir}/python3-hdmf.list

%changelog

%autochangelog
