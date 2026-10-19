%global source0_hash 7de0efcc361c573f2537ee7ceabdb3bc64b19b61304cfa25e828caa7db8ae1a4
%bcond cattrs %{undefined fc40}
Name:           python-ufoLib2
Version:        0.18.1
Release:        5%{?dist}
Summary:        A library to deal with UFO font sources
License:        Apache-2.0
URL:            https://github.com/fonttools/ufoLib2
Source0:        https://files.pythonhosted.org/packages/source/u/ufolib2/ufolib2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm) >= 6.2
Requires:       python3-ufoLib2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-ufoLib2+lxml
Summary:        Metapackage for python3-ufoLib2 lxml extras
Requires:       python3-ufoLib2 = %{version}-%{release}
Provides:       python3dist(ufoLib2[lxml]) = %{version}-%{release}

%description -n python3-ufoLib2+lxml
Metapackage for python3-ufoLib2 lxml extras.

%package -n       python3-ufoLib2+converters
Summary:        Metapackage for python3-ufoLib2 converters extras
Requires:       python3-ufoLib2 = %{version}-%{release}
Requires:       python3dist(cattrs) >= 25.1.1
Provides:       python3dist(ufoLib2[converters]) = %{version}-%{release}

%description -n python3-ufoLib2+converters
Metapackage for python3-ufoLib2 converters extras.

%package -n       python3-ufoLib2+json
Summary:        Metapackage for python3-ufoLib2 json extras
Requires:       python3-ufoLib2 = %{version}-%{release}
Requires:       python3dist(cattrs) >= 25.1.1
Provides:       python3dist(ufoLib2[json]) = %{version}-%{release}

%description -n python3-ufoLib2+json
Metapackage for python3-ufoLib2 json extras.

%package -n       python3-ufoLib2+msgpack
Summary:        Metapackage for python3-ufoLib2 msgpack extras
Requires:       python3-ufoLib2 = %{version}-%{release}
Requires:       python3dist(cattrs) >= 25.1.1
Provides:       python3dist(ufoLib2[msgpack]) = %{version}-%{release}

%description -n python3-ufoLib2+msgpack
Metapackage for python3-ufoLib2 msgpack extras.

%description

%package -n python3-ufoLib2
Summary:        A library to deal with UFO font sources
# oreon:reqs
Requires:       python3dist(attrs) >= 22.1.0
Requires:       python3dist(fonttools[ufo]) >= 4.58.0
# /oreon:reqs
%description -n python3-ufoLib2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ufolib2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ufoLib2 usr/lib/python3*/site-packages/ufoLib2* usr/lib64/python3*/site-packages/ufoLib2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ufoLib2* usr/lib64/python3*/site-packages/ufoLib2* usr/bin/*

%check

%pyproject_check_import %{?!with_cattrs:-e ufoLib2.converters -e ufoLib2.serde.json -e ufoLib2.serde.msgpack}
%pytest -v
%files
%files -n python3-ufoLib2 -f %{oreon_filedir}/python3-ufoLib2.list

%changelog

%autochangelog
