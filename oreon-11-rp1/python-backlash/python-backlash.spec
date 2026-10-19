%global source0_hash 7721245a87a8c68b743ea9c63b803bdfde0c8db601580bd980a08736cbe5b583
Name:           python-backlash
Version:        0.5.1
Release:        1%{?dist}
Summary:        Interactive in-browser debugger and error reporting middleware for WSGI and ASGI applications
License:        MIT
URL:            https://github.com/TurboGears/backlash
Source0:        https://files.pythonhosted.org/packages/source/b/backlash/backlash-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-backlash = %{version}-%{release}
# /oreon:deps
%package -n       python3-backlash+testing
Summary:        Metapackage for python3-backlash testing extras
Requires:       python3-backlash = %{version}-%{release}
Provides:       python3dist(backlash[testing]) = %{version}-%{release}

%description -n python3-backlash+testing
Metapackage for python3-backlash testing extras.

%description

%package -n     python3-backlash
Summary:        Interactive in-browser debugger and error reporting middleware for WSGI and ASGI applications
%description -n python3-backlash

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir backlash-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-backlash usr/lib/python3*/site-packages/backlash* usr/lib64/python3*/site-packages/backlash* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/backlash* usr/lib64/python3*/site-packages/backlash* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-backlash -f %{oreon_filedir}/python3-backlash.list

%changelog

%autochangelog
