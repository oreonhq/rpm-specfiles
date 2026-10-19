%global source0_hash 98210cd96c256dd9936f58e1c762aba94da7db7d38d058bb0fbaf7e4b9567146
Name:           python-elasticsearch
Version:        9.5.1
Release:        1%{?dist}
Summary:        Python client for Elasticsearch
License:        Apache-2.0
URL:            https://github.com/elastic/elasticsearch-py
Source0:        https://files.pythonhosted.org/packages/source/e/elasticsearch/elasticsearch-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-elasticsearch = %{version}-%{release}
# /oreon:deps
%package -n       python3-elasticsearch+async
Summary:        Metapackage for python3-elasticsearch async extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(aiohttp) >= 3
Requires:       python3dist(aiohttp) < 4
Provides:       python3dist(elasticsearch[async]) = %{version}-%{release}

%description -n python3-elasticsearch+async
Metapackage for python3-elasticsearch async extras.

%package -n       python3-elasticsearch+requests
Summary:        Metapackage for python3-elasticsearch requests extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(requests) >= 2.4.0
Requires:       python3dist(requests) < 3.0.0
Provides:       python3dist(elasticsearch[requests]) = %{version}-%{release}

%description -n python3-elasticsearch+requests
Metapackage for python3-elasticsearch requests extras.

%package -n       python3-elasticsearch+orjson
Summary:        Metapackage for python3-elasticsearch orjson extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(orjson) >= 3
Provides:       python3dist(elasticsearch[orjson]) = %{version}-%{release}

%description -n python3-elasticsearch+orjson
Metapackage for python3-elasticsearch orjson extras.

%package -n       python3-elasticsearch+pyarrow
Summary:        Metapackage for python3-elasticsearch pyarrow extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(pyarrow) >= 1
Provides:       python3dist(elasticsearch[pyarrow]) = %{version}-%{release}

%description -n python3-elasticsearch+pyarrow
Metapackage for python3-elasticsearch pyarrow extras.

%package -n       python3-elasticsearch+vectorstore_mmr
Summary:        Metapackage for python3-elasticsearch vectorstore_mmr extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(numpy) >= 1
Requires:       python3dist(simsimd) >= 3
Provides:       python3dist(elasticsearch[vectorstore_mmr]) = %{version}-%{release}

%description -n python3-elasticsearch+vectorstore_mmr
Metapackage for python3-elasticsearch vectorstore_mmr extras.

%package -n       python3-elasticsearch+dev
Summary:        Metapackage for python3-elasticsearch dev extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(requests) >= 2
Requires:       python3dist(requests) < 3
Requires:       python3dist(pyyaml) >= 5.4
Provides:       python3dist(elasticsearch[dev]) = %{version}-%{release}

%description -n python3-elasticsearch+dev
Metapackage for python3-elasticsearch dev extras.

%package -n       python3-elasticsearch+docs
Summary:        Metapackage for python3-elasticsearch docs extras
Requires:       python3-elasticsearch = %{version}-%{release}
Requires:       python3dist(sphinx-rtd-theme) >= 2.0
Provides:       python3dist(elasticsearch[docs]) = %{version}-%{release}

%description -n python3-elasticsearch+docs
Metapackage for python3-elasticsearch docs extras.

%description

%package -n     python3-elasticsearch
Summary:        Python client for Elasticsearch
# oreon:reqs
Requires:       python3dist(elastic-transport) < 10
Requires:       python3dist(elastic-transport) >= 9.4.1
# /oreon:reqs
%description -n python3-elasticsearch

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir elasticsearch-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-elasticsearch usr/lib/python3*/site-packages/elasticsearch* usr/lib64/python3*/site-packages/elasticsearch* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/elasticsearch* usr/lib64/python3*/site-packages/elasticsearch* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-elasticsearch -f %{oreon_filedir}/python3-elasticsearch.list

%changelog

%autochangelog
