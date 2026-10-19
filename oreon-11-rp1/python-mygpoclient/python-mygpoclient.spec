%global source0_hash 00e8b9fc990aafd7427411bb7b8e7878cd4e364ccf405691070ff924985c70b5
Name:       python-mygpoclient
Version:    1.10
Release:        1%{?dist}
Summary:        Python module to connect to the my.gpodder.org webservice
License:    GPL-3.0-or-later
URL:        http://thpinfo.com/2010/mygpoclient/ 
Source0:        http://thpinfo.com/2010/mygpoclient/mygpoclient-%{version}.tar.gz
BuildArch:  noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mygpoclient = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-mygpoclient
Summary: %summary
%{?python3_provide:%python3_provide python3-mygpoclient}
BuildRequires: python3-devel
BuildRequires: python3-minimock
BuildRequires: python3-coverage
BuildRequires: python3-pytest
BuildRequires: python3-simplejson
%description -n python3-mygpoclient

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mygpoclient-%{version}

# Leave out http-tests as they currently fail occasionally (reported upstream)
rm mygpoclient/http_test.py

%build

%pyproject_wheel
%check

%pytest
%install
%pyproject_install
%oreon_autofiles python3-mygpoclient usr/lib/python3*/site-packages/mygpoclient* usr/lib64/python3*/site-packages/mygpoclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mygpoclient* usr/lib64/python3*/site-packages/mygpoclient* usr/bin/*

%files
%files -n python3-mygpoclient -f %{oreon_filedir}/python3-mygpoclient.list

%changelog

%autochangelog
