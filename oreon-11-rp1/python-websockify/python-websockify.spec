%global source0_hash b6413e364efd04f3c92ec8c17747e3c4adc20157c2ef1c5d019a26d944a46df8
%global pkgname websockify
%global summary WSGI based adapter for the Websockets protocol
Name:           python-%{pkgname}
Version:        0.13.0
Release:        1%{?dist}
Summary:        WSGI based adapter for the Websockets protocol
License:        LGPL-3.0-only
URL:            https://github.com/kanaka/websockify
Source0:        https://github.com/kanaka/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Python WSGI based adapter for the Websockets protocol

%package -n python3-%{pkgname}
Summary:        WSGI based adapter for the Websockets protocol
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-websockify -f %{oreon_filedir}/python3-websockify.list
%files -n python-websockify-doc -f %{oreon_filedir}/python-websockify-doc.list

%changelog

%autochangelog
