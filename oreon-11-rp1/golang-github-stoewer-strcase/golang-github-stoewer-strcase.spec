%global source0_hash 5015a14dc191baa9f0b606e755534ddc45742b81f9f4be88bd4e65d92f29937d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/stoewer/go-strcase
Version:                1.2.0
%gometa
%global common_description %{expand:
Convert snake case, camel case and kebap case strings.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Convert snake case, camel case and kebap case strings
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-strcase-%{version}.tar.gz
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
