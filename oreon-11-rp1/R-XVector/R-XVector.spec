%global source0_hash c963d04bd4c5c0387c401158408e02a08f1e9051124cae4154045c903c8be390
Name:           R-XVector
Version:        %R_rpm_version 0.50.0
Release:        1%{?dist}
Summary:        Representation and manipulation of external sequences
License:        Artistic-2.0
URL:            %{bioc_url}
Source0:        https://bioconductor.org/packages/3.22/bioc/src/contrib/XVector_0.50.0.tar.gz
Obsoletes:      %{name}-devel <= 0.50.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Memory efficient S4 classes for storing sequences "externally" (behind an R
external pointer, or on disk).

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
