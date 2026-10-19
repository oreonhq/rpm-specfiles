%global source0_hash be22e89fd5e050782201778267080c9b92b89e04e2cef5299d41aee84359a6a6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-git/go-billy/v5
Version:                5.9.1
%gometa
%global common_description %{expand:
The missing interface filesystem abstraction for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-git-billy-5
Release:        1%{?dist}
Summary:        The missing interface filesystem abstraction for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/go-git/go-billy/archive/v%{version}/go-billy-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
