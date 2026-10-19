%global source0_hash 12cbf488b0655dc05aa18a0ca5982de970302604e461fc92e87ebd9b7539b6ff
Name:           python-nitime
Version:        0.12.1
Release:        1%{?dist}
Summary:        Nitime: timeseries analysis for neuroscience data
License:        ...
URL:            http://nipy.org/nitime
Source0:        https://files.pythonhosted.org/packages/source/n/nitime/nitime-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-nitime = %{version}-%{release}
# /oreon:deps
%package -n       python3-nitime+full
Summary:        Metapackage for python3-nitime full extras
Requires:       python3-nitime = %{version}-%{release}
Requires:       python3dist(networkx) >= 3.0
Requires:       python3dist(nibabel) >= 5.0
Provides:       python3dist(nitime[full]) = %{version}-%{release}

%description -n python3-nitime+full
Metapackage for python3-nitime full extras.

%description

%package -n     python3-nitime
Summary:        Nitime: timeseries analysis for neuroscience data
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.7
Requires:       python3dist(numpy) >= 1.24
Requires:       python3dist(scipy) >= 1.10
# /oreon:reqs
%description -n python3-nitime

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir nitime-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nitime usr/lib/python3*/site-packages/nitime* usr/lib64/python3*/site-packages/nitime* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nitime* usr/lib64/python3*/site-packages/nitime* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nitime -f %{oreon_filedir}/python3-nitime.list

%changelog

%autochangelog
