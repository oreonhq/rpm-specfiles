%global source0_hash none

Name:           python-myhdl
Version:        0.11.52
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python as a Hardware Description Language

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://www.myhdl.org
Source:         %{pypi_source myhdl}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'myhdl' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-myhdl
Summary:        %{summary}

%description -n python3-myhdl %_description


%prep
%autosetup -p1 -n myhdl-%{version}


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


%files -n python3-myhdl -f %{pyproject_files}

%changelog
%autochangelog
