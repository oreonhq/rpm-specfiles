%global source0_hash 873e979323df6060cb4f843bc920f07fa59c05002359bf5d4a3311c8911f6640
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/blang/semver
Version:                4.0.0
%gometa
%global common_description %{expand:
Semver is a Semantic Versioning library written in Go. It fully covers spec
version 2.0.0.}
%global golicenses      LICENSE
%global godocs          examples README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Semantic Versioning library written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/semver-%{version}.tar.gz
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
