%global source0_hash 26338ee8f6a6d9ba24ef067e875424b90efdfd6cd6f827f174151c8f2b77a555
Name:           yle-dl
Version:        20260716
Release:        1%{?dist}
Summary:        Download videos from Yle servers
License:        GPL-3.0-or-later
URL:            https://aajanki.github.io/yle-dl/index-en.html
Source0:        https://github.com/aajanki/%{name}/archive/releases/%{version}/%{name}-%{version}.tar.gz
Patch:          0000-Revert-New-style-license-metadata.patch
Patch:          https://github.com/aajanki/%{name}/pull/391.patch
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       /usr/bin/ffmpeg
Recommends:     yle-dl+extra
Recommends:     wget
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-yle-dl = %{version}-%{release}
# /oreon:deps
%package -n       python3-yle-dl+extra
Summary:        Metapackage for python3-yle-dl extra extras
Requires:       python3-yle-dl = %{version}-%{release}
Provides:       python3dist(yle-dl[extra]) = %{version}-%{release}

%description -n python3-yle-dl+extra
Metapackage for python3-yle-dl extra extras.

%description
Command-line program for downloading media files from the video streaming
services of the Finnish national broadcasting company Yle: Yle Areena,
Elävä arkisto, and Yle news. The videos are saved in Matroska (.mkv) or MP4
format.

# Enables storing video metadata as extended file attributes
# and automatically detecting filesystems that require restricted character sets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-releases-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest --ignore=tests/integration
%files

%changelog

%autochangelog
