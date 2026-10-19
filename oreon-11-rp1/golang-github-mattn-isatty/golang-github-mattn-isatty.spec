%global source0_hash b4fe77aff60d7e9d2e6b626dd8acfbf63a651df72724318931f6ba0b4b7d3273
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mattn/go-isatty
Version:                0.0.24
%gometa
%global common_description %{expand:
Is a TTY? for Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Is a TTY? for Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-isatty-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
