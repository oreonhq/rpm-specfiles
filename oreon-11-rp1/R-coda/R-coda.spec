%global source0_hash f4b451d86fbb56ff9ade043ddd6b0944368c37d0dad12d02837750ecdc708ad6
Name:           R-coda
Version:        %R_rpm_version 0.19-4.1
Release:        1%{?dist}
Summary:        Output Analysis and Diagnostics for MCMC
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=coda&version=0.19-4.1#/coda_0.19-4.1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides functions for summarizing and plotting the output from Markov
Chain Monte Carlo (MCMC) simulations, as well as diagnostic tests of
convergence to the equilibrium distribution of the Markov chain.

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
