%global source0_hash dbfd0fe1ee409d0243fdd7a6a6ff14f4948cec1fd78e0376291f805e1501fae9
Name:           python-twisted
Version:        26.4.0
Release:        1%{?dist}
Summary:        An asynchronous networking framework written in Python
License:        ...
URL:            https://twisted.org/
Source0:        https://files.pythonhosted.org/packages/source/t/twisted/twisted-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-fancy-pypi-readme) >= 22.5.0
BuildRequires:  python3dist(hatchling) >= 1.10.0
BuildRequires:  python3dist(incremental) >= 24.7.0
Requires:       python3-twisted = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-twisted
Summary:        An asynchronous networking framework written in Python
# oreon:reqs
Requires:       python3dist(attrs) >= 22.2.0
Requires:       python3dist(automat) >= 24.8.0
Requires:       python3dist(constantly) >= 15.1
Requires:       python3dist(hyperlink) >= 17.1.1
Requires:       python3dist(incremental) >= 24.7.0
Requires:       python3dist(typing-extensions) >= 4.2.0
Requires:       python3dist(zope.interface) >= 5
# /oreon:reqs
%description -n python3-twisted

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir twisted-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-twisted usr/lib/python3*/site-packages/twisted* usr/lib64/python3*/site-packages/twisted* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/twisted* usr/lib64/python3*/site-packages/twisted* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-twisted -f %{oreon_filedir}/python3-twisted.list

%changelog

%autochangelog
