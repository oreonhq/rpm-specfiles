%global source0_hash e700cbc53a857f443a782cc95f6a4d8ba4a264b12b67c3328b2f4f2f4156273f

%global pypi_name python-markdown-math
%global srcname markdown-math

Name:           python-%{srcname}
Version:        0.8
Release:        21%{?dist}
Summary:        Math extension for Python-Markdown

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mitya57/python-markdown-math
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(markdown)

%description
Extension for Python-Markdown: this extension adds math
formulas support to Python-Markdown.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Extension for Python-Markdown: this extension adds math
formulas support to Python-Markdown.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} test.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/mdx_math.py
%{python3_sitelib}/python_markdown_math-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
