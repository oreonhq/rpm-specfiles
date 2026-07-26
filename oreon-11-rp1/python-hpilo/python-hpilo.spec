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

# Automatically converted from old format: ASL 2.0 or GPLv3+ - review is highly recommended.
License:        Apache-2.0 OR GPL-3.0-or-later
URL:            https://github.com/seveas/python-hpilo
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description 
%{_desc}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{desc}
%{desc}

%package        doc
Summary:        Documentation for %{name}

%description    doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build -b html docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# remove version-control-internal-file
rm examples/elasticsearch/.gitignore

%install
%pyproject_install
%pyproject_save_files hpilo hpilo_fw

%check
# https://github.com/seveas/python-hpilo/issues/272
# pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES examples ilo.conf.example
%{_bindir}/hpilo_cli

%files doc
%license COPYING
%doc html

%changelog
%autochangelog
