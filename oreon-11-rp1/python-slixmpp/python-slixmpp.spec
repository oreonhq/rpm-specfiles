%global source0_hash 05257ee0f2aecb42d6479f6071c89ad3c734fda0ee753eb4625ecdc6114d90b1
Name:           python-slixmpp
Version:        1.17.0
Release:        1%{?dist}
Summary:        Slixmpp is an elegant Python library for XMPP _aka Jabber_.
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/s/slixmpp/slixmpp-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-slixmpp = %{version}-%{release}
# /oreon:deps
%package -n       python3-slixmpp+xep-0363
Summary:        Metapackage for python3-slixmpp xep-0363 extras
Requires:       python3-slixmpp = %{version}-%{release}
Provides:       python3dist(slixmpp[xep-0363]) = %{version}-%{release}

%description -n python3-slixmpp+xep-0363
Metapackage for python3-slixmpp xep-0363 extras.

%package -n       python3-slixmpp+xep-0444-compliance
Summary:        Metapackage for python3-slixmpp xep-0444-compliance extras
Requires:       python3-slixmpp = %{version}-%{release}
Provides:       python3dist(slixmpp[xep-0444-compliance]) = %{version}-%{release}

%description -n python3-slixmpp+xep-0444-compliance
Metapackage for python3-slixmpp xep-0444-compliance extras.

%package -n       python3-slixmpp+xep-0454
Summary:        Metapackage for python3-slixmpp xep-0454 extras
Requires:       python3-slixmpp = %{version}-%{release}
Provides:       python3dist(slixmpp[xep-0454]) = %{version}-%{release}

%description -n python3-slixmpp+xep-0454
Metapackage for python3-slixmpp xep-0454 extras.

%package -n       python3-slixmpp+safer-xml-parsing
Summary:        Metapackage for python3-slixmpp safer-xml-parsing extras
Requires:       python3-slixmpp = %{version}-%{release}
Provides:       python3dist(slixmpp[safer-xml-parsing]) = %{version}-%{release}

%description -n python3-slixmpp+safer-xml-parsing
Metapackage for python3-slixmpp safer-xml-parsing extras.

%description

%package -n     python3-slixmpp
Summary:        Slixmpp is an elegant Python library for XMPP _aka Jabber_.
# oreon:reqs
Requires:       python3dist(aiodns) >= 3.2.0
Requires:       python3dist(pyasn1) >= 0.6.1
Requires:       python3dist(pyasn1-modules) >= 0.4.1
# /oreon:reqs
%description -n python3-slixmpp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir slixmpp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-slixmpp usr/lib/python3*/site-packages/slixmpp* usr/lib64/python3*/site-packages/slixmpp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/slixmpp* usr/lib64/python3*/site-packages/slixmpp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-slixmpp -f %{oreon_filedir}/python3-slixmpp.list

%changelog

%autochangelog
