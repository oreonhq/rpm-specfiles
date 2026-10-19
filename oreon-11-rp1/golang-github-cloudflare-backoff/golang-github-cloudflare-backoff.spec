%global source0_hash 281cd79149d825fb578cbbfa8b070b77aabd4b2d7f38f38d5e66e40f34e69f65
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/cloudflare/backoff
%global commit          647f3cdfc87a18586e279c97afd6526d01b0d063
%gometa
%global common_description %{expand:
This package implements the backoff strategy described in the AWS Architecture
Blog article "Exponential Backoff And Jitter". Essentially, the backoff has an
interval time.Duration; the nth call to backoff will return an a time.Duration
that is 2 n * interval. If jitter is enabled (which is the default behaviour),
the duration is a random value between 0 and 2 n * interval. The backoff is
configured with a maximum duration that will not be exceeded; e.g., by default,
the longest duration returned is backoff.DefaultMaxDuration.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Backoff timer shared between several projects
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/backoff-%{commit}.tar.gz
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
