%global source0_hash c803c40f4cf860b49dea58ee3e1c33cb9c790520e233537e1340049f89b82a88
Name:           python-fsspec
Version:        2026.7.0
Release:        1%{?dist}
Summary:        File-system specification
License:        BSD-3-Clause
URL:            https://github.com/fsspec/filesystem_spec
Source0:        https://files.pythonhosted.org/packages/source/f/fsspec/fsspec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-fsspec = %{version}-%{release}
# /oreon:deps
%package -n       python3-fsspec+abfs
Summary:        Metapackage for python3-fsspec abfs extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[abfs]) = %{version}-%{release}

%description -n python3-fsspec+abfs
Metapackage for python3-fsspec abfs extras.

%package -n       python3-fsspec+adl
Summary:        Metapackage for python3-fsspec adl extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[adl]) = %{version}-%{release}

%description -n python3-fsspec+adl
Metapackage for python3-fsspec adl extras.

%package -n       python3-fsspec+arrow
Summary:        Metapackage for python3-fsspec arrow extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(pyarrow) >= 1
Provides:       python3dist(fsspec[arrow]) = %{version}-%{release}

%description -n python3-fsspec+arrow
Metapackage for python3-fsspec arrow extras.

%package -n       python3-fsspec+dask
Summary:        Metapackage for python3-fsspec dask extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[dask]) = %{version}-%{release}

%description -n python3-fsspec+dask
Metapackage for python3-fsspec dask extras.

%package -n       python3-fsspec+dropbox
Summary:        Metapackage for python3-fsspec dropbox extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[dropbox]) = %{version}-%{release}

%description -n python3-fsspec+dropbox
Metapackage for python3-fsspec dropbox extras.

%package -n       python3-fsspec+entrypoints
Summary:        Metapackage for python3-fsspec entrypoints extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[entrypoints]) = %{version}-%{release}

%description -n python3-fsspec+entrypoints
Metapackage for python3-fsspec entrypoints extras.

%package -n       python3-fsspec+fuse
Summary:        Metapackage for python3-fsspec fuse extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[fuse]) = %{version}-%{release}

%description -n python3-fsspec+fuse
Metapackage for python3-fsspec fuse extras.

%package -n       python3-fsspec+gcs
Summary:        Metapackage for python3-fsspec gcs extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(gcsfs) >= 2026.4.0
Provides:       python3dist(fsspec[gcs]) = %{version}-%{release}

%description -n python3-fsspec+gcs
Metapackage for python3-fsspec gcs extras.

%package -n       python3-fsspec+git
Summary:        Metapackage for python3-fsspec git extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[git]) = %{version}-%{release}

%description -n python3-fsspec+git
Metapackage for python3-fsspec git extras.

%package -n       python3-fsspec+github
Summary:        Metapackage for python3-fsspec github extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[github]) = %{version}-%{release}

%description -n python3-fsspec+github
Metapackage for python3-fsspec github extras.

%package -n       python3-fsspec+gs
Summary:        Metapackage for python3-fsspec gs extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[gs]) = %{version}-%{release}

%description -n python3-fsspec+gs
Metapackage for python3-fsspec gs extras.

%package -n       python3-fsspec+gui
Summary:        Metapackage for python3-fsspec gui extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[gui]) = %{version}-%{release}

%description -n python3-fsspec+gui
Metapackage for python3-fsspec gui extras.

%package -n       python3-fsspec+hdfs
Summary:        Metapackage for python3-fsspec hdfs extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(pyarrow) >= 1
Provides:       python3dist(fsspec[hdfs]) = %{version}-%{release}

%description -n python3-fsspec+hdfs
Metapackage for python3-fsspec hdfs extras.

%package -n       python3-fsspec+http
Summary:        Metapackage for python3-fsspec http extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(aiohttp)
Provides:       python3dist(fsspec[http]) = %{version}-%{release}

%description -n python3-fsspec+http
Metapackage for python3-fsspec http extras.

%package -n       python3-fsspec+libarchive
Summary:        Metapackage for python3-fsspec libarchive extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[libarchive]) = %{version}-%{release}

%description -n python3-fsspec+libarchive
Metapackage for python3-fsspec libarchive extras.

%package -n       python3-fsspec+oci
Summary:        Metapackage for python3-fsspec oci extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[oci]) = %{version}-%{release}

%description -n python3-fsspec+oci
Metapackage for python3-fsspec oci extras.

%package -n       python3-fsspec+s3
Summary:        Metapackage for python3-fsspec s3 extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(s3fs) >= 2026.6.0
Provides:       python3dist(fsspec[s3]) = %{version}-%{release}

%description -n python3-fsspec+s3
Metapackage for python3-fsspec s3 extras.

%package -n       python3-fsspec+sftp
Summary:        Metapackage for python3-fsspec sftp extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[sftp]) = %{version}-%{release}

%description -n python3-fsspec+sftp
Metapackage for python3-fsspec sftp extras.

%package -n       python3-fsspec+smb
Summary:        Metapackage for python3-fsspec smb extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[smb]) = %{version}-%{release}

%description -n python3-fsspec+smb
Metapackage for python3-fsspec smb extras.

%package -n       python3-fsspec+ssh
Summary:        Metapackage for python3-fsspec ssh extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[ssh]) = %{version}-%{release}

%description -n python3-fsspec+ssh
Metapackage for python3-fsspec ssh extras.

%package -n       python3-fsspec+tqdm
Summary:        Metapackage for python3-fsspec tqdm extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[tqdm]) = %{version}-%{release}

%description -n python3-fsspec+tqdm
Metapackage for python3-fsspec tqdm extras.

%package -n       python3-fsspec+full
Summary:        Metapackage for python3-fsspec full extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[full]) = %{version}-%{release}

%description -n python3-fsspec+full
Metapackage for python3-fsspec full extras.

%package -n       python3-fsspec+dev
Summary:        Metapackage for python3-fsspec dev extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.5
Provides:       python3dist(fsspec[dev]) = %{version}-%{release}

%description -n python3-fsspec+dev
Metapackage for python3-fsspec dev extras.

%package -n       python3-fsspec+doc
Summary:        Metapackage for python3-fsspec doc extras
Requires:       python3-fsspec = %{version}-%{release}
Provides:       python3dist(fsspec[doc]) = %{version}-%{release}

%description -n python3-fsspec+doc
Metapackage for python3-fsspec doc extras.

%package -n       python3-fsspec+test
Summary:        Metapackage for python3-fsspec test extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(pytest-asyncio)
Provides:       python3dist(fsspec[test]) = %{version}-%{release}

%description -n python3-fsspec+test
Metapackage for python3-fsspec test extras.

%package -n       python3-fsspec+test_full
Summary:        Metapackage for python3-fsspec test_full extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(pandas) < 3.0.0
Requires:       python3dist(zarr) < 3.2.0
Provides:       python3dist(fsspec[test_full]) = %{version}-%{release}

%description -n python3-fsspec+test_full
Metapackage for python3-fsspec test_full extras.

%package -n       python3-fsspec+test_downstream
Summary:        Metapackage for python3-fsspec test_downstream extras
Requires:       python3-fsspec = %{version}-%{release}
Requires:       python3dist(moto[server]) > 4
Requires:       python3dist(moto[server]) < 5
Requires:       python3dist(aiobotocore) >= 2.5.4
Requires:       python3dist(aiobotocore) < 3.0.0
Provides:       python3dist(fsspec[test_downstream]) = %{version}-%{release}

%description -n python3-fsspec+test_downstream
Metapackage for python3-fsspec test_downstream extras.

%description

%package -n     python3-fsspec
Summary:        File-system specification
%description -n python3-fsspec

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fsspec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fsspec usr/lib/python3*/site-packages/fsspec* usr/lib64/python3*/site-packages/fsspec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fsspec* usr/lib64/python3*/site-packages/fsspec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fsspec -f %{oreon_filedir}/python3-fsspec.list

%changelog

%autochangelog
