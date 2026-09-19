%global source0_hash e626a8d158aaf1fd5ebc058cbda5e8553e471f5d8520b4c6f78a9b2adab271ca

Summary:   Backup over network to multiple incremental archives
Name:      bontmia
Version:   0.14
Release:   39%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:   GPL-2.0-only
URL:       http://folk.uio.no/johnen/bontmia/
Source0:   http://folk.uio.no/johnen/%{name}/%{name}-%{version}.tar.gz
Patch0:    bontmia-0.14-mktemp.patch
Patch1:    bontmia-0.14-cp-al.patch
Requires:  bind-utils
Requires:  coreutils
Requires:  findutils
Requires:  grep
Requires:  hostname
Requires:  openssh-clients
Requires:  perl-interpreter
Requires:  rsync
Requires:  sed
BuildArch: noarch
%description
A disk based backup system which provides a complete snapshot of
backed up directories. Using a clever hardlink and rsync trick,
the backup is fast and space efficient.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
#empty

%install
install -D -p -m 0755 bontmia %{buildroot}%{_bindir}/bontmia

%files
%doc COPYING README
%{_bindir}/bontmia

%changelog
%autochangelog
