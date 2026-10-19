%global source0_hash 6c2106a74c44a748f2cea795d9686e27a0058a90debcfd8558b62b06aec0c7dd
Name:           R-askpass
Version:        %R_rpm_version 1.2.1
Release:        1%{?dist}
Summary:        Safe Password Entry for R, Git, and SSH
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=askpass&version=%{version}#/askpass_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Cross-platform utilities for prompting the user for credentials or a
passphrase, for example to authenticate with a server or read a protected key.
Includes native programs for MacOS and Windows, hence no 'tcltk' is required.
Password entry can be invoked in two different ways: directly from R via the
askpass() function, or indirectly as password-entry back-end for 'ssh-agent' or
'git-credential' via the SSH_ASKPASS and GIT_ASKPASS environment variables.
Thereby the user can be prompted for credentials or a passphrase if needed when
R calls out to git or ssh.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm askpass/inst/mac-* # macOS stuff

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
