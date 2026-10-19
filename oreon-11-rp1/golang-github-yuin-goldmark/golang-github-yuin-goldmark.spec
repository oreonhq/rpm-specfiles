%global source0_hash f380537403849ce8cb0710752156bba4090a80aa4199e1cb5f58298be9e3a2e9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/yuin/goldmark
Version:                1.7.13
%gometa -L
%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-yuin-goldmark
Release:        1%{?dist}
Summary:        Markdown parser written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goldmark-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%ifarch aarch64 %{ix86} riscv64
export GOLDMARK_TEST_TIMEOUT_MULTIPLIER=10
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
