%global source0_hash none

Name:           python-zuul-sphinx
Version:        0.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Sphinx extension for documenting Zuul jobs

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://docs.openstack.org/infra/zuul-sphinx/
Source:         %{pypi_source zuul_sphinx}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'zuul-sphinx' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-zuul-sphinx
Summary:        %{summary}

%description -n python3-zuul-sphinx %_description


%prep
%autosetup -p1 -n zuul_sphinx-%{version}


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


%files -n python3-zuul-sphinx -f %{pyproject_files}

%changelog
%autochangelog
