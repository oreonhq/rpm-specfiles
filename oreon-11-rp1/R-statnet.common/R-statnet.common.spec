%global source0_hash 66787cbada206c85d884af5ffa234aedec9aa96634230380322a30c7951dd33f
Name:           R-statnet.common
Version:        %R_rpm_version 4.13.0
Release:        1%{?dist}
Summary:        Common R Scripts and Utilities Used by the Statnet Project Software
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=statnet.common&version=%{version}#/statnet.common_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Non-statistical utilities used by the software developed by the Statnet
Project. They may also be of use to others.

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
