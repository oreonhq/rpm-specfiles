%global source0_hash e808d2c8e4237cbff79fc0dab516868c8de64cab898f60beedffb87fbc570fc9

Name:		comps-extras
Version:	24
Release:	22%{?dist}
Summary:	Images for package groups

# while GPL isn't normal for images, it is the case here
# No version specified.
# KDE logo is LGPLv2+
# LXDE logo is GPLv2+
# MATE logo is GPLv2+
# Cinnamon logo is taken from getfedora.org and thus CC-BY-SA
# Haskell logo is a variation on MIT/X11
# Sugar and Ruby logos are CC-BY-SA
# See COPYING for more details
# Automatically converted from old format: GPL+ and LGPLv2+ and GPLv2+ and CC-BY-SA and MIT - review is highly recommended.
License:	GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT
URL:		https://pagure.io/%{name}
Source0:	https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	fdupes
BuildRequires: make

%description
This package contains images for the components included in this distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%make_build

%install
%make_install
%fdupes -s %{buildroot}%{_datadir}/pixmaps

%files
%doc comps.dtd comps-cleanup.xsl
%license COPYING
%{_datadir}/pixmaps/comps

%changelog
%autochangelog
