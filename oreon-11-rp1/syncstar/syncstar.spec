%global source0_hash ff256d37c3aabeab70340e07abdd2ea759195acbc7bd755af6bb9ba98f9ebe30

%global pack syncstar

Name:           %{pack}
Version:        0.2.2
Release:        6%{?dist}
Summary:        Service for creating bootable USB storage devices at community conference kiosks

# The syncstar project is licensed under AGPL-3.0-or-later license, except for the following files
#
# MIT license -
# syncstar/frontend/assets/index-*.css (Read here https://github.com/facebook/react)
# syncstar/frontend/assets/index-*.js (Read here https://github.com/facebook/react)
#
# OFL license -
# syncstar/frontend/assets/mono_*.ttf (Read here https://github.com/JetBrains/JetBrainsMono)
# syncstar/frontend/assets/sans_*.ttf (Read here https://github.com/rsms/inter)

License:        AGPL-3.0-or-later AND MIT
Url:            https://github.com/gridhead/%{pack}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       coreutils
Requires:       util-linux
Requires:       redis

%description
SyncStar lets users create bootable USB storage devices with the operating
system image of their choice. This application is intended to be deployed on
kiosk devices and electronic signages where conference guests and booth
visitors can avail its services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pack}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pack}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
