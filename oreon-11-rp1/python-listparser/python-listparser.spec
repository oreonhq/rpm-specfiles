%global source0_hash 0dda5b41ca9531fc3c438eb4abf4d8a7cf03ef050d196875993e897a66c1f885
Name:           python-listparser
Version:        0.20
Release:        1%{?dist}
Summary:        Parse OPML subscription lists
License:        MIT
URL:            https://github.com/kurtmckee/listparser/
Source0:        https://files.pythonhosted.org/packages/source/l/listparser/listparser-%{version}.tar.gz
BuildArch:      noarch
Patch0:         2to3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-listparser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-listparser
Summary:        Parse OPML subscription lists
%description -n python3-listparser

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir listparser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-listparser usr/lib/python3*/site-packages/listparser* usr/lib64/python3*/site-packages/listparser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/listparser* usr/lib64/python3*/site-packages/listparser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-listparser -f %{oreon_filedir}/python3-listparser.list

%changelog

%autochangelog
