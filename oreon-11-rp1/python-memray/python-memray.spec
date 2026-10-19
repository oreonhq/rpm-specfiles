%global source0_hash ce1f1d900948d57d7db5b5d8d81f4ebfcb798eff674493503ce5bfaafcea84dc
Name:           python-memray
Version:        1.20.0
Release:        1%{?dist}
Summary:        A memory profiler for Python applications
License:        ...
URL:            https://github.com/bloomberg/memray
Source0:        https://files.pythonhosted.org/packages/source/m/memray/memray-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(scikit-build-core) >= 0.9
Requires:       python3-memray = %{version}-%{release}
# /oreon:deps
%package -n       python3-memray+test
Summary:        Metapackage for python3-memray test extras
Requires:       python3-memray = %{version}-%{release}
Requires:       python3dist(textual) >= 0.43
Provides:       python3dist(memray[test]) = %{version}-%{release}

%description -n python3-memray+test
Metapackage for python3-memray test extras.

%package -n       python3-memray+docs
Summary:        Metapackage for python3-memray docs extras
Requires:       python3-memray = %{version}-%{release}
Provides:       python3dist(memray[docs]) = %{version}-%{release}

%description -n python3-memray+docs
Metapackage for python3-memray docs extras.

%package -n       python3-memray+lint
Summary:        Metapackage for python3-memray lint extras
Requires:       python3-memray = %{version}-%{release}
Provides:       python3dist(memray[lint]) = %{version}-%{release}

%description -n python3-memray+lint
Metapackage for python3-memray lint extras.

%package -n       python3-memray+benchmark
Summary:        Metapackage for python3-memray benchmark extras
Requires:       python3-memray = %{version}-%{release}
Provides:       python3dist(memray[benchmark]) = %{version}-%{release}

%description -n python3-memray+benchmark
Metapackage for python3-memray benchmark extras.

%package -n       python3-memray+dev
Summary:        Metapackage for python3-memray dev extras
Requires:       python3-memray = %{version}-%{release}
Requires:       python3dist(textual) >= 0.43
Provides:       python3dist(memray[dev]) = %{version}-%{release}

%description -n python3-memray+dev
Metapackage for python3-memray dev extras.

%description

%package -n     python3-memray
Summary:        A memory profiler for Python applications
# oreon:reqs
Requires:       python3dist(jinja2) >= 2.9
Requires:       python3dist(rich) >= 11.2.0
Requires:       python3dist(textual) >= 0.41.0
# /oreon:reqs
%description -n python3-memray

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir memray-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-memray usr/lib/python3*/site-packages/memray* usr/lib64/python3*/site-packages/memray* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/memray* usr/lib64/python3*/site-packages/memray* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-memray -f %{oreon_filedir}/python3-memray.list

%changelog

%autochangelog
