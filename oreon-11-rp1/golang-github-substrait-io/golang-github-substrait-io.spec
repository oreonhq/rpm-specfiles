%global source0_hash 31ba533ffd5ada1ee0c25b599e115e5d18106550b775aac6348c05bf015b01c1
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%global goipath         github.com/substrait-io/substrait-go
Version:                0.4.2
%gometa -L
%global common_description %{expand:
Experimental Go bindings for substrait.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles     extensions/definitions/*.yaml
Name:           golang-github-substrait-io
Release:        1%{?dist}
Summary:        Experimental Go bindings for substrait
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/substrait-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
