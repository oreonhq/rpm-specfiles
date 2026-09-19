%global source0_hash none

Name:           python-distributed
Version:        2026.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Distributed scheduler for Dask

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://distributed.dask.org
Source:         %{pypi_source distributed}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'distributed' generated automatically by pyp2spec.}

Patch:          0001-Increase-test-timeout-for-slower-architectures.patch
Patch:          0002-Install-test-packages.patch
Patch:          0003-Disable-warnings-as-errors-in-tests.patch
Patch:          0004-Loosen-up-some-dependencies.patch
Patch:          0005-Skip-doc-test-when-not-running-from-a-git-checkout.patch
Patch:          0006-Update-make_tls_certs.py-work-with-openssl-3-8701.patch
Patch:          0007-Avoid-using-sys.prefix-in-CLI-test.patch

%description %_description

%package -n     python3-distributed
Summary:        %{summary}

%description -n python3-distributed %_description


%prep
%autosetup -p1 -n distributed-%{version}


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


%files -n python3-distributed -f %{pyproject_files}

%changelog
%autochangelog
