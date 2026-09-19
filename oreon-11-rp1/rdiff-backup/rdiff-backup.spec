%global source0_hash d0778357266bc6513bb7f75a4570b29b24b2760348bbf607babfc3a6f09458cf

%global gittag 2.2.6

Version: %{gittag}
Summary: Convenient and transparent local/remote incremental mirror/backup
Name: rdiff-backup
Release: 13%{?dist}

URL: https://rdiff-backup.net/
Source0: https://github.com/%{name}/%{name}/releases/download/v%{gittag}/%{name}-%{version}.tar.gz

License: GPL-2.0-or-later
BuildRequires: python3-devel >= 3.6, librsync-devel >= 1.0.0
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: gcc

#recommended runtime dependencies
Recommends: py3libacl
Recommends: python3-pyxattr
Recommends: python3-psutil

%description
rdiff-backup is a script, written in Python, that backs up one
directory to another and is intended to be run periodically (nightly
from cron for instance). The target directory ends up a copy of the
source directory, but extra reverse diffs are stored in the target
directory, so you can still recover files lost some time ago. The idea
is to combine the best features of a mirror and an incremental
backup. rdiff-backup can also operate in a bandwidth efficient manner
over a pipe, like rsync. Thus you can use rdiff-backup and ssh to
securely back a hard drive up to a remote location, and only the
differences from the previous backup will be transmitted.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

# Remove doc files so we package them with rpmbuild
rm -rf $RPM_BUILD_ROOT/usr/share/doc/*

%files
%defattr(-,root,root)
%{_bindir}/rdiff-backup
%{_bindir}/rdiff-backup-statistics
%{_bindir}/rdiff-backup-delete
%{_mandir}/man1/rdiff-backup*
%{python3_sitearch}/rdiff_backup/
%{python3_sitearch}/rdiff_backup-*.egg-info
%{python3_sitearch}/rdiffbackup/
%{_datadir}/bash-completion/completions/rdiff-backup
%doc CHANGELOG.adoc README.adoc
%doc docs/credits.adoc docs/DEVELOP.adoc docs/examples.adoc
%doc docs/FAQ.adoc docs/migration.adoc
%license COPYING

%changelog
%autochangelog
