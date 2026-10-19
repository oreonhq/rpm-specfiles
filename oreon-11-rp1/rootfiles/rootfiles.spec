%global source0_hash none
Summary:        The basic required files for the root user's directory
Name: rootfiles
Version: 9.0
Release:        1%{?dist}
License: LicenseRef-Not-Copyrightable
Source0:        dot-bashrc
Source1: dot-bash_profile
Source2: dot-bash_logout
Source3: dot-tcshrc
Source4: dot-cshrc
Source5: rootfiles.conf
%define ROOTFILES_DIR %{_datadir}/rootfiles
BuildArch: noarch
# oreon:deps
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The rootfiles package contains basic required files that are placed
in the root user's account.  These files are basically the same
as those in /etc/skel, which are placed in regular
users' home directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%install
mkdir -p $RPM_BUILD_ROOT/%{ROOTFILES_DIR}
install -D -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_tmpfilesdir}/rootfiles.conf
for file in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ; do
  f=`basename $file`
  install -p -m 644 $file $RPM_BUILD_ROOT/%{ROOTFILES_DIR}/${f/dot-/.}
done
%oreon_autofiles main

%posttrans

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0-1
- Prepare for Oreon 11 (RP1)
