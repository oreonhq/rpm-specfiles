%global source0_hash 807c789c3184d7070010dbdf1339ee46ff9fb9b6694d7caa3047f975f8a7df60

%global srcname bottle

Name:           python-%{srcname}
Version:        0.13.4
Release:        5%{?dist}
Summary:        Fast and simple WSGI-framework for small web-applications

License:        MIT
URL:            http://bottlepy.org
Source0:        https://github.com/bottlepy/bottle/archive/0.13.4.tar.gz#/bottle-0.13.4.tar.gz

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
