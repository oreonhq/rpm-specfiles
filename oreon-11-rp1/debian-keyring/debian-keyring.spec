%global source0_hash 2d019c3fa19c42da4d37571e473c296286dad0214cb3bd5cafd99f04a8bf5471
%global upstreamname debian-archive-keyring
Name:           debian-keyring
Version:        2025.1
Release:        1%{?dist}
Summary:        GnuPG archive keys of the Debian archive
License:        LicenseRef-Fedora-Public-Domain
URL:            http://packages.debian.org/unstable/admin/%{upstreamname}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{upstreamname}/%{upstreamname}_%{version}.tar.xz
Patch0:         debian-keyring_gpg2.patch
BuildArch:      noarch
Requires:       keyrings-filesystem
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  jetring
BuildRequires:  keyrings-filesystem
BuildRequires:  make
# /oreon:deps
%description
The Debian project digitally signs its Release files. This package contains the
archive keys used for that.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}

%build

make
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
