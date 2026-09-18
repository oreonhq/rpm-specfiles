%global source0_hash none

Name:           python-nltk
Version:        3.10.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Natural Language Toolkit

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/nltk/nltk
Source:         %{pypi_source nltk}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nltk' generated automatically by pyp2spec.}

Patch1: fix-import-WordNetLemmatizer.patch

%description %_description

%package -n     python3-nltk
Summary:        %{summary}

%description -n python3-nltk %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nltk all,corenlp,machine-learning,plot,tgrep,twitter


%prep
%autosetup -p1 -n nltk-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,corenlp,machine-learning,plot,tgrep,twitter


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nltk -f %{pyproject_files}
%{_bindir}/nltk

%changelog
%autochangelog
