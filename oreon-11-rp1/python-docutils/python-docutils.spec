%global source0_hash none

Name:           python-docutils
Version:        0.23
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Docutils -- Python Documentation Utilities

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://docutils.sourceforge.io
Source:         %{pypi_source docutils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'docutils' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-docutils
Summary:        %{summary}

%description -n python3-docutils %_description


%prep
%autosetup -p1 -n docutils-%{version}


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


%files -n python3-docutils -f %{pyproject_files}
%{_bindir}/docutils
%{_bindir}/rst2html
%{_bindir}/rst2html4
%{_bindir}/rst2html5
%{_bindir}/rst2latex
%{_bindir}/rst2man
%{_bindir}/rst2odt
%{_bindir}/rst2pseudoxml
%{_bindir}/rst2s5
%{_bindir}/rst2xetex
%{_bindir}/rst2xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.4-1
- Prepare for Oreon 11 (RP1)
