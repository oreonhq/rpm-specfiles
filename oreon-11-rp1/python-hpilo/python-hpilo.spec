%global source0_hash 172b598109b43127750df3dc00100a191d71207b7b0f37b11fba393c0169b3b9
%global srcname hpilo
%global desc %{expand: \
HP iLO XML interface access from Python (Python 3)
This module will make it easy for you to access the Integrated Lights Out
management interface of your HP hardware. It supports RILOE II, iLO, iLO 2, iLO
3 and iLO 4. It uses the XML interface or hponcfg to access and change the iLO.}
Name:           python-%{srcname}
Version:        4.4.3
Release:        17%{?dist}
Summary:        Accessing the HP iLO XML interface from python
License:        Apache-2.0 OR GPL-3.0-or-later
URL:            https://github.com/seveas/python-hpilo
Source0:        https://github.com/seveas/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hpilo = %{version}-%{release}
# /oreon:deps
%description 
%{_desc}

%package     -n python3-%{srcname}
Summary:        Accessing the HP iLO XML interface from python
%description -n python3-%{srcname} %{desc}
%{desc}

%package        doc
Summary:        Documentation for %{name}
%description    doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
sphinx-build -b html docs html
rm -rf html/.{doctrees,buildinfo}
rm examples/elasticsearch/.gitignore
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/hpilo* usr/lib64/python3*/site-packages/hpilo* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files
%files -n python3-hpilo -f %{oreon_filedir}/python3-hpilo.list
%files -n python-hpilo-doc -f %{oreon_filedir}/python-hpilo-doc.list

%changelog

%autochangelog
