%global source0_hash 5b97353978b54d7315bc9690dbfdea0062cc2823d001dbcc035c3420df1ebe26
Name:           R-msm
Version:        %R_rpm_version 1.8.2
Release:        1%{?dist}
Summary:        Multi-state Markov and hidden Markov models in continuous time
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=msm&version=%{version}#/msm_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Functions for fitting general continuous-time Markov and hidden Markov
multi-state models to longitudinal data.  Both Markov transition rates
and the hidden Markov output process can be modeled in terms of
covariates.  A variety of observation schemes are supported, including
processes observed at arbitrary times, completely-observed processes,
and censored states.

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
