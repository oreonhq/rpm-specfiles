%global source0_hash 140043804b4cfcb5e174af3a188ce4cd1e17f7f6aeb777bbd4da21f6c73e013c

Name:           R-credentials
Version:        %R_rpm_version 2.0.3
Release:        %autorelease
Summary:        Tools for Managing SSH and Git Credentials

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Setup and retrieve HTTPS and SSH credentials for use with 'git' and other
services. For HTTPS remotes the package interfaces the 'git-credential'
utility which 'git' uses to store HTTP usernames and passwords. For SSH
remotes we provide convenient functions to find or generate appropriate SSH
keys. The package both helps the user to setup a local git installation,
and also provides a back-end for git/ssh client libraries to authenticate
with existing user credentials.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
