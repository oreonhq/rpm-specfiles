%global source0_hash none

Name:           python-multitasking
Version:        0.0.13
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Non-blocking Python methods using decorators

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ranaroussi/multitasking
Source:         %{pypi_source multitasking}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'multitasking' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-multitasking
Summary:        %{summary}

%description -n python3-multitasking %_description


%prep
%autosetup -p1 -n multitasking-%{version}


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


%files -n python3-multitasking -f %{pyproject_files}

%changelog
%autochangelog
