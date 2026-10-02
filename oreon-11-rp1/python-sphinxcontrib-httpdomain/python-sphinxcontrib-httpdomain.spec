%global source0_hash 449700c12406370cc80df8c54eba930bf098d38b414cf756c594d2ce313647c2

Name:           python-sphinxcontrib-httpdomain
Version:        2.0.0a4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx extension that provides a domain for documenting HTTP APIs.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/sphinx-contrib/httpdomain
Source:         %{pypi_source sphinxcontrib_httpdomain}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinxcontrib-httpdomain' generated automatically by pyp2spec.}

Patch4:         0004-httpdomain-bump-domain-data-version.patch

%description %_description

%package -n     python3-sphinxcontrib-httpdomain
Summary:        %{summary}

%description -n python3-sphinxcontrib-httpdomain %_description


%prep
%autosetup -p1 -n sphinxcontrib_httpdomain-%{version}


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


%files -n python3-sphinxcontrib-httpdomain -f %{pyproject_files}

%changelog
%autochangelog
