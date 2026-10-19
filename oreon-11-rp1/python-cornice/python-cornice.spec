%global source0_hash bfd1b6c2a991a7ccb1b2082b6de9e3b8f198b6a2b4a07ab0800e05df05a45361
%global pypi_name cornice
%global desc Helpers to build & document Web Services with Pyramid.
Name:             python-cornice
Version:          6.1.0
Release:        1%{?dist}
BuildArch:        noarch
License:          MPL-2.0
Summary:        Define Web Services in Pyramid
URL:              https://github.com/Cornices/cornice/
Source0:        https://files.pythonhosted.org/packages/source/c/cornice/cornice-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-cornice = %{version}-%{release}
# /oreon:deps
%package -n       python3-cornice+dev
Summary:        Metapackage for python3-cornice dev extras
Requires:       python3-cornice = %{version}-%{release}
Requires:       python3dist(pytest) < 9
Requires:       python3dist(pytest-cache) < 2
Requires:       python3dist(pytest-cov) < 5
Requires:       python3dist(webtest) < 4
Requires:       python3dist(marshmallow) < 4
Requires:       python3dist(colander) < 3
Provides:       python3dist(cornice[dev]) = %{version}-%{release}

%description -n python3-cornice+dev
Metapackage for python3-cornice dev extras.

%description
%{desc}

%package -n python3-cornice
Summary:        Define Web Services in Pyramid
Recommends: %{py3_dist colander}
%description -n python3-%{pypi_name}
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cornice usr/lib/python3*/site-packages/cornice* usr/lib64/python3*/site-packages/cornice* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cornice* usr/lib64/python3*/site-packages/cornice* usr/bin/*

%check

%pytest -v
%files
%files -n python3-cornice -f %{oreon_filedir}/python3-cornice.list

%changelog

%autochangelog
