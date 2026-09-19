%global source0_hash none

Name:           python-oletools
Version:        0.60.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python tools to analyze security characteristics of MS Office and OLE files _also called Structured Storage, Compound File Binary Format or Compound Document File Format_, for Malware Analysis and Incident Response #DFIR

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/decalage2/oletools
Source:         %{pypi_source oletools %{version} zip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oletools' generated automatically by pyp2spec.}

Patch0:         %{name}-01-thirdparty.patch

%description %_description

%package -n     python3-oletools
Summary:        %{summary}

%description -n python3-oletools %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-oletools full


%prep
%autosetup -p1 -n oletools-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x full


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-oletools -f %{pyproject_files}
%{_bindir}/ezhexviewer
%{_bindir}/ftguess
%{_bindir}/mraptor
%{_bindir}/msodde
%{_bindir}/olebrowse
%{_bindir}/oledir
%{_bindir}/olefile
%{_bindir}/oleid
%{_bindir}/olemap
%{_bindir}/olemeta
%{_bindir}/oleobj
%{_bindir}/oletimes
%{_bindir}/olevba
%{_bindir}/pyxswf
%{_bindir}/rtfobj

%changelog
%autochangelog
