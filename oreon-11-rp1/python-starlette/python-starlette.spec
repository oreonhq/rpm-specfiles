%global source0_hash d4e3ac5e546444960c710297a3c9fc3f7ebae1b7e963f3d36173b49da535be9b
Name:           python-starlette
Version:        1.6.0
Release:        1%{?dist}
Summary:        The little ASGI library that shines.
License:        BSD-3-Clause
URL:            https://github.com/Kludex/starlette
Source0:        https://files.pythonhosted.org/packages/source/s/starlette/starlette-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-starlette-CVE-2026-48710.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-starlette = %{version}-%{release}
# /oreon:deps
%package -n       python3-starlette+full
Summary:        Metapackage for python3-starlette full extras
Requires:       python3-starlette = %{version}-%{release}
Requires:       python3dist(python-multipart) >= 0.0.18
Requires:       python3dist(httpx) >= 0.27.0
Requires:       python3dist(httpx) < 0.29.0
Requires:       python3dist(httpx2) >= 2.0.0
Provides:       python3dist(starlette[full]) = %{version}-%{release}

%description -n python3-starlette+full
Metapackage for python3-starlette full extras.

%description

%package -n     python3-starlette
Summary:        The little ASGI library that shines.
# oreon:reqs
Requires:       python3dist(anyio) < 5
Requires:       python3dist(anyio) >= 3.6.2
Requires:       python3dist(typing-extensions) >= 4.10.0
# /oreon:reqs
%description -n python3-starlette

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir starlette-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-starlette usr/lib/python3*/site-packages/starlette* usr/lib64/python3*/site-packages/starlette* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/starlette* usr/lib64/python3*/site-packages/starlette* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-starlette -f %{oreon_filedir}/python3-starlette.list

%changelog

%autochangelog
