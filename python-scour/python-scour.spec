%global modname scour
%global sum     An SVG scrubber

Name:               python-scour
Version:            0.38.2
Release:            17%{?dist}
Summary:            %{sum}

# All files are Apache-2.0 except scour/svg_regex.py
# which is BSD-3-Clause
License:            Apache-2.0 AND BSD-3-Clause
URL:                https://github.com/scour-project/scour
Source0:            %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
# Tests
BuildRequires:      python3-six
BuildRequires:      python3-pytest
BuildArch: noarch

%global _description %{expand:
Scour is an SVG optimizer/cleaner written in Python that reduces the
size of scalable vector graphics by optimizing structure and removing
unnecessary data.

It can be used to create streamlined vector graphics suitable for web
deployment, publishing/sharing or further processing.

The goal of Scour is to output a file that renders identically at a
fraction of the size by removing a lot of redundant information created
by most SVG editors. Optimization options are typically lossless but can
be tweaked for more aggressive cleaning.}


%description %_description


%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}
Requires: python3-packaging

%description -n python3-%{modname}
%_description


%prep
%autosetup -n %{modname}-%{version}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pyproject_check_import
%pytest


%files -n python3-%{modname} -f %{pyproject_files}
%{_bindir}/scour
%doc README.md
%doc HISTORY.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.38.2-17
- Prepare for Oreon 11 (RP1)
