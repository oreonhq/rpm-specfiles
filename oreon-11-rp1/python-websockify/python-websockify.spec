%global source0_hash 37448ec992ef626f29558404cf6535592d02894ec1d5f0990a8c62621b39a967

%global pkgname websockify
%global summary WSGI based adapter for the Websockets protocol
Name:           python-%{pkgname}
Version:        0.12.0
Release:        7%{?dist}
Summary:        %{summary}

License:        LGPL-3.0-only
URL:            https://github.com/kanaka/websockify
Source0:        %{url}/archive/v%{version}/websockify-%{version}.tar.gz
BuildArch:      noarch

%description
Python WSGI based adapter for the Websockets protocol

%package -n python3-%{pkgname}
Summary:        %{summary} - Python 3 version
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-setuptools

%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Python WSGI based adapter for the Websockets protocol - Python 3 version

%package doc
Summary:        %{summary} - documentation

%description doc
Python WSGI based adapter for the Websockets protocol - documentation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}

%build
%py3_build

%install
%py3_install

rm -Rf %{buildroot}/usr/share/websockify
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/websockify.1 %{buildroot}%{_mandir}/man1/

%files -n python3-%{pkgname}
%license COPYING
%{_mandir}/man1/websockify.1*
%{python3_sitelib}/websockify/
%{python3_sitelib}/websockify-%{version}-py%{python3_version}.egg-info
%{_bindir}/websockify

%files doc
%license COPYING
%doc docs

%changelog
%autochangelog
