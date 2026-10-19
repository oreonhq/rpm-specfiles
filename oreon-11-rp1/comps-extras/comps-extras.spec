%global source0_hash e808d2c8e4237cbff79fc0dab516868c8de64cab898f60beedffb87fbc570fc9
Name:		comps-extras
Version:	24
Release:        22%{?dist}
Summary:        Images for package groups
License:	GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT
URL:		https://pagure.io/%{name}
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  fdupes
BuildRequires:  make
# /oreon:deps
%description
This package contains images for the components included in this distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install
%fdupes -s %{buildroot}%{_datadir}/pixmaps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
