%global source0_hash 2dcd0ec453f5ec4d96f69b0c472569d57d3c5f9956a82a48492ee02f12071137
Name:           R-filelock
Version:        %R_rpm_version 1.0.3
Release:        1%{?dist}
Summary:        Portable File Locking
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=filelock&version=%{version}#/filelock_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Place an exclusive or shared lock on a file. It uses 'LockFile' on Windows and
'fcntl' locks on Unix-like systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
