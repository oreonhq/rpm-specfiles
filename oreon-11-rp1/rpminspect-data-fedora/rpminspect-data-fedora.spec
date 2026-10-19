%global source0_hash 97fe5c2ec0f1aa23524d3460726bb6f5613de70a73c4a0395dac182598ddfe71
Name:           rpminspect-data-fedora
Version:        1.16
Release:        1%{?dist}
Epoch:          1
Summary:        Build deviation compliance tool data files
Group:          Development/Tools
License:        CC-BY-SA-4.0
URL:            https://codeberg.org/rpminspect/rpminspect-data-fedora
Source0:        https://codeberg.org/rpminspect/rpminspect-data-fedora/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       rpminspect >= 2.0
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
# oreon:deps
BuildRequires:  meson
BuildRequires:  ninja-build
# /oreon:deps
%description
Fedora Linux specific configuration file for rpminspect and data files
used by the inspections provided by librpminspect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
