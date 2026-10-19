%global source0_hash 8b2a053a02826198ec29baf3e4b89bda313656d9d959def873bfa4be0c94d845
Name:           R-gert
Version:        %R_rpm_version 2.3.1
Release:        1%{?dist}
Summary:        Simple Git Client for R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gert&version=%{version}#/gert_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(libgit2)
# /oreon:deps
%description
Simple git client for R based on 'libgit2' with support for SSH and HTTPS
remotes. All functions in 'gert' use basic R data types (such as vectors
and data-frames) for their arguments and return values. User credentials
are shared with command line 'git' through the git-credential store and ssh
keys stored on disk or ssh-agent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
export USE_SYSTEM_LIBGIT2=1
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
