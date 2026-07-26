%global source0_hash 576047f45560e82f64aa5f15200b1eb094dcfe1c5b8f531a8a65bd208e25a493

Name:           python-sphinx-thebe
Version:        0.3.1
Release:        %autorelease
Summary:        Integrate interactive code blocks into your documentation

License:        MIT
BuildArch:      noarch
URL:            https://sphinx-thebe.readthedocs.io/
VCS:            git:https://github.com/executablebooks/sphinx-thebe.git
Source:         %pypi_source sphinx_thebe

BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x testing
BuildOption(install): -l sphinx_thebe

%description
Integrate interactive code blocks into your documentation with Thebe and
Binder.

%package     -n python3-sphinx-thebe
Summary:        Integrate interactive code blocks into your documentation

%description -n python3-sphinx-thebe
Integrate interactive code blocks into your documentation with Thebe and
Binder.

%check
%pytest

%files -n python3-sphinx-thebe -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
