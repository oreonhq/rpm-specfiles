%global source0_hash none

Name:           python-llm
Version:        0.35
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        CLI utility and Python library for interacting with Large Language Models from organizations like OpenAI, Anthropic and Gemini plus local models installed on your own machine.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/simonw/llm
Source:         %{pypi_source llm}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'llm' generated automatically by pyp2spec.}

Patch:          python-llm-0.28-relax-click.patch
Patch:          python-llm-0.27.1-disable-tests.patch
Patch:          python-llm-0.27.1-sqlite-3.51.patch
Patch:          https://github.com/simonw/llm/pull/1333.patch

%description %_description

%package -n     python3-llm
Summary:        %{summary}

%description -n python3-llm %_description


%prep
%autosetup -p1 -n llm-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-llm -f %{pyproject_files}
%{_bindir}/llm

%changelog
%autochangelog
