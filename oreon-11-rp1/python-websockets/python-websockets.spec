%global source0_hash none

Name:           python-websockets
Version:        17.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        An implementation of the WebSocket Protocol _RFC 6455 _ 7692_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/python-websockets/websockets
Source:         %{pypi_source websockets}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'websockets' generated automatically by pyp2spec.}

Patch:          https://github.com/python-websockets/websockets/commit/3128f5619d.patch
Patch:          https://github.com/python-websockets/websockets/pull/1639.patch
Patch:          https://github.com/python-websockets/websockets/commit/036fd45c16afec1b713ae7f37393c76c3ff528a5.patch

%description %_description

%package -n     python3-websockets
Summary:        %{summary}

%description -n python3-websockets %_description


%prep
%autosetup -p1 -n websockets-%{version}


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


%files -n python3-websockets -f %{pyproject_files}
%{_bindir}/websockets

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.0.1-1
- Prepare for Oreon 11 (RP1)
