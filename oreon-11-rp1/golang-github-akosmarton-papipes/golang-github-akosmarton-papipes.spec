%global source0_hash 6007b24e08742e0593f449aab209fc0f13dc5fbeced11095867dae2acc654a1a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/akosmarton/papipes
%global commit          3c63b4919c769c9c2b2d07e69a98abb0eb47fe64
%gometa -L -f
%global common_description %{expand:
Pulseaudio client library in Golang for creating virtual sinks and sources.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           golang-github-akosmarton-papipes
Version:        0
Release:        1%{?dist}
Summary:        Pulseaudio library for creating virtual sinks and sources
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/papipes-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
