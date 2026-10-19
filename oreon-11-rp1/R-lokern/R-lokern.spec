%global source0_hash 6c71ef9fff25078010b2bba34f418f1d62402de2a54f7563d911db5bf0acd577
Name:           R-lokern
Version:        %R_rpm_version 1.1-12
Release:        1%{?dist}
Summary:        Kernel Regression Smoothing with Local or Global Plug-in Bandwidth
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=lokern&version=1.1-12#/lokern_1.1-12.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Kernel regression smoothing with adaptive local or global plug-in bandwidth
selection.

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
