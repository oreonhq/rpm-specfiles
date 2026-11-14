# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a6fd48da305b49da4ee1ee8b40234fffaf2d581519e49300023a3a7024c02fa4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global rel_tag rel_1_2_3

Name: python3-mako
Version: 1.2.3
Release: 1%{?dist}
Summary: Mako template library for Python
License: MIT AND Python-2.0.1 AND BSD-3-Clause
URL: https://www.makotemplates.org/
Source0: https://github.com/sqlalchemy/mako/archive/%{rel_tag}.tar.gz
Patch0: mako-pygments-quotes.patch
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-markupsafe
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-wheel

Requires: python3
Requires: python3-markupsafe

Provides: python3dist(mako) = %{version}
Provides: python-mako = %{version}-%{release}
Obsoletes: python2-mako < 1.1.0-3
Obsoletes: python-mako-doc < 1.1.4-6

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%prep
%oreon_sha256
%autosetup -p1 -n mako-%{rel_tag}
sed -i '/tag_build = dev/d' setup.cfg

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
mv %{buildroot}%{_bindir}/mako-render %{buildroot}%{_bindir}/mako-render-%{python3_version}
ln -s mako-render-%{python3_version} %{buildroot}%{_bindir}/mako-render-3
ln -s mako-render-%{python3_version} %{buildroot}%{_bindir}/mako-render
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest

%files -f %{_builddir}/%{name}.files
%license LICENSE
%doc CHANGES README.rst examples

%changelog
%autochangelog
