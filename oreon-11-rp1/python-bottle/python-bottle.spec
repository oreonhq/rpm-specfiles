%global srcname bottle

Name:           python-%{srcname}
Version:        0.13.4
Release:        5%{?dist}
Summary:        Fast and simple WSGI-framework for small web-applications

License:        MIT
URL:            http://bottlepy.org
Source0:        https://github.com/bottlepy/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 807c789c3184d7070010dbdf1339ee46ff9fb9b6694d7caa3047f975f8a7df60
%global source0_file 0.13.4.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(pytest)

%description
Bottle is a fast and simple micro-framework for small web-applications.
It offers request dispatching (Routes) with URL parameter support, Templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines. All in a single file and with no dependencies other than the
Python Standard Library.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Fast and simple WSGI-framework for small web-applications
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Bottle is a fast and simple micro-framework for small web-applications.
It offers request dispatching (Routes) with URL parameter support, Templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines. All in a single file and with no dependencies other than the
Python Standard Library.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/0.13.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "807c789c3184d7070010dbdf1339ee46ff9fb9b6694d7caa3047f975f8a7df60" || { echo "oreon: Source0 SHA256 mismatch for 0.13.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{srcname}-%{version}
sed -i '/^#!/d' bottle.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm %{buildroot}%{_bindir}/bottle %{buildroot}%{_bindir}/bottle.py

%check
%{pytest} test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS README.rst docs/*
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/*.dist-info
%{python3_sitelib}/*.py

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.4-5
- Prepare for Oreon 11 (RP1)
