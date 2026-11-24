# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 288e3ca7d54b06f2ac191970bc275c1939cb46d450b255bf6718b04aa37ab4f7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?rhel} > 11 || 0%{?oreon}
%bcond soupsieve 0
%bcond tests 0
%else
%bcond soupsieve 1
%bcond tests 1
%endif

Name:           python-beautifulsoup4
Version:        4.15.0
Release:        1%{?dist}
Summary:        HTML/XML parser for quick-turnaround applications like screen-scraping
License:        MIT
URL:            http://www.crummy.com/software/BeautifulSoup/
Source0:        https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
Patch0:         0001-libxml2-seems-to-have-reverted-changes-done-in-2.13..patch
Patch11:        beautifulsoup4-4.14-disable-soupsieve.patch
BuildArch:      noarch
%if %{with tests}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-html5lib
BuildRequires:  python3-lxml
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with soupsieve}
BuildRequires:  python3-packaging
BuildRequires:  python3-soupsieve
%endif

%global _description %{expand:
Beautiful Soup is a Python HTML/XML parser designed for quick
turnaround projects like screen-scraping. Three features make it
powerful:

Beautiful Soup won't choke if you give it bad markup.

Beautiful Soup provides a few simple methods and Pythonic idioms for
navigating, searching, and modifying a parse tree.

Beautiful Soup automatically converts incoming documents to Unicode
and outgoing documents to UTF-8.

Beautiful Soup parses anything you give it.

Valuable data that was once locked up in poorly-designed websites is
now within your reach. Projects that would have taken hours take only
minutes with Beautiful Soup.}

%description %_description

%package     -n python3-beautifulsoup4
Summary:        %summary
Requires:       python3-lxml
%if %{with soupsieve}
Requires:       python3-soupsieve
%endif
Obsoletes:      python3-BeautifulSoup < 1:3.2.1-2
%{?python_provide:%python_provide python3-beautifulsoup4}

%description -n python3-beautifulsoup4 %_description

%prep
%oreon_sha256
%autosetup -N -n beautifulsoup4-%{version}
%autopatch -p1 -M 10
%if %{without soupsieve}
%autopatch -p1 -m 10
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bs4

%if %{with tests}
%check
%tox
%endif

%files -n python3-beautifulsoup4
%license LICENSE
%doc NEWS.txt CHANGELOG
%{python3_sitelib}/beautifulsoup4-%{version}.dist-info/
%{python3_sitelib}/bs4

%changelog
%autochangelog
