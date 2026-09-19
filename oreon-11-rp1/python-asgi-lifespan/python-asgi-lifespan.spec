%global source0_hash 5e2effaf0bfe39829cf2d64e7ecc47c7d86d676a6599f7afba378c31f5e3a308

Name:           python-asgi-lifespan
Version:        2.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Programmatic startup/shutdown of ASGI apps.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/florimondmanca/asgi-lifespan
Source:         %{pypi_source asgi-lifespan}

BuildArch:      noarch
BuildRequires:  python3-devel

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'asgi-lifespan' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-asgi-lifespan
Summary:        %{summary}

%description -n python3-asgi-lifespan %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n asgi-lifespan-%{version}

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

%files -n python3-asgi-lifespan -f %{pyproject_files}

%changelog
%autochangelog
