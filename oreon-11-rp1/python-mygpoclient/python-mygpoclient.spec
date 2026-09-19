%global source0_hash 00e8b9fc990aafd7427411bb7b8e7878cd4e364ccf405691070ff924985c70b5

Name:       python-mygpoclient
Version:    1.10
Release:    7%{?dist}
Summary:    Python module to connect to the my.gpodder.org webservice

License:    GPL-3.0-or-later
URL:        http://thpinfo.com/2010/mygpoclient/ 
Source0:    http://thpinfo.com/2010/mygpoclient/mygpoclient-%{version}.tar.gz  
BuildArch:  noarch

%global _description\
%{name} is a client-library to connect the my.gpodder.org webservice.

%description %_description

%package -n python3-mygpoclient
Summary: %summary
%{?python3_provide:%python3_provide python3-mygpoclient}
BuildRequires: python3-devel
BuildRequires: python3-minimock
BuildRequires: python3-coverage
BuildRequires: python3-pytest
BuildRequires: python3-simplejson

%description -n python3-mygpoclient %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mygpoclient-%{version}

# Leave out http-tests as they currently fail occasionally (reported upstream)
rm mygpoclient/http_test.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install

%files -n python3-mygpoclient
%{python3_sitelib}/mygpoclient
%{python3_sitelib}/mygpoclient*.dist-info
%{_bindir}/mygpo-*
%{_mandir}/man1/mygpo-bpsync.1.gz
%exclude %{python3_sitelib}/mygpoclient/*test.py*
%doc README.md COPYING AUTHORS

%changelog
%autochangelog
