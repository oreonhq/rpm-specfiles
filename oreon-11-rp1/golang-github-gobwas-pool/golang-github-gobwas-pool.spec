%global source0_hash af627b30208ca77b4f8949910d8cc2fd6fdb14deda16ac7fb625f7cbdbd79805
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gobwas/pool
Version:                0.2.1
%gometa
%global common_description %{expand:
Go Pooling Helpers.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go Pooling Helpers
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pool-%{version}.tar.gz
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
