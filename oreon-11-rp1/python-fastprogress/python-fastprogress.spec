%global source0_hash 7de3a5b136fdf0a9763c19180d0bdfc1bb8c6172b09123c0e4ba272d0c092d0c
Name:           python-fastprogress
Version:        1.1.6
Release:        1%{?dist}
Summary:        A nested progress with plotting options for fastai
License:        Apache-2.0
URL:            https://github.com/answerdotai/fastprogress
Source0:        https://files.pythonhosted.org/packages/source/f/fastprogress/fastprogress-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-fastprogress = %{version}-%{release}
# /oreon:deps
%package -n       python3-fastprogress+dev
Summary:        Metapackage for python3-fastprogress dev extras
Requires:       python3-fastprogress = %{version}-%{release}
Provides:       python3dist(fastprogress[dev]) = %{version}-%{release}

%description -n python3-fastprogress+dev
Metapackage for python3-fastprogress dev extras.

%description

%package -n     python3-fastprogress
Summary:        A nested progress with plotting options for fastai
# oreon:reqs
Requires:       python3dist(fastcore) >= 1.10.0
Requires:       python3dist(python-fasthtml) >= 0.12.34
# /oreon:reqs
%description -n python3-fastprogress

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fastprogress-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastprogress usr/lib/python3*/site-packages/fastprogress* usr/lib64/python3*/site-packages/fastprogress* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastprogress* usr/lib64/python3*/site-packages/fastprogress* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastprogress -f %{oreon_filedir}/python3-fastprogress.list

%changelog

%autochangelog
