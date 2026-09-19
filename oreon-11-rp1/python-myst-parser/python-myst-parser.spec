%global source0_hash none

Name:           python-myst-parser
Version:        5.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        An extended _CommonMark__https://spec.commonmark.org/_ compliant parser,

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/executablebooks/MyST-Parser
Source:         %{pypi_source myst_parser}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'myst-parser' generated automatically by pyp2spec.}

Patch:          Adjust-test-output-to-docutils-0.22.patch

%description %_description

%package -n     python3-myst-parser
Summary:        %{summary}

%description -n python3-myst-parser %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-myst-parser code-style,linkify,rtd,testing,testing-docutils


%prep
%autosetup -p1 -n myst_parser-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x code-style,linkify,rtd,testing,testing-docutils


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-myst-parser -f %{pyproject_files}
%{_bindir}/myst-anchors
%{_bindir}/myst-docutils-demo
%{_bindir}/myst-docutils-html
%{_bindir}/myst-docutils-html5
%{_bindir}/myst-docutils-latex
%{_bindir}/myst-docutils-pseudoxml
%{_bindir}/myst-docutils-xml
%{_bindir}/myst-inv

%changelog
%autochangelog
