%global source0_hash effdf6836ea847c61b764424ded1cf2aabb09ec087f3ecf41cadaa1e70a8ff33
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/vishvananda/netns
%global commit          18c4f4234207848a45d5e6b3fe8a754f4f37ea3c
%gometa
%global common_description %{expand:
The netns package provides an ultra-simple interface for handling network
namespaces in Go. Changing namespaces requires elevated privileges, so in most
cases this code needs to be run as root.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Simple network namespace handling for go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/netns-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
