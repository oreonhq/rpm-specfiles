%global source0_hash 5223a689f315fc53c5bc271b3a8259032cc74f5311a6d7c1f700a1c65d40c2b2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jtolds/gls
Version:                4.20.0
%gometa
%global common_description %{expand:
Package Gls implements goroutine-local storage.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Goroutine local storage
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gls-%{version}.tar.gz
Source1:        glide.lock
Source2:        glide.yaml
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
