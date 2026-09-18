%global source0_hash none

Name:           python-oslo-metrics
Version:        0.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Oslo Metrics library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.metrics
Source:         %{pypi_source oslo_metrics}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oslo-metrics' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-oslo-metrics
Summary:        %{summary}

%description -n python3-oslo-metrics %_description


%prep
%autosetup -p1 -n oslo_metrics-%{version}


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


%files -n python3-oslo-metrics -f %{pyproject_files}
%{_bindir}/oslo-metrics

%changelog
%autochangelog
