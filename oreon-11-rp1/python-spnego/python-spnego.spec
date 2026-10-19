%global source0_hash 448a491a9bf0e5fb957567fe46e6809fa836aa40dfcccebcc740bb64acb1be1c
Name:           python-spnego
Version:        0.12.2
Release:        1%{?dist}
Summary:        Windows Negotiate Authentication Client and Server
License:        MIT
URL:            https://github.com/jborean93/pyspnego
Source0:        https://files.pythonhosted.org/packages/source/p/pyspnego/pyspnego-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-spnego = %{version}-%{release}
# /oreon:deps
%package -n       python3-spnego+kerberos
Summary:        Metapackage for python3-spnego kerberos extras
Requires:       python3-spnego = %{version}-%{release}
Requires:       python3dist(gssapi) >= 1.6.0
Requires:       python3dist(krb5) >= 0.3.0
Provides:       python3dist(spnego[kerberos]) = %{version}-%{release}

%description -n python3-spnego+kerberos
Metapackage for python3-spnego kerberos extras.

%package -n       python3-spnego+yaml
Summary:        Metapackage for python3-spnego yaml extras
Requires:       python3-spnego = %{version}-%{release}
Provides:       python3dist(spnego[yaml]) = %{version}-%{release}

%description -n python3-spnego+yaml
Metapackage for python3-spnego yaml extras.

%description

%package -n     python3-spnego
Summary:        Windows Negotiate Authentication Client and Server
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
# oreon:reqs
Requires:       python3dist(sspilib) >= 0.5.0
# /oreon:reqs
%description -n python3-spnego

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyspnego-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-spnego usr/lib/python3*/site-packages/spnego* usr/lib64/python3*/site-packages/spnego* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/spnego* usr/lib64/python3*/site-packages/spnego* usr/bin/*

%check

%pytest -v tests
%files
%files -n python3-spnego -f %{oreon_filedir}/python3-spnego.list

%changelog

%autochangelog
