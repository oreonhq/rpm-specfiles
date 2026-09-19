%global source0_hash 2d019c3fa19c42da4d37571e473c296286dad0214cb3bd5cafd99f04a8bf5471

%global upstreamname debian-archive-keyring

Name:           debian-keyring
Version:        2025.1
Release:        4%{?dist}
Summary:        GnuPG archive keys of the Debian archive

License:        LicenseRef-Fedora-Public-Domain
URL:            http://packages.debian.org/unstable/admin/%{upstreamname}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{upstreamname}/%{upstreamname}_%{version}.tar.xz
# Use gpg2
Patch0:         debian-keyring_gpg2.patch

BuildArch:      noarch
BuildRequires:  jetring
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  keyrings-filesystem
Requires:       keyrings-filesystem

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

%files
%doc README
%exclude %{_sysconfdir}/apt/trusted.gpg.d
%{_keyringsdir}/*.gpg
%{_keyringsdir}/*.pgp

%changelog
%autochangelog
