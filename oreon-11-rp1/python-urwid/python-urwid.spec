%global source0_hash none

Name:           python-urwid
Version:        4.1.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A full-featured console _xterm et al._ user interface library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-only
URL:            https://urwid.org/
Source:         %{pypi_source urwid}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'urwid' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-urwid
Summary:        %{summary}

%description -n python3-urwid %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-urwid curses,glib,lcd,serial,tornado,trio,twisted,zmq


%prep
%autosetup -p1 -n urwid-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x curses,glib,lcd,serial,tornado,trio,twisted,zmq


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-urwid -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.4-1
- Prepare for Oreon 11 (RP1)
