%global source0_hash f06ffd583a7526331dcbb65083c9c754a76595cd4b226acccc93ecae6173ad1a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xrash/smetrics
%global commit          039620a656736e6ad994090895784a7af15e0b80
%gometa
%global common_description %{expand:
This library contains implementations of the Levenshtein distance, Jaro-Winkler
and Soundex algorithms written in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        String metrics library written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/smetrics-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
