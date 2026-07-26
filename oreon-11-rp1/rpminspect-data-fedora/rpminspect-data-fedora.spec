%global source0_hash 33c2d9ebbc168affe1e33d86cf6a852bbdc084d385f57745e9afe633c637175c

Name:           rpminspect-data-fedora
Version:        1.16
Release:        4%{?dist}
Epoch:          1
Summary:        Build deviation compliance tool data files
Group:          Development/Tools
License:        CC-BY-SA-4.0
URL:            https://codeberg.org/rpminspect/rpminspect-data-fedora
Source0:        https://codeberg.org/rpminspect/rpminspect-data-fedora/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build

Requires:       rpminspect >= 2.0

# Used by inspections enabled in the configuration file
Requires:       fedora-license-data >= 1.7
Requires:       xhtml1-dtds
Requires:       html401-dtds
Requires:       dash
Requires:       ksh
Requires:       zsh
Requires:       tcsh
Requires:       rc
Requires:       bash
Requires:       libabigail
Requires:       /usr/bin/annocheck

%description
Fedora Linux specific configuration file for rpminspect and data files
used by the inspections provided by librpminspect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
%meson
%meson_build

%install
%meson_install

%files
%license CC-BY-SA-4.0.txt
%doc AUTHORS.md README
%{_datadir}/rpminspect
%{_bindir}/rpminspect-fedora

%changelog
%autochangelog
