%global source0_hash 0ae931b893aae5a0b2a056be0a5be292f4005cb41b1554e079e03881263a36f6

Name:           python-sphinx-inline-tabs
Version:        2025.12.21.14
Release:        %autorelease
Summary:        Add inline tabbed content to your Sphinx documentation
# SPDX
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source:         %{url}/archive/%{version}/sphinx-inline-tabs-%{version}.tar.gz

Patch:          https://github.com/pradyunsg/sphinx-inline-tabs/pull/53.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%global orbs_pyproject_requires_options -x test
%global orbs_pyproject_files_options -l sphinx_inline_tabs

%global _description %{expand:
Add inline tabbed content to your Sphinx documentation.

Features:

- Elegant design: Small footprint in the markup and generated website,
  while looking good.
- Configurable: All the colors can be configured using CSS variables.
- Synchronization: Tabs with the same label all switch with a single click.
- Works without JavaScript: JavaScript is not required for the basics, only for
  synchronization.}

%description %_description

%package -n python3-sphinx-inline-tabs
Summary:        %{summary}

%description -n python3-sphinx-inline-tabs  %_description

%prep
%autosetup -p1
sed -i '/pytest-cov/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?orbs_pyproject_requires_options}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{?orbs_pyproject_files_options}

%check
%pytest -k "not xml"

%files -n python3-sphinx-inline-tabs -f %{pyproject_files}
%doc README.md
%doc CODE_OF_CONDUCT.md

%changelog
%autochangelog
