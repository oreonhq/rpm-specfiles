%global source0_hash 98db84bb0224a26094e6adba91b7ee7a1a7ace28cb648d818f8e779e6a19f825
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/beorn7/perks
Version:                1.0.1
%gometa
%global common_description %{expand:
Perks contains the Go package quantile that computes approximate quantiles over
an unbounded data stream within low memory and CPU bounds.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Effective computation of things
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/perks-%{version}.tar.gz
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
