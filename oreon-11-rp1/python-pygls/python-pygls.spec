%global source0_hash 69714019ef1deb7fb38bf3dcd1d6e93dcddf5eef239830d10ed581eb7511f35d
Name:           python-pygls
Version:        2.1.1
Release:        1%{?dist}
Summary:        A pythonic generic language server
License:        Apache-2.0
URL:            https://github.com/openlawlibrary/pygls
Source0:        https://github.com/openlawlibrary/pygls/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pygls = %{version}-%{release}
# /oreon:deps
%package -n       python3-pygls+ws
Summary:        Metapackage for python3-pygls ws extras
Requires:       python3-pygls = %{version}-%{release}
Requires:       python3dist(websockets) >= 13.0
Provides:       python3dist(pygls[ws]) = %{version}-%{release}

%description -n python3-pygls+ws
Metapackage for python3-pygls ws extras.

%description

%package -n     python3-pygls
Summary:        A pythonic generic language server
# oreon:reqs
Requires:       python3dist(attrs) >= 24.3.0
Requires:       python3dist(cattrs) >= 23.1.2
Requires:       python3dist(lsprotocol) == 2025.0.0
# /oreon:reqs
%description -n python3-pygls

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygls usr/lib/python3*/site-packages/pygls* usr/lib64/python3*/site-packages/pygls* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygls* usr/lib64/python3*/site-packages/pygls* usr/bin/*

%check

%pytest -rs
%files
%files -n python3-pygls -f %{oreon_filedir}/python3-pygls.list

%changelog

%autochangelog
