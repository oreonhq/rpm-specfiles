%global source0_hash 738da7dcc74817c7668d032f932598482a23cce1b061c537e54278be44d2fff8
Name:           python-gcsfs
Version:        2026.8.1
Release:        1%{?dist}
Summary:        Convenient Filesystem interface over GCS
License:        BSD-3-Clause
URL:            https://github.com/fsspec/gcsfs
Source0:        https://files.pythonhosted.org/packages/source/g/gcsfs/gcsfs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-gcsfs = %{version}-%{release}
# /oreon:deps
%package -n       python3-gcsfs+gcsfuse
Summary:        Metapackage for python3-gcsfs gcsfuse extras
Requires:       python3-gcsfs = %{version}-%{release}
Provides:       python3dist(gcsfs[gcsfuse]) = %{version}-%{release}

%description -n python3-gcsfs+gcsfuse
Metapackage for python3-gcsfs gcsfuse extras.

%package -n       python3-gcsfs+crc
Summary:        Metapackage for python3-gcsfs crc extras
Requires:       python3-gcsfs = %{version}-%{release}
Provides:       python3dist(gcsfs[crc]) = %{version}-%{release}

%description -n python3-gcsfs+crc
Metapackage for python3-gcsfs crc extras.

%package -n       python3-gcsfs+dev
Summary:        Metapackage for python3-gcsfs dev extras
Requires:       python3-gcsfs = %{version}-%{release}
Provides:       python3dist(gcsfs[dev]) = %{version}-%{release}

%description -n python3-gcsfs+dev
Metapackage for python3-gcsfs dev extras.

%description

%package -n     python3-gcsfs
Summary:        Convenient Filesystem interface over GCS
# oreon:reqs
Requires:       python3dist(aiohttp) >= 3.9.0
Requires:       python3dist(decorator) > 4.1.2
Requires:       python3dist(fsspec) >= 2026.7.0
Requires:       python3dist(google-auth) >= 1.2
Requires:       python3dist(google-cloud-storage) >= 3.11.0
# /oreon:reqs
%description -n python3-gcsfs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gcsfs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gcsfs usr/lib/python3*/site-packages/gcsfs* usr/lib64/python3*/site-packages/gcsfs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gcsfs* usr/lib64/python3*/site-packages/gcsfs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gcsfs -f %{oreon_filedir}/python3-gcsfs.list

%changelog

%autochangelog
