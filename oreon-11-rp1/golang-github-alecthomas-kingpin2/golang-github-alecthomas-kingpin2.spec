%global source0_hash 8c3cf1d68f6f86b1c62c074be1f8e216761c57d608f4f963b59e0306296e5395
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alecthomas/kingpin/v2
Version:                2.4.0
%gometa -L -f
%global common_description %{expand:
Go command line and flag parser.}
%global golicenses      COPYING
%global godocs          README.md
Name:           golang-github-alecthomas-kingpin2
Release:        1%{?dist}
Summary:        Go command line and flag parser
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/alecthomas/kingpin/archive/v%{version}/kingpin-%{version}.tar.gz
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
