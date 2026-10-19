%global source0_hash 32c2931992fbec9c31b71de3e27059f1cbb45b4b1f45fd42e0e8dbcec6de3be9
Name:           R-clipr
Version:        %R_rpm_version 0.8.0
Release:        1%{?dist}
Summary:        Read and Write from the System Clipboard
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=clipr&version=%{version}#/clipr_%{version}.tar.gz
BuildArch:      noarch
Requires:       xsel
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Simple utility functions to read from and write to the Windows, OS X, and
X11 clipboards.

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
