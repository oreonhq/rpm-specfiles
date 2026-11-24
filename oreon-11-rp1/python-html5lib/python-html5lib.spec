# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b2e5b40261e20f354d198eae92afc10d750afb487ed5e50f9c4eaf07c184146f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-html5lib
Summary:        A python based HTML parser/tokenizer
Version:        1.1
Release:        %{autorelease}
Epoch:          1
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
Source0:        %{pypi_source html5lib}

Patch:          %{url}/pull/506.patch
Patch:          %{url}/pull/573.patch
Patch:          %{url}/pull/583.patch
Patch:          590.patch
Patch:          %{url}/pull/591.patch
Patch:          594.patch
Patch:          wbr_element_support.patch
Patch:          formaction_uri.patch
Patch:          %{url}/pull/600.patch

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-expect)

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%package -n python3-html5lib
Summary:        %{summary}

%description -n python3-html5lib
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%pyproject_extras_subpkg -n python3-html5lib lxml genshi chardet all

%prep
%oreon_sha256
%autosetup -p1 -n html5lib-%{version}

sed -i 's/from mock import/from unittest.mock import/' html5lib/tests/test_meta.py

%generate_buildrequires
%pyproject_buildrequires -x all

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files html5lib

%check
%pytest

%files -n python3-html5lib -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
