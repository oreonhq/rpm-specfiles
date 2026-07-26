%global source0_hash 5b97353978b54d7315bc9690dbfdea0062cc2823d001dbcc035c3420df1ebe26

Name:           R-msm
Version:        %R_rpm_version 1.8.2
Release:        %autorelease
Summary:        Multi-state Markov and hidden Markov models in continuous time

# Automatically converted from old format: GPLv2+ and GPLv3+ - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Functions for fitting general continuous-time Markov and hidden Markov
multi-state models to longitudinal data.  Both Markov transition rates
and the hidden Markov output process can be modeled in terms of
covariates.  A variety of observation schemes are supported, including
processes observed at arbitrary times, completely-observed processes,
and censored states.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
