%global source0_hash 610ca751c9bc2492b38eb9a38a7fbc93edbbb2d7182edaf34e66ae493dee5c8c
Name:           python-pygments
Version:        2.21.0
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python.
License:        BSD-2-Clause
URL:            https://pygments.org
Source0:        https://files.pythonhosted.org/packages/source/p/pygments/pygments-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27
Requires:       python3-pygments = %{version}-%{release}
# /oreon:deps
%package -n       python3-pygments+plugins
Summary:        Metapackage for python3-pygments plugins extras
Requires:       python3-pygments = %{version}-%{release}
Provides:       python3dist(pygments[plugins]) = %{version}-%{release}

%description -n python3-pygments+plugins
Metapackage for python3-pygments plugins extras.

%package -n       python3-pygments+windows-terminal
Summary:        Metapackage for python3-pygments windows-terminal extras
Requires:       python3-pygments = %{version}-%{release}
Requires:       python3dist(colorama) >= 0.4.6
Provides:       python3dist(pygments[windows-terminal]) = %{version}-%{release}

%description -n python3-pygments+windows-terminal
Metapackage for python3-pygments windows-terminal extras.

%description

%package -n     python3-pygments
Summary:        Pygments is a syntax highlighting package written in Python.
%description -n python3-pygments

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pygments-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygments usr/lib/python3*/site-packages/pygments* usr/lib64/python3*/site-packages/pygments* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygments* usr/lib64/python3*/site-packages/pygments* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygments -f %{oreon_filedir}/python3-pygments.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.19.1-1
- Prepare for Oreon 11 (RP1)
