%global source0_hash 8b2a053a02826198ec29baf3e4b89bda313656d9d959def873bfa4be0c94d845

Name:           R-gert
Version:        %R_rpm_version 2.3.1
Release:        %autorelease
Summary:        Simple Git Client for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libgit2)

%description
Simple git client for R based on 'libgit2' with support for SSH and HTTPS
remotes. All functions in 'gert' use basic R data types (such as vectors
and data-frames) for their arguments and return values. User credentials
are shared with command line 'git' through the git-credential store and ssh
keys stored on disk or ssh-agent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
export USE_SYSTEM_LIBGIT2=1
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
