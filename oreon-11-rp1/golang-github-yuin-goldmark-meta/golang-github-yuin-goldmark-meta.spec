%global source0_hash eb6d05cb2b27a6c8dbde4fa7d00ed212c1f3434a7516d53bdcedcb51fefc0e32
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/yuin/goldmark-meta
Version:                1.1.0
%gometa -L -f
%global common_description %{expand:
A YAML metadata extension for the goldmark markdown parser.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-yuin-goldmark-meta
Release:        1%{?dist}
Summary:        A YAML metadata extension for the goldmark markdown parser
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goldmark-meta-%{version}.tar.gz
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
