%global source0_hash a383e17d912e512d20de0bb096d8c21331bd28e1c8a9273e6e75f3c48c7ee85c
Name:           python-quart-trio
Version:        0.13.0
Release:        1%{?dist}
Summary:        A Quart extension to provide trio support
License:        MIT
URL:            https://github.com/pgjones/quart-trio
Source0:        https://github.com/pgjones/quart-trio/archive/%{version}/quart-trio-%{version}.tar.gz
Patch:          0001-Downstream-only-patch-out-coverage-analysis.patch
Patch:          0002-Downstream-only-patch-out-pytest-sugar.patch
BuildArch:      noarch
%global common_description %{expand:
Quart-Trio is an extension for Quart to support the Trio event loop. This is an
alternative to using the asyncio event loop present in the Python standard
library and supported by default in Quart.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-quart-trio = %{version}-%{release}
# /oreon:deps
%package -n       python3-quart-trio+docs
Summary:        Metapackage for python3-quart-trio docs extras
Requires:       python3-quart-trio = %{version}-%{release}
Provides:       python3dist(quart-trio[docs]) = %{version}-%{release}

%description -n python3-quart-trio+docs
Metapackage for python3-quart-trio docs extras.

%description %{common_description}

%package -n python3-quart-trio
Summary:        A Quart extension to provide trio support
# oreon:reqs
Requires:       python3dist(hypercorn[trio]) >= 0.12.0
Requires:       python3dist(quart) >= 0.23
Requires:       python3dist(trio) >= 0.19.0
# /oreon:reqs
%description -n python3-quart-trio %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-quart-trio usr/lib/python3*/site-packages/quart_trio* usr/lib64/python3*/site-packages/quart_trio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/quart_trio* usr/lib64/python3*/site-packages/quart_trio* usr/bin/*

%check

%tox -- -- -v
%files
%files -n python3-quart-trio -f %{oreon_filedir}/python3-quart-trio.list

%changelog

%autochangelog
