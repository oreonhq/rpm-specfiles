%global source0_hash 49d8089e6831ad0370f827c74d531c0ffcdafcaf8574358977949b49f74fade3
Name:           btrfs-sxbackup
Version:        0.6.11
Release:        1%{?dist}
Summary:        Incremental btrfs snapshot backups with push/pull support via SSH
License:        GPL-2.0-only
URL:            https://github.com/masc3d/btrfs-sxbackup
Source0:        https://github.com/masc3d/btrfs-sxbackup/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         btrfs-sxbackup-manpages.patch
Patch1:         btrfs-sxbackup-tests.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-btrfs-sxbackup = %{version}-%{release}
# /oreon:deps
%description
Btrfs snapshot backup utility with push/pull support via SSH, retention, Email
notifications, compression of transferred data, and syslog logging.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -d %{buildroot}/%{_mandir}/man1
install -p -m644 man/* %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_sysconfdir}
install -p -m644 etc/btrfs-sxbackup.conf %{buildroot}/%{_sysconfdir}
%oreon_autofiles main

%check

%python3 -m unittest discover -v -s btrfs_sxbackup/tests -p "Test*.py"
%files

%changelog

%autochangelog
