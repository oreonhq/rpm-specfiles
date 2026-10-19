%global source0_hash f0ef70282c66ca7d994ff8d5b53ee7c5f03fd3f9e24a34e0fc6eef68dcda9231
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/inconshreveable/log15
Version:                3.2.1
%gometa
%global goaltipaths     gopkg.in/inconshreveable/log15.v2
%global common_description %{expand:
Package Log15 provides an opinionated, simple toolkit for best-practice logging
in Go (golang) that is both human and machine readable. It is modeled after the
Go standard library's io and net/http packages and is an alternative to the
standard library's log package.}
%global golicenses      LICENSE term/LICENSE
%global godocs          CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Structured, composable logging for go
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/log15-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/go-stack/stack)
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-isatty)
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
