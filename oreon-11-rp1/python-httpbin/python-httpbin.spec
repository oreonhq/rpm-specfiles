%global source0_hash 6023a5a2e8fb8e91abdd6d34d1f1f455092f97d567c25600e1b48ee1178aa738
Name:           python-httpbin
Version:        0.10.4
Release:        1%{?dist}
Summary:        HTTP Request and Response Service
License:        ISC AND MIT
URL:            https://github.com/psf/httpbin
Source0:        https://files.pythonhosted.org/packages/source/h/httpbin/httpbin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-httpbin = %{version}-%{release}
# /oreon:deps
%package -n       python3-httpbin+test
Summary:        Metapackage for python3-httpbin test extras
Requires:       python3-httpbin = %{version}-%{release}
Provides:       python3dist(httpbin[test]) = %{version}-%{release}

%description -n python3-httpbin+test
Metapackage for python3-httpbin test extras.

%package -n       python3-httpbin+mainapp
Summary:        Metapackage for python3-httpbin mainapp extras
Requires:       python3-httpbin = %{version}-%{release}
Provides:       python3dist(httpbin[mainapp]) = %{version}-%{release}

%description -n python3-httpbin+mainapp
Metapackage for python3-httpbin mainapp extras.

%description

%package -n     python3-httpbin
Summary:        HTTP Request and Response Service
# oreon:reqs
Requires:       python3dist(flask) >= 2.2.4
Requires:       python3dist(greenlet) < 3.0
Requires:       python3dist(greenlet) >= 3.0.0a1
Requires:       python3dist(werkzeug) >= 2.2.2
# /oreon:reqs
%description -n python3-httpbin

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir httpbin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httpbin usr/lib/python3*/site-packages/httpbin* usr/lib64/python3*/site-packages/httpbin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httpbin* usr/lib64/python3*/site-packages/httpbin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-httpbin -f %{oreon_filedir}/python3-httpbin.list

%changelog

%autochangelog
