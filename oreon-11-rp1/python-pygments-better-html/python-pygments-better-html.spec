%global source0_hash none

Name:           python-pygments-better-html
Version:        0.1.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Better HTML formatter for Pygments.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/Kwpolska/pygments_better_html
Source:         %{pypi_source pygments_better_html}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pygments-better-html' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pygments-better-html
Summary:        %{summary}

%description -n python3-pygments-better-html %_description


%prep
%autosetup -p1 -n pygments_better_html-%{version}


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


%files -n python3-pygments-better-html -f %{pyproject_files}

%changelog
%autochangelog
