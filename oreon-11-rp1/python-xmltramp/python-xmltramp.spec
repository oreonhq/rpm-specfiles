%global source0_hash 3b4b1635f70cfc0fbd58726aa8f33ec4da204fe9cd41ca22268413a5662ddf21
Name:           python-xmltramp
Version:        2.18
Release:        1%{?dist}
Summary:        Pythonic API for XML
License:        GPL-2.0-only
URL:            http://www.aaronsw.com/2002/xmltramp/
Source0:        http://www.aaronsw.com/2002/xmltramp/xmltramp-%{version}.py
Patch1:         0001-Patch-for-RHBZ-750694.patch
Patch2:         0002-fix-imports-and-syntax-for-Python-3.patch
Patch3:         0003-__str__-needs-to-return-str-not-bytes-on-Python-3.patch
Patch4:         0004-empty-slice-is-slice-None-None-None-on-Python-3.patch
Patch5:         0005-use-OrderedDict-for-attributes-and-namespaces.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description

%package -n python3-xmltramp
Summary: %summary
%{?python_provide:%python_provide python3-xmltramp}
%description -n python3-xmltramp

%prep

%setup -c -T
cp -p %{SOURCE0} xmltramp.py
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build

%install
install -Dm0644 -t %{buildroot}%{python3_sitelib}/ xmltramp.py
%oreon_autofiles python3-xmltramp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} xmltramp.py
%files -f %{oreon_filedir}/main.list
%files -n python3-xmltramp -f %{oreon_filedir}/python3-xmltramp.list

%changelog

%autochangelog
