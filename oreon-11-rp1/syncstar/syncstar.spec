%global source0_hash 24c2f30800e3505c3d71bafbe11269cc63f40131ca353017141af4edceb62805
%global pack syncstar
Name:           %{pack}
Version:        0.2.2
Release:        6%{?dist}
Summary:        Service for creating bootable USB storage devices at community conference kiosks
License:        AGPL-3.0-or-later AND MIT
Url:            https://github.com/gridhead/%{pack}
Source0:        https://files.pythonhosted.org/packages/source/s/syncstar/syncstar-%{version}.tar.gz
BuildArch:      noarch
Requires:       coreutils
Requires:       util-linux
Requires:       redis
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-syncstar = %{version}-%{release}
# /oreon:deps
%description
SyncStar lets users create bootable USB storage devices with the operating
system image of their choice. This application is intended to be deployed on
kiosk devices and electronic signages where conference guests and booth
visitors can avail its services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pack}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
