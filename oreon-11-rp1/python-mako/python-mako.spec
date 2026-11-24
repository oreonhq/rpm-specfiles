# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 60608d2535a5315dca4245d558594bf700b54ec7192d9b5a92c4bccf5e315dcc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global src_name mako
%global _description %{expand:
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako`s
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi.

Conceptually, Mako is an embedded Python (i.e. Python Server Page) language,
which refines the familiar ideas of componentized layout and inheritance to
produce one of the most straightforward and flexible models available, while
also maintaining close ties to Python calling and scoping semantics.}

%bcond bootstrap 0
%if 0%{?oreon}
%bcond tests 0
%else
%bcond tests %{without bootstrap}
%endif

Name:		python-%{src_name}
Version:	1.4.1
Release:        %{autorelease}
Summary:	Mako template library for Python

License:	MIT AND Python-2.0.1 AND BSD-3-Clause
URL:		https://www.makotemplates.org
Source0:        https://github.com/sqlalchemy/mako/archive/rel_1_4_1/%{src_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires: oreon-rpm-macros
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description %{_description}

%package -n python3-%{src_name}
Summary:	%{summary}
%if %{undefined rhel}
Recommends:	python3-beaker
%endif
Obsoletes:	python2-mako < 1.1.0-3
Obsoletes:	python-mako-doc < 1.1.4-6

%description -n python3-%{src_name} %{_description}

%prep
%oreon_sha256
%autosetup -p1 -n %{src_name}-rel_1_4_1
%pyproject_patch_dependency lingua:ignore
%if 0%{?rhel} || 0%{?oreon}
%pyproject_patch_dependency beaker:ignore
%pyproject_patch_dependency dogpile.cache:ignore
%pyproject_patch_dependency junitparser:ignore
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g tests}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{src_name}

%check
%pyproject_check_import --exclude mako.ext.babelplugin --exclude mako.ext.linguaplugin
%if %{with tests}
%pytest -v
%endif

%files -n python3-%{src_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render

%changelog
%autochangelog
