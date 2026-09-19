%global source0_hash none

Name:           python-dns-lexicon
Version:        3.25.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Manipulate DNS records on various DNS providers in a standardized/agnostic way

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://dns-lexicon.github.io/dns-lexicon/introduction.html
Source:         %{pypi_source dns_lexicon}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dns-lexicon' generated automatically by pyp2spec.}

Patch:          python-dns-lexicon-tox-config.patch

%description %_description

%package -n     python3-dns-lexicon
Summary:        %{summary}

%description -n python3-dns-lexicon %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-dns-lexicon full,gransy,localzone,oci,qcloud,route53,softlayer


%prep
%autosetup -p1 -n dns_lexicon-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x full,gransy,localzone,oci,qcloud,route53,softlayer


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-dns-lexicon -f %{pyproject_files}
%{_bindir}/lexicon

%changelog
%autochangelog
