%global source0_hash 76cee167e81fc3cc0e0cc696fe58cadd039e19a774c8f4d2e5c0fea724c7aaca
%global srcname %(echo %{name} | sed 's/^python-//')
Name:           python-xml2rfc
Version:        3.9.1
Release:        18%{?dist}
Summary:        Convert IETF RFC-7749 XML into txt format
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            https://pypi.python.org/pypi/xml2rfc/
Source0:        https://files.pythonhosted.org/packages/source/x/xml2rfc/xml2rfc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary: Convert IETF RFC-2629 XML into txt format
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
Requires: python3-google-i18n-address
Requires: python3-appdirs
Requires: python3-configargparse
Requires: python3-pyflakes
Requires: python3-html5lib
Requires: python3-intervaltree
Requires: python3-pycountry
Requires: python3-jinja2
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# temp workaround, filed bug upstream: https://trac.ietf.org/trac/xml2rfc/ticket/661#ticket
sed -i "s/jinja2>=2.11,<3.0/jinja2>=2.11/" requirements.txt

%build

%py3_build
%check

%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-xml2rfc -f %{oreon_filedir}/python3-xml2rfc.list

%changelog

%autochangelog
