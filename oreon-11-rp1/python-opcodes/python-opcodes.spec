%global source0_hash none

Name:           python-opcodes
Version:        0.3.14
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Database of Processor Instructions/Opcodes

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/Maratyszcza/Opcodes
Source:         %{pypi_source opcodes}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opcodes' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-opcodes
Summary:        %{summary}

%description -n python3-opcodes %_description


%prep
%autosetup -p1 -n opcodes-%{version}


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


%files -n python3-opcodes -f %{pyproject_files}

%changelog
%autochangelog
