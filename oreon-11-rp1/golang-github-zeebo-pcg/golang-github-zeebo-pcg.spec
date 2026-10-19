%global source0_hash 200dadedb81875c652bb439604d7ba4e25e88bd88640e4de708b1e0616d6992e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zeebo/pcg
Version:                1.0.1
%gometa
%global common_description %{expand:
PCG random number generator.}
%global golicenses      LICENSE
%global godocs          README.txt
Name:           %{goname}
Release:        1%{?dist}
Summary:        PCG random number generator
License:        CC0-1.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pcg-%{version}.tar.gz
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
