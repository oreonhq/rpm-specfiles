%global source0_hash cf30099e25e840d875b8d17a6c06811c6e6b7f6af6cba4b8016ec9d82de2c1f1
Name:           python-huami-token
Version:        0.8.0
Release:        1%{?dist}
Summary:        This script retrieves the Bluetooth access token for the watch or band from Huami servers. Additionally, it downloads the AGPS data packs, cep_alm_pak.zip and cep_7days.zip.
License:        MIT
URL:            https://codeberg.org/argrento/huami-token
Source0:        https://files.pythonhosted.org/packages/source/h/huami_token/huami_token-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{name}-deps.patch
Patch:          %{name}-entrypoint.patch
Patch:          %{name}-headers.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.25
Requires:       python3-huami-token = %{version}-%{release}
# /oreon:deps
%package -n       python3-huami-token+dev
Summary:        Metapackage for python3-huami-token dev extras
Requires:       python3-huami-token = %{version}-%{release}
Requires:       python3dist(pytest) >= 8
Requires:       python3dist(pytest) < 9
Requires:       python3dist(types-requests) >= 2.31.0.20231231
Requires:       python3dist(ruff) >= 0.5
Requires:       python3dist(ruff) < 1
Requires:       python3dist(mypy) >= 1.10
Requires:       python3dist(mypy) < 2
Provides:       python3dist(huami-token[dev]) = %{version}-%{release}

%description -n python3-huami-token+dev
Metapackage for python3-huami-token dev extras.

%description

%package -n     python3-huami-token
Summary:        This script retrieves the Bluetooth access token for the watch or band from Huami servers. Additionally, it downloads the AGPS data packs, cep_alm_pak.zip and cep_7days.zip.
# oreon:reqs
Requires:       python3dist(loguru) >= 0.7.3
Requires:       python3dist(pycryptodome) >= 3.23.0
Requires:       python3dist(requests) < 3
Requires:       python3dist(requests) >= 2.31.0
# /oreon:reqs
%description -n python3-huami-token

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir huami_token-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-huami-token usr/lib/python3*/site-packages/huami_token* usr/lib64/python3*/site-packages/huami_token* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/huami_token* usr/lib64/python3*/site-packages/huami_token* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-huami-token -f %{oreon_filedir}/python3-huami-token.list

%changelog

%autochangelog
