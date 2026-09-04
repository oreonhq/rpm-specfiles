%global source0_hash 26338ee8f6a6d9ba24ef067e875424b90efdfd6cd6f827f174151c8f2b77a555

Name:           yle-dl
Version:        20260716
Release:        %autorelease
Summary:        Download videos from Yle servers

License:        GPL-3.0-or-later
URL:            https://aajanki.github.io/yle-dl/index-en.html
Source:         https://github.com/aajanki/%{name}/archive/releases/%{version}/%{name}-%{version}.tar.gz
Patch:          0000-Revert-New-style-license-metadata.patch
Patch:          https://github.com/aajanki/%{name}/pull/391.patch

BuildArch:      noarch
# Depends on archful python3-xattr which excludes i686
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  /usr/bin/ffmpeg
Requires:       /usr/bin/ffmpeg
Recommends:     yle-dl+extra
# According to README, "required for podcasts".
Recommends:     wget

%description
Command-line program for downloading media files from the video streaming
services of the Finnish national broadcasting company Yle: Yle Areena,
Elävä arkisto, and Yle news. The videos are saved in Matroska (.mkv) or MP4
format.

# Enables storing video metadata as extended file attributes
# and automatically detecting filesystems that require restricted character sets.
%pyproject_extras_subpkg -n yle-dl extra

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-releases-%{version}

%generate_buildrequires
%pyproject_buildrequires -x extra -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files yledl

%check
%pytest --ignore=tests/integration

%files -f %{pyproject_files}
%doc README.*
%license COPYING
%{_bindir}/yle-dl

%changelog
%autochangelog
