%global source0_hash 9b79d3bf6a4c0274ec5e25e77b382985ea770401b7a1553df9c35184290a0d1f

%global github_owner    poeml
%global github_name     withlock
%global github_commit   6ffda60e1c91c591ebab41e18a4c5f1e58980f4e

Name:           withlock
Version:        0.5
Release:        22%{?dist}
Summary:        Locking wrapper script

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{version}.tar.gz
# Specify /usr/bin/python3 to ensure use of py3
Patch0:         withlock-0.5-python3.patch
BuildArch:      noarch
BuildRequires:  gzip
Requires:       python3

%description
withlock is a locking wrapper script to make sure that some program
isn't run more than once. It is ideal to prevent periodic jobs spawned
by cron from stacking up.

The locks created are valid only while the wrapper is running, and
thus will never require additional cleanup, even after a reboot. This
makes the wrapper safe and easy to use, and much better than
implementing half-hearted locking within scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{github_name}-%{github_commit}

%build
# No build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m 0755 withlock %{buildroot}%{_bindir}
install -m 0644 withlock.1 %{buildroot}%{_mandir}/man1
gzip %{buildroot}%{_mandir}/man1/withlock.1

%files
%license LICENSE-2.0.txt
%doc README.md
%{_bindir}/withlock
%{_mandir}/man1/withlock.1*

%changelog
%autochangelog
