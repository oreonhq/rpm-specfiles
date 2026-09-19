%global source0_hash none

Name:           python-persist-queue
Version:        1.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A thread-safe disk based persistent queue in Python.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://github.com/peter-wangxu/persist-queue
Source:         %{pypi_source persist_queue}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'persist-queue' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-persist-queue
Summary:        %{summary}

%description -n python3-persist-queue %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-persist-queue async,extra


%prep
%autosetup -p1 -n persist_queue-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x async,extra


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-persist-queue -f %{pyproject_files}

%changelog
%autochangelog
