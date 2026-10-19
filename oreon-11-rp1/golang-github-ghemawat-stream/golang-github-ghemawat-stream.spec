%global source0_hash 58170f6c07359a3e2ca6a1dfe2085d84ad5ea2903e5ba53e36e0e5ce2a4f5e8d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ghemawat/stream
%global commit          696b145b53b9611fe9c9f189122f990171e391a0
%gometa
%global common_description %{expand:
Package stream provides filters that can be chained together in a manner
similar to Unix pipelines.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Filters that can be chained together similar to Unix pipelines
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/stream-%{commit}.tar.gz
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

rm -rfv stream_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
