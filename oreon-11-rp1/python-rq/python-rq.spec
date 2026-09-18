%global source0_hash none

Name:           python-rq
Version:        2.12.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        RQ is a simple, lightweight, library for creating background jobs, and processing them.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://python-rq.org/
Source:         %{pypi_source rq}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rq' generated automatically by pyp2spec.}

Patch: https://github.com/rq/rq/pull/2359.patch
Patch: https://github.com/rq/rq/commit/df29cf6.patch
Patch: https://github.com/rq/rq/commit/615525b.patch

%description %_description

%package -n     python3-rq
Summary:        %{summary}

%description -n python3-rq %_description


%prep
%autosetup -p1 -n rq-%{version}


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


%files -n python3-rq -f %{pyproject_files}
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker

%changelog
%autochangelog
