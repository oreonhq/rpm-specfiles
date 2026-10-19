%global source0_hash 081f163d52533a286bc8249a241da5614b5dab0c06377b208980dc205e272da9
Name:           python-zarr-checksum
Version:        0.4.7
Release:        1%{?dist}
Summary:        Checksum support for zarrs stored in various backends
License:        Apache-2.0
URL:            https://github.com/dandi/zarr_checksum
Source0:        https://files.pythonhosted.org/packages/source/z/zarr_checksum/zarr_checksum-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-zarr-checksum = %{version}-%{release}
# /oreon:deps
%package -n       python3-zarr-checksum+boto
Summary:        Metapackage for python3-zarr-checksum boto extras
Requires:       python3-zarr-checksum = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.24
Provides:       python3dist(zarr-checksum[boto]) = %{version}-%{release}

%description -n python3-zarr-checksum+boto
Metapackage for python3-zarr-checksum boto extras.

%package -n       python3-zarr-checksum+test
Summary:        Metapackage for python3-zarr-checksum test extras
Requires:       python3-zarr-checksum = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.2.1
Provides:       python3dist(zarr-checksum[test]) = %{version}-%{release}

%description -n python3-zarr-checksum+test
Metapackage for python3-zarr-checksum test extras.

%package -n       python3-zarr-checksum+format
Summary:        Metapackage for python3-zarr-checksum format extras
Requires:       python3-zarr-checksum = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.11.2
Provides:       python3dist(zarr-checksum[format]) = %{version}-%{release}

%description -n python3-zarr-checksum+format
Metapackage for python3-zarr-checksum format extras.

%package -n       python3-zarr-checksum+lint
Summary:        Metapackage for python3-zarr-checksum lint extras
Requires:       python3-zarr-checksum = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.11.2
Provides:       python3dist(zarr-checksum[lint]) = %{version}-%{release}

%description -n python3-zarr-checksum+lint
Metapackage for python3-zarr-checksum lint extras.

%package -n       python3-zarr-checksum+dev
Summary:        Metapackage for python3-zarr-checksum dev extras
Requires:       python3-zarr-checksum = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.11.2
Requires:       python3dist(boto3-stubs) >= 1.24
Provides:       python3dist(zarr-checksum[dev]) = %{version}-%{release}

%description -n python3-zarr-checksum+dev
Metapackage for python3-zarr-checksum dev extras.

%description

%package -n     python3-zarr-checksum
Summary:        Checksum support for zarrs stored in various backends
# oreon:reqs
Requires:       python3dist(click) >= 8.1.8
Requires:       python3dist(tqdm) >= 4.67.1
# /oreon:reqs
%description -n python3-zarr-checksum

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zarr_checksum-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zarr-checksum usr/lib/python3*/site-packages/zarr_checksum* usr/lib64/python3*/site-packages/zarr_checksum* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zarr_checksum* usr/lib64/python3*/site-packages/zarr_checksum* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zarr-checksum -f %{oreon_filedir}/python3-zarr-checksum.list

%changelog

%autochangelog
