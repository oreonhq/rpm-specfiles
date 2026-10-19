%global source0_hash 3cf49f69df8326bcf17a3cb3d3d3ec4a856858fe3a7473746c9044c317d3ba55
Name:           python-cattrs
Version:        26.2.0
Release:        1%{?dist}
Summary:        Composable complex class support for attrs and dataclasses.
License:        MIT
URL:            https://catt.rs
Source0:        https://files.pythonhosted.org/packages/source/c/cattrs/cattrs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cattrs = %{version}-%{release}
# /oreon:deps
%package -n       python3-cattrs+ujson
Summary:        Metapackage for python3-cattrs ujson extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(ujson) >= 5.10.0
Provides:       python3dist(cattrs[ujson]) = %{version}-%{release}

%description -n python3-cattrs+ujson
Metapackage for python3-cattrs ujson extras.

%package -n       python3-cattrs+orjson
Summary:        Metapackage for python3-cattrs orjson extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(orjson) >= 3.11.3
Provides:       python3dist(cattrs[orjson]) = %{version}-%{release}

%description -n python3-cattrs+orjson
Metapackage for python3-cattrs orjson extras.

%package -n       python3-cattrs+msgpack
Summary:        Metapackage for python3-cattrs msgpack extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(msgpack) >= 1.0.5
Provides:       python3dist(cattrs[msgpack]) = %{version}-%{release}

%description -n python3-cattrs+msgpack
Metapackage for python3-cattrs msgpack extras.

%package -n       python3-cattrs+pyyaml
Summary:        Metapackage for python3-cattrs pyyaml extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0
Provides:       python3dist(cattrs[pyyaml]) = %{version}-%{release}

%description -n python3-cattrs+pyyaml
Metapackage for python3-cattrs pyyaml extras.

%package -n       python3-cattrs+tomlkit
Summary:        Metapackage for python3-cattrs tomlkit extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(tomlkit) >= 0.11.8
Provides:       python3dist(cattrs[tomlkit]) = %{version}-%{release}

%description -n python3-cattrs+tomlkit
Metapackage for python3-cattrs tomlkit extras.

%package -n       python3-cattrs+cbor2
Summary:        Metapackage for python3-cattrs cbor2 extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(cbor2) >= 5.4.6
Provides:       python3dist(cattrs[cbor2]) = %{version}-%{release}

%description -n python3-cattrs+cbor2
Metapackage for python3-cattrs cbor2 extras.

%package -n       python3-cattrs+bson
Summary:        Metapackage for python3-cattrs bson extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(pymongo) >= 4.4.0
Provides:       python3dist(cattrs[bson]) = %{version}-%{release}

%description -n python3-cattrs+bson
Metapackage for python3-cattrs bson extras.

%package -n       python3-cattrs+msgspec
Summary:        Metapackage for python3-cattrs msgspec extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(msgspec) >= 0.21.1
Provides:       python3dist(cattrs[msgspec]) = %{version}-%{release}

%description -n python3-cattrs+msgspec
Metapackage for python3-cattrs msgspec extras.

%package -n       python3-cattrs+tomllib
Summary:        Metapackage for python3-cattrs tomllib extras
Requires:       python3-cattrs = %{version}-%{release}
Requires:       python3dist(tomli) >= 1.1.0
Requires:       python3dist(tomli-w) >= 1.1.0
Provides:       python3dist(cattrs[tomllib]) = %{version}-%{release}

%description -n python3-cattrs+tomllib
Metapackage for python3-cattrs tomllib extras.

%description

%package -n     python3-cattrs
Summary:        Composable complex class support for attrs and dataclasses.
# oreon:reqs
Requires:       python3dist(attrs) >= 25.4.0
Requires:       python3dist(exceptiongroup) >= 1.1.1
Requires:       python3dist(typing-extensions) >= 4.14.0
# /oreon:reqs
%description -n python3-cattrs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cattrs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cattrs usr/lib/python3*/site-packages/cattrs* usr/lib64/python3*/site-packages/cattrs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cattrs* usr/lib64/python3*/site-packages/cattrs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cattrs -f %{oreon_filedir}/python3-cattrs.list

%changelog

%autochangelog
