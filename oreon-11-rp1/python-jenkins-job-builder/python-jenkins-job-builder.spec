%global source0_hash none

Name:           python-jenkins-job-builder
Version:        6.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Manage Jenkins jobs with YAML

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://jenkins-job-builder.readthedocs.io/en/latest/
Source:         %{pypi_source jenkins_job_builder}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jenkins-job-builder' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jenkins-job-builder
Summary:        %{summary}

%description -n python3-jenkins-job-builder %_description


%prep
%autosetup -p1 -n jenkins_job_builder-%{version}


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


%files -n python3-jenkins-job-builder -f %{pyproject_files}
%{_bindir}/jenkins-jobs

%changelog
%autochangelog
