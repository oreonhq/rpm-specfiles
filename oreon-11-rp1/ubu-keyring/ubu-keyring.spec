%global source0_hash aecd455ae15561371d6e454f121f079f0641d5e1b579a5563a2bc363fc74aa2e

Name:           ubu-keyring
Version:        2023.11.28.1
Release:        6%{?dist}
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
