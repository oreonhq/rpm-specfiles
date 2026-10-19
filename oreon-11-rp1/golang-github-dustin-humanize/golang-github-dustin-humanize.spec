%global source0_hash 103ef7f1ce7f8fbf72c054aad46b6848026f7eb2634913cb4dc1b386dd05a298
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/dustin/go-humanize
Version:                1.1.0
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-dustin-go-humanize-devel < 1.0.0-2
}
%global common_description %{expand:
Package humanize converts boring ugly numbers to human-friendly strings and
back.
Durations can be turned into strings such as "3 days ago", numbers representing
sizes like 82854982 into useful strings like, "83 MB" or "79 MiB" (whichever you
prefer).}
%global golicenses      LICENSE
%global godocs          README.markdown
Name:           %{goname}
Release:        1%{?dist}
Summary:        Formatters for units to human friendly sizes
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-humanize-%{version}.tar.gz
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
