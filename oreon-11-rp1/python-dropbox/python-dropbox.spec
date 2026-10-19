%global source0_hash 61fcb821f7e8585aa4b9e2abc94801aaf8d65ed5ca89313450e56d51c46add7e
Name:           python-dropbox
Version:        12.2.1
Release:        1%{?dist}
Summary:        Official Dropbox API Client
License:        MIT
URL:            http://www.dropbox.com/developers
Source0:        https://files.pythonhosted.org/packages/source/d/dropbox/dropbox-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) < 9
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-dropbox = %{version}-%{release}
# /oreon:deps
%package -n       python3-dropbox+test
Summary:        Metapackage for python3-dropbox test extras
Requires:       python3-dropbox = %{version}-%{release}
Requires:       python3dist(stone) >= 3.5.3
Requires:       python3dist(stone) < 4
Provides:       python3dist(dropbox[test]) = %{version}-%{release}

%description -n python3-dropbox+test
Metapackage for python3-dropbox test extras.

%package -n       python3-dropbox+docs
Summary:        Metapackage for python3-dropbox docs extras
Requires:       python3-dropbox = %{version}-%{release}
Provides:       python3dist(dropbox[docs]) = %{version}-%{release}

%description -n python3-dropbox+docs
Metapackage for python3-dropbox docs extras.

%package -n       python3-dropbox+dev
Summary:        Metapackage for python3-dropbox dev extras
Requires:       python3-dropbox = %{version}-%{release}
Provides:       python3dist(dropbox[dev]) = %{version}-%{release}

%description -n python3-dropbox+dev
Metapackage for python3-dropbox dev extras.

%description

%package -n     python3-dropbox
Summary:        Official Dropbox API Client
# oreon:reqs
Requires:       python3dist(requests) >= 2.16.2
Requires:       python3dist(stone) < 4
Requires:       python3dist(stone) >= 3.5.3
# /oreon:reqs
%description -n python3-dropbox

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dropbox-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dropbox usr/lib/python3*/site-packages/dropbox* usr/lib64/python3*/site-packages/dropbox* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dropbox* usr/lib64/python3*/site-packages/dropbox* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dropbox -f %{oreon_filedir}/python3-dropbox.list

%changelog

%autochangelog
