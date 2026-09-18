%global source0_hash none

Name:           python-llama-cpp-python
Version:        0.3.35
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python bindings for the llama.cpp library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/abetlen/llama-cpp-python
Source:         %{pypi_source llama_cpp_python}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'llama-cpp-python' generated automatically by pyp2spec.}

Patch1:         0001-don-t-build-llava.patch
Patch2:         0002-search-for-libllama-so-in-usr-lib64.patch
Patch3:         https://github.com/abetlen/llama-cpp-python/pull/1718.patch#/0003-drop-optional-dependency-of-scikit-build-core.patch

%description %_description

%package -n     python3-llama-cpp-python
Summary:        %{summary}

%description -n python3-llama-cpp-python %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-llama-cpp-python all,dev,server,test


%prep
%autosetup -p1 -n llama_cpp_python-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,dev,server,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-llama-cpp-python -f %{pyproject_files}

%changelog
%autochangelog
