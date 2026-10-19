%global source0_hash a8eeedc4e87cf070f7ef450b76cdecd120d1e5c602a9c35855ec7777591f949f
Name:           python-salib
Version:        1.5.2
Release:        1%{?dist}
Summary:        Tools for global sensitivity analysis. Contains Sobol_, Morris, FAST, DGSM, PAWN, HDMR, Moment Independent and fractional factorial methods
License:        MIT
URL:            https://github.com/SALib/SALib
Source0:        https://files.pythonhosted.org/packages/source/s/salib/salib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-salib = %{version}-%{release}
# /oreon:deps
%package -n       python3-salib+distributed
Summary:        Metapackage for python3-salib distributed extras
Requires:       python3-salib = %{version}-%{release}
Requires:       python3dist(pathos) >= 0.3.2
Provides:       python3dist(salib[distributed]) = %{version}-%{release}

%description -n python3-salib+distributed
Metapackage for python3-salib distributed extras.

%package -n       python3-salib+test
Summary:        Metapackage for python3-salib test extras
Requires:       python3-salib = %{version}-%{release}
Provides:       python3dist(salib[test]) = %{version}-%{release}

%description -n python3-salib+test
Metapackage for python3-salib test extras.

%package -n       python3-salib+doc
Summary:        Metapackage for python3-salib doc extras
Requires:       python3-salib = %{version}-%{release}
Requires:       python3dist(pydata-sphinx-theme) >= 0.15.2
Provides:       python3dist(salib[doc]) = %{version}-%{release}

%description -n python3-salib+doc
Metapackage for python3-salib doc extras.

%package -n       python3-salib+dev
Summary:        Metapackage for python3-salib dev extras
Requires:       python3-salib = %{version}-%{release}
Provides:       python3dist(salib[dev]) = %{version}-%{release}

%description -n python3-salib+dev
Metapackage for python3-salib dev extras.

%description

%package -n     python3-salib
Summary:        Tools for global sensitivity analysis. Contains Sobol_, Morris, FAST, DGSM, PAWN, HDMR, Moment Independent and fractional factorial methods
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.5
Requires:       python3dist(numpy) >= 2.0
Requires:       python3dist(pandas) >= 2.0
Requires:       python3dist(scipy) >= 1.9.3
# /oreon:reqs
%description -n python3-salib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir salib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-salib usr/lib/python3*/site-packages/salib* usr/lib64/python3*/site-packages/salib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/salib* usr/lib64/python3*/site-packages/salib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-salib -f %{oreon_filedir}/python3-salib.list

%changelog

%autochangelog
