%global source0_hash none

Name:           python-onionbalance
Version:        0.2.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Onionbalance provides load-balancing and redundancy for Tor hidden services by distributing requests to multiple backend Tor instances.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL
URL:            https://gitlab.torproject.org/tpo/onion-services/onionbalance/
Source:         %{pypi_source onionbalance}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'onionbalance' generated automatically by pyp2spec.}

Patch0:         python-onionbalance-fix-versioneer.patch
Patch1:         drop-dependency-on-future.patch

%description %_description

%package -n     python3-onionbalance
Summary:        %{summary}

%description -n python3-onionbalance %_description


%prep
%autosetup -p1 -n onionbalance-%{version}


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


%files -n python3-onionbalance -f %{pyproject_files}
%{_bindir}/onionbalance
%{_bindir}/onionbalance-config

%changelog
%autochangelog
