%global source0_hash a9356f0cb89b3b8621529c5d5eebd69bfe154f4c3f68b4cf2de47e45fa855c2e
Name:           python-uvicorn
Version:        0.53.0
Release:        1%{?dist}
Summary:        The lightning-fast ASGI server.
License:        BSD-3-Clause
URL:            https://uvicorn.dev/
Source0:        https://files.pythonhosted.org/packages/source/u/uvicorn/uvicorn-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-uvicorn = %{version}-%{release}
# /oreon:deps
%package -n       python3-uvicorn+standard
Summary:        Metapackage for python3-uvicorn standard extras
Requires:       python3-uvicorn = %{version}-%{release}
Requires:       python3dist(httptools) >= 0.8.0
Requires:       python3dist(python-dotenv) >= 0.13
Requires:       python3dist(pyyaml) >= 5.1
Requires:       python3dist(uvloop) >= 0.15.1
Requires:       python3dist(watchfiles) >= 0.20
Requires:       python3dist(websockets) >= 13.0
Provides:       python3dist(uvicorn[standard]) = %{version}-%{release}

%description -n python3-uvicorn+standard
Metapackage for python3-uvicorn standard extras.

%description

%package -n     python3-uvicorn
Summary:        The lightning-fast ASGI server.
# oreon:reqs
Requires:       python3dist(click) >= 7.0
Requires:       python3dist(h11) >= 0.8
Requires:       python3dist(typing-extensions) >= 4.0
# /oreon:reqs
%description -n python3-uvicorn

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir uvicorn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-uvicorn usr/lib/python3*/site-packages/uvicorn* usr/lib64/python3*/site-packages/uvicorn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uvicorn* usr/lib64/python3*/site-packages/uvicorn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-uvicorn -f %{oreon_filedir}/python3-uvicorn.list

%changelog

%autochangelog
