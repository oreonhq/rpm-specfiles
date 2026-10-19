%global source0_hash 721b86b77fca33a735598292022ac6feef99747bf48f52defdada6b572acd5af
Name:           python-eventlet
Version:        0.41.2
Release:        1%{?dist}
Summary:        Highly concurrent networking library
License:        MIT
URL:            https://github.com/eventlet/eventlet
Source0:        https://files.pythonhosted.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
BuildArch:      noarch
Patch0: 0001-Update-pyzmq-and-psycopg2-binary-versions.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.3
BuildRequires:  python3dist(hatchling) >= 1.12.2
Requires:       python3-eventlet = %{version}-%{release}
# /oreon:deps
%package -n       python3-eventlet+dev
Summary:        Metapackage for python3-eventlet dev extras
Requires:       python3-eventlet = %{version}-%{release}
Provides:       python3dist(eventlet[dev]) = %{version}-%{release}

%description -n python3-eventlet+dev
Metapackage for python3-eventlet dev extras.

%description

%package -n     python3-eventlet
Summary:        Highly concurrent networking library
# oreon:reqs
Requires:       python3dist(dnspython) >= 1.15.0
Requires:       python3dist(greenlet) >= 1.0
# /oreon:reqs
%description -n python3-eventlet

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir eventlet-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-eventlet usr/lib/python3*/site-packages/eventlet* usr/lib64/python3*/site-packages/eventlet* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/eventlet* usr/lib64/python3*/site-packages/eventlet* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-eventlet -f %{oreon_filedir}/python3-eventlet.list

%changelog

%autochangelog
