%global source0_hash 800f072d39d892f69cdfd29e88499320993450ec4cdcd545067a628d69c36886

Name:           python-repoze-tm2
Version:        2.2.0
Release:        17%{?dist}
Summary:        Zope-like transaction manager via WSGI middleware

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/repoze.tm2
Source0:        https://pypi.python.org/packages/source/r/repoze.tm2/repoze.tm2-%{version}.tar.gz
BuildArch:      noarch

%global _description\
The ZODB transaction manager is a completely generic transaction manager.  It\
can be used independently of the actual "object database" part of ZODB.  One\
of the purposes of creating repoze.tm was to allow for systems other than\
Zope to make use of two-phase commit transactions in a WSGI context.

%description %_description

%package -n python3-repoze-tm2
Summary: Zope-like transaction manager via WSGI middleware
BuildRequires: python3-devel
BuildRequires: python3-transaction

%description -n python3-repoze-tm2
The ZODB transaction manager is a completely generic transaction manager.  It
can be used independently of the actual "object database" part of ZODB.  One
of the purposes of creating repoze.tm was to allow for systems other than
Zope to make use of two-phase commit transactions in a WSGI context.

This package contains the python3 version of the library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n repoze.tm2-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l repoze

%check
%pyproject_check_import

%files -n python3-repoze-tm2 -f %{pyproject_files}
%doc README.rst COPYRIGHT.txt CHANGES.rst
%{python3_sitelib}/repoze.tm2-%{version}-py*-nspkg.pth

%changelog
%autochangelog
