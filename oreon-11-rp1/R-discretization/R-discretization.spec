%global source0_hash f3ce4851e1c1e388cafd5b195c8bb833cfcab13e691984066b23fe1c33887d4a
Name:           R-discretization
Version:        %R_rpm_version 1.0-1.1
Release:        1%{?dist}
Summary:        Data Preprocessing, Discretization for Classification
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=discretization&version=1.0-1.1#/discretization_1.0-1.1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A collection of supervised discretization algorithms. It can also
be grouped in terms of top-down or bottom-up, implementing
the discretization algorithms.

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
