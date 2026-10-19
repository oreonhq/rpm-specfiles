%global source0_hash 520882a7cdfa63920471b710261c059c09252bf9c38995073b7c84c5726e6b49
Name:           R-unix
Version:        %R_rpm_version 1.5.9
Release:        1%{?dist}
Summary:        POSIX System Utilities
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=unix&version=%{version}#/unix_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Bindings to system utilities found in most Unix systems such as POSIX functions
which are not part of the Standard C Library.

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
