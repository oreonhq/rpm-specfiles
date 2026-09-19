%global source0_hash none

Name:           python-eth-event
Version:        1.4.10
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Ethereum event decoder and topic generator

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/iamdefinitelyahuman/eth-event
Source:         %{pypi_source eth_event}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'eth-event' generated automatically by pyp2spec.}

Patch:         python-eth-event-0001-Relax-deps.patch

%description %_description

%package -n     python3-eth-event
Summary:        %{summary}

%description -n python3-eth-event %_description


%prep
%autosetup -p1 -n eth_event-%{version}


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


%files -n python3-eth-event -f %{pyproject_files}

%changelog
%autochangelog
