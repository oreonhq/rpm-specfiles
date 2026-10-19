%global source0_hash 51a5a8e36f30ddd97866779e93c4e93b0d4958a60fabd1d17fc2226bfe7823db
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/subosito/gotenv
Version:                1.6.0
%gometa
%global common_description %{expand:
Load environment variables from `.env` or `io.Reader` in Go.}
%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Load environment variables from `.env` or `io.Reader` in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gotenv-%{version}.tar.gz
Patch:          https://github.com/subosito/gotenv/pull/30.patch
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
