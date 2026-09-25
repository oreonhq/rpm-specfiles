%global source0_hash 0a9ebc8d4e2f3e8a22848c5258033035bec17a3012ac3fea16dbaa764489eb71

Name:           python-trove-classifiers
Version:        2026.9.21.13
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Canonical source for classifiers on PyPI _pypi.org_.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pypa/trove-classifiers
Source:         %{pypi_source trove_classifiers}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'trove-classifiers' generated automatically by pyp2spec.}

Patch:          Move-to-PEP-621-declarative-metadata.patch

%description %_description

%package -n     python3-trove-classifiers
Summary:        %{summary}

%description -n python3-trove-classifiers %_description


%prep
%autosetup -p1 -n trove_classifiers-%{version}


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


%files -n python3-trove-classifiers -f %{pyproject_files}
%{_bindir}/trove-classifiers

%changelog
%autochangelog
