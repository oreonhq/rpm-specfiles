%global source0_hash none

Name:           python-wxpython
Version:        4.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Cross platform GUI toolkit for Python, _Phoenix_ version

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://wxPython.org/
Source:         %{pypi_source wxpython}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'wxpython' generated automatically by pyp2spec.}

Patch:          fix-ftbfs-doxygen-1.15.0.patch

%description %_description

%package -n     python3-wxpython
Summary:        %{summary}

%description -n python3-wxpython %_description


%prep
%autosetup -p1 -n wxpython-%{version}


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


%files -n python3-wxpython -f %{pyproject_files}
%{_bindir}/helpviewer
%{_bindir}/img2png
%{_bindir}/img2py
%{_bindir}/img2xpm
%{_bindir}/pycrust
%{_bindir}/pyshell
%{_bindir}/pyslices
%{_bindir}/pyslicesshell
%{_bindir}/pywxrc
%{_bindir}/wxdemo
%{_bindir}/wxdocs
%{_bindir}/wxget

%changelog
%autochangelog
