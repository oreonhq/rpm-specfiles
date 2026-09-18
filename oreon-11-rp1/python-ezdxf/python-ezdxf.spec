%global source0_hash none

Name:           python-ezdxf
Version:        1.4.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python package to create/manipulate DXF drawings.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/mozman/ezdxf
Source:         %{pypi_source ezdxf}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ezdxf' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ezdxf
Summary:        %{summary}

%description -n python3-ezdxf %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ezdxf dev,dev5,draw,draw5


%prep
%autosetup -p1 -n ezdxf-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,dev5,draw,draw5


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-ezdxf -f %{pyproject_files}
%{_bindir}/ezdxf

%changelog
%autochangelog
