%global source0_hash bb6ff310bba8b1130ffe675347f668f7234d022ba3d51edea5ea7e2ea9523897

%global pypi_name PyKMIP
%global sname pykmip

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{sname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Python implementation of the Key Management Interoperability Protocol

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/OpenKMIP/PyKMIP
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         enum34.patch
BuildArch:      noarch

%description
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%if %{with python2}
%package -n python2-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires:       python2-devel
BuildRequires:       python2-six
BuildRequires:       python2-setuptools

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:       python2-enum34
%else
BuildRequires:       python-enum34
%endif

Requires:     python2-cryptography
Requires:     python2-requests
Requires:     python2-six
Requires:     python2-sqlalchemy

%if 0%{?fedora} || 0%{?rhel} > 7
Requires:     python2-enum34
%else
Requires:     python-enum34
%endif

%description -n python2-%{sname}
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).
%endif

%if %{with python3}
%package -n python3-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:       python3-devel
BuildRequires:       python3-six
BuildRequires:       python3-setuptools

Requires:     python3-cryptography
Requires:     python3-requests
Requires:     python3-six
Requires:     python3-sqlalchemy

%description -n python3-%{sname}
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{sname}
%doc README.rst
%license LICENSE.txt
%if !%{with python3}
%{_bindir}/pykmip-server
%endif
%{python2_sitelib}/kmip
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{sname}
%doc README.rst
%license LICENSE.txt
%{_bindir}/pykmip-server
%{python3_sitelib}/kmip
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
%autochangelog
