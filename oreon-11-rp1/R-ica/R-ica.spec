%global source0_hash 474d3530b16b76a1bf1a1114d24092678ea7215fa57c6fdcee6333f1e768b865
Name:           R-ica
Version:        %R_rpm_version 1.0-3
Release:        1%{?dist}
Summary:        Independent Component Analysis
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=ica&version=1.0-3#/ica_1.0-3.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Independent Component Analysis (ICA) using various algorithms:
FastICA, Information-Maximization (Infomax), and Joint
Approximate Diagonalization of Eigenmatrices (JADE).

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
