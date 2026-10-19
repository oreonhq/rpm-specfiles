%global source0_hash 2f2055a949f69db3e8c1f37d787f6ffd076ea29d561dda68918289a2a5d41a93
Name:           python-wsgidav
Version:        4.3.5
Release:        1%{?dist}
Summary:        Generic and extendable WebDAV server based on WSGI
License:        MIT
URL:            https://github.com/mar10/wsgidav
Source0:        https://files.pythonhosted.org/packages/source/w/wsgidav/wsgidav-%{version}.tar.gz
BuildArch:      noarch
Patch:         %{url}/commit/991a23f5f5f3f46232eacd96666e23c1b5e110b5.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wsgidav = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wsgidav
Summary:        Generic and extendable WebDAV server based on WSGI
%description -n python3-wsgidav

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir wsgidav-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wsgidav usr/lib/python3*/site-packages/wsgidav* usr/lib64/python3*/site-packages/wsgidav* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wsgidav* usr/lib64/python3*/site-packages/wsgidav* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wsgidav -f %{oreon_filedir}/python3-wsgidav.list

%changelog

%autochangelog
