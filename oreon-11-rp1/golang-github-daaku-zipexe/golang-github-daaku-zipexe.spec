%global source0_hash 751e40e4ed4dfdab655dbb5c201b694edbbe35f370dd28116ddb721ab50afe03
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/daaku/go.zipexe
Version:                1.0.2
%gometa
%global common_description %{expand:
Package zipexe attempts to open an executable binary file as a zip file.}
%global golicenses      license
%global godocs          readme.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Open an executable binary file as a zip file
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go.zipexe-%{version}.tar.gz
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
