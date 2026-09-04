%global source0_hash 652d6b53b7fd676e7d45e99076ebd44624d477f3883c1bcb7bcf6f2855cdf7c4

Name:           ubu-keyring
Version:        2026.08.18
Release:        1%{?dist}
Summary:        GnuPG keys of the Ubuntu archive

License:        LicenseRef-Fedora-Public-Domain
URL:            https://launchpad.net/ubuntu-keyring
Source0:        https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-keyring_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  keyrings-filesystem
Requires:       keyrings-filesystem

%description
The Ubuntu project digitally signs its Release files. This package contains the
archive keys used for that, in a minimal form for use in the installer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ubuntu-keyring

%build

%install
install -d %{buildroot}%{_keyringsdir}
[ ! -s keyrings/ubuntu-archive-removed-keys.gpg ] && rm keyrings/ubuntu-archive-removed-keys.gpg
cp -a keyrings/* %{buildroot}%{_keyringsdir}

%files
%doc README
%{_keyringsdir}/*.gpg

%changelog
%autochangelog
