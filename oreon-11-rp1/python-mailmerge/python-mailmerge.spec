%global source0_hash 2714ee8cdb933633d29d71a55437c6c655835dd461d0564534c9d7e27fcc0a56
Name:           python-mailmerge
Version:        2.3.0
Release:        1%{?dist}
Summary:        A simple, command line mail merge tool
License:        ...
URL:            https://github.com/awdeorio/mailmerge/
Source0:        https://files.pythonhosted.org/packages/source/m/mailmerge/mailmerge-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0.0
Requires:       python3-mailmerge = %{version}-%{release}
# /oreon:deps
%package -n       python3-mailmerge+dev
Summary:        Metapackage for python3-mailmerge dev extras
Requires:       python3-mailmerge = %{version}-%{release}
Provides:       python3dist(mailmerge[dev]) = %{version}-%{release}

%description -n python3-mailmerge+dev
Metapackage for python3-mailmerge dev extras.

%package -n       python3-mailmerge+test
Summary:        Metapackage for python3-mailmerge test extras
Requires:       python3-mailmerge = %{version}-%{release}
Provides:       python3dist(mailmerge[test]) = %{version}-%{release}

%description -n python3-mailmerge+test
Metapackage for python3-mailmerge test extras.

%description

%package -n     python3-mailmerge
Summary:        A simple, command line mail merge tool
# oreon:reqs
Requires:       python3dist(click) >= 8.3
# /oreon:reqs
%description -n python3-mailmerge

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mailmerge-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mailmerge usr/lib/python3*/site-packages/mailmerge* usr/lib64/python3*/site-packages/mailmerge* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mailmerge* usr/lib64/python3*/site-packages/mailmerge* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mailmerge -f %{oreon_filedir}/python3-mailmerge.list

%changelog

%autochangelog
