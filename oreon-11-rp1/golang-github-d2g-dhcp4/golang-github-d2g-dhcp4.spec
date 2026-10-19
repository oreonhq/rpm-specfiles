%global source0_hash 9bff835383c5fc07089f0458dfb2533f4d5a0f0da59967fdc988ed505e5d13b3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/d2g/dhcp4
%global commit          a1d1b6c41b1ce8a71a5121a9cee31809c4707d9c
%gometa
%global common_description %{expand:
A DHCP library written in Go.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        DHCP4 library written in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/dhcp4-%{commit}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
