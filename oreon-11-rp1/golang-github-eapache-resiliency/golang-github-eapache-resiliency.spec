%global source0_hash 9f84d71fae41cdcd2acedb9fe17ebe7659e1b2cf734be6b2d7135a0aab8f2649
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/eapache/go-resiliency
Version:                1.7.0
%gometa
%global common_description %{expand:
Resiliency patterns for golang.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Resiliency patterns for golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-resiliency-%{version}.tar.gz
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
