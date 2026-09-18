%global source0_hash none

Name:           python-pymupdf
Version:        1.28.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A high performance Python library for data extraction, analysis, conversion _ manipulation of PDF _and other_ documents.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pymupdf/pymupdf
Source:         %{pypi_source pymupdf}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pymupdf' generated automatically by pyp2spec.}

Patch:		0001-fix-test_-font.patch
Patch:		0001-test_pixmap-adjust-to-turbojpeg.patch
Patch:		0001-setup.py-do-not-require-libclang-and-swig.patch
Patch:		0001-tests-adjust-to-verbose-font-warning.patch
Patch:		0001-adjust-tests-to-tesseract-5.5.1.patch
Patch:		0001-tests-conftest-do-not-call-pip.patch

%description %_description

%package -n     python3-pymupdf
Summary:        %{summary}

%description -n python3-pymupdf %_description


%prep
%autosetup -p1 -n pymupdf-%{version}


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


%files -n python3-pymupdf -f %{pyproject_files}
%{_bindir}/pymupdf

%changelog
%autochangelog
