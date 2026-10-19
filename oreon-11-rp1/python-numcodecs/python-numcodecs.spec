%global source0_hash e8db2e337bdafd3bb5f891a2543b53b2b36a509ce9d587af2846db3715b6c8b9
Name:           python-numcodecs
Version:        0.17.0
Release:        1%{?dist}
Summary:        A Python package providing buffer compression and transformation codecs for use in data storage and communication applications.
License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source0:        https://files.pythonhosted.org/packages/source/n/numcodecs/numcodecs-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(meson) >= 1.6.0
BuildRequires:  python3dist(meson-python) >= 0.17
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(setuptools-scm) >= 6.2
Requires:       python3-numcodecs = %{version}-%{release}
# /oreon:deps
%package -n       python3-numcodecs+msgpack
Summary:        Metapackage for python3-numcodecs msgpack extras
Requires:       python3-numcodecs = %{version}-%{release}
Provides:       python3dist(numcodecs[msgpack]) = %{version}-%{release}

%description -n python3-numcodecs+msgpack
Metapackage for python3-numcodecs msgpack extras.

%package -n       python3-numcodecs+zfpy
Summary:        Metapackage for python3-numcodecs zfpy extras
Requires:       python3-numcodecs = %{version}-%{release}
Requires:       python3dist(zfpy) >= 1.0.0
Provides:       python3dist(numcodecs[zfpy]) = %{version}-%{release}

%description -n python3-numcodecs+zfpy
Metapackage for python3-numcodecs zfpy extras.

%package -n       python3-numcodecs+pcodec
Summary:        Metapackage for python3-numcodecs pcodec extras
Requires:       python3-numcodecs = %{version}-%{release}
Requires:       python3dist(pcodec) >= 1
Requires:       python3dist(pcodec) < 2
Provides:       python3dist(numcodecs[pcodec]) = %{version}-%{release}

%description -n python3-numcodecs+pcodec
Metapackage for python3-numcodecs pcodec extras.

%package -n       python3-numcodecs+crc32c
Summary:        Metapackage for python3-numcodecs crc32c extras
Requires:       python3-numcodecs = %{version}-%{release}
Requires:       python3dist(crc32c) >= 2.7
Provides:       python3dist(numcodecs[crc32c]) = %{version}-%{release}

%description -n python3-numcodecs+crc32c
Metapackage for python3-numcodecs crc32c extras.

%package -n       python3-numcodecs+google_crc32c
Summary:        Metapackage for python3-numcodecs google_crc32c extras
Requires:       python3-numcodecs = %{version}-%{release}
Requires:       python3dist(google-crc32c) >= 1.5
Provides:       python3dist(numcodecs[google_crc32c]) = %{version}-%{release}

%description -n python3-numcodecs+google_crc32c
Metapackage for python3-numcodecs google_crc32c extras.

%package -n       python3-numcodecs+docs
Summary:        Metapackage for python3-numcodecs docs extras
Requires:       python3-numcodecs = %{version}-%{release}
Provides:       python3dist(numcodecs[docs]) = %{version}-%{release}

%description -n python3-numcodecs+docs
Metapackage for python3-numcodecs docs extras.

%package -n       python3-numcodecs+test
Summary:        Metapackage for python3-numcodecs test extras
Requires:       python3-numcodecs = %{version}-%{release}
Provides:       python3dist(numcodecs[test]) = %{version}-%{release}

%description -n python3-numcodecs+test
Metapackage for python3-numcodecs test extras.

%package -n       python3-numcodecs+test_extras
Summary:        Metapackage for python3-numcodecs test_extras extras
Requires:       python3-numcodecs = %{version}-%{release}
Provides:       python3dist(numcodecs[test_extras]) = %{version}-%{release}

%description -n python3-numcodecs+test_extras
Metapackage for python3-numcodecs test_extras extras.

%description

%package -n     python3-numcodecs
Summary:        A Python package providing buffer compression and transformation codecs for use in data storage and communication applications.
# oreon:reqs
Requires:       python3dist(numpy) >= 2.0
# /oreon:reqs
%description -n python3-numcodecs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir numcodecs-%{version}
%oreon_prep
%build

%pyproject_wheel -Csetup-args=-Dsystem_blosc=enabled -Csetup-args=-Dsystem_zstd=enabled -Csetup-args=-Dsystem_lz4=enabled
%install
%pyproject_install
%oreon_autofiles python3-numcodecs usr/lib/python3*/site-packages/numcodecs* usr/lib64/python3*/site-packages/numcodecs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/numcodecs* usr/lib64/python3*/site-packages/numcodecs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-numcodecs -f %{oreon_filedir}/python3-numcodecs.list

%changelog

%autochangelog
