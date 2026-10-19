%global source0_hash 10f3751ea3b5fde2cdf217e0789711bb078bb4caf3909ac1307ff6c35292f8c7
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/rs/zerolog
Version:                1.35.1
%gometa -L
%global common_description %{expand:
The Zerolog package provides a fast and simple logger dedicated to JSON output.
Zerolog's API is designed to provide both a great developer experience and
stunning performance. Its unique chaining API allows zerolog to write JSON (or
CBOR) log events by avoiding allocations and reflection.
Uber's zap library pioneered this approach. Zerolog is taking this concept to
the next level with a simpler to use API and even better performance.}
%global golicenses      LICENSE
%global godocs          README.md README-lint.md README-prettylog.md
Name:           golang-github-rs-zerolog
Release:        1%{?dist}
Summary:        Zero allocation JSON logger
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/zerolog-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

mv cmd/lint/README.md README-lint.md
mv cmd/prettylog/README.md README-prettylog.md

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck -d journald
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
