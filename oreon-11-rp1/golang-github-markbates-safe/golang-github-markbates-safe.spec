%global source0_hash fd873a2601a7233fa7f7ccc82406222b993b5ec4c661eb840bdb584140209994
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/markbates/safe
Version:                1.1.0
%gometa
%global common_description %{expand:
Safe for Go.}
%global golicenses      LICENSE
%global godocs          shoulders.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Safe for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/safe-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/require)
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
