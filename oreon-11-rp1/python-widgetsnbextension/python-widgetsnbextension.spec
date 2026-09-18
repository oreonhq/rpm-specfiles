%global source0_hash none

Name:           python-widgetsnbextension
Version:        4.0.16
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Jupyter interactive widgets for Jupyter Notebook

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://jupyter.org
Source:         %{pypi_source widgetsnbextension}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'widgetsnbextension' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-widgetsnbextension
Summary:        %{summary}

%description -n python3-widgetsnbextension %_description


%prep
%autosetup -p1 -n widgetsnbextension-%{version}


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


%files -n python3-widgetsnbextension -f %{pyproject_files}

%changelog
%autochangelog
