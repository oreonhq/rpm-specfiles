%global source0_hash 3158c5f0e6a9af4ef589e37528253ecd6a53fdb4ddb47e2a2dbfc20048fe9615
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zyedidia/pty
Version:                2.0.0
%gometa
%global common_description %{expand:
Pty is a Go package for using unix pseudo-terminals.}
%global golicenses      License
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        PTY interface for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pty-%{version}.tar.gz
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
