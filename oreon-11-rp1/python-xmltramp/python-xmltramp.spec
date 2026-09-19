%global source0_hash none

Name:           python-xmltramp
Version:        2.18
Release:        30%{?dist}
Summary:        Pythonic API for XML

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
# License text is not present in the upstream file, though clearly marked as GPLv2
# See https://www.redhat.com/archives/fedora-legal-list/2008-January/msg00010.html

URL:            http://www.aaronsw.com/2002/xmltramp/
Source0:        http://www.aaronsw.com/2002/xmltramp/xmltramp-%{version}.py
Patch1:         0001-Patch-for-RHBZ-750694.patch
Patch2:         0002-fix-imports-and-syntax-for-Python-3.patch
Patch3:         0003-__str__-needs-to-return-str-not-bytes-on-Python-3.patch
Patch4:         0004-empty-slice-is-slice-None-None-None-on-Python-3.patch
Patch5:         0005-use-OrderedDict-for-attributes-and-namespaces.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
xmltramp is a simple Pythonic API for working with XML.

%description %_description

%package -n python3-xmltramp
Summary: %summary
%{?python_provide:%python_provide python3-xmltramp}

%description -n python3-xmltramp %_description

%prep
%setup -c -T
cp -p %{SOURCE0} xmltramp.py
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
# noarch

%install
install -Dm0644 -t %{buildroot}%{python3_sitelib}/ xmltramp.py

%check
%{__python3} xmltramp.py

%files -n python3-xmltramp
%{python3_sitelib}/xmltramp.py*
%{python3_sitelib}/__pycache__/

%changelog
%autochangelog
