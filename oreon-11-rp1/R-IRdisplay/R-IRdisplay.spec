%global source0_hash 83eb030ff91f546cb647899f8aa3f5dc9fe163a89a981696447ea49cc98e8d2b
Name:           R-IRdisplay
Version:        %R_rpm_version 1.1
Release:        1%{?dist}
Summary:        'Jupyter' Display Machinery
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=IRdisplay&version=%{version}#/IRdisplay_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
 An interface to the rich display capabilities of 'Jupyter' front-ends
(e.g. 'Jupyter Notebook') <https://jupyter.org>. Designed to be used from a
running 'IRkernel' session <https://irkernel.github.io>.

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
