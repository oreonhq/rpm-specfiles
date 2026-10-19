%global source0_hash e8b2904af9ebc9cfad174397cdf9b890ad4249a0e699b0aa179ecd47a2f65d92
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/Knetic/govaluate
Version:                3.0.0
%global commit          9aa49832a739dcd78a5542ff189fb82c3e423116
%gometa
%global common_description %{expand:
Provides support for evaluating arbitrary C-like artithmetic/string
expressions.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTORS MANUAL.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Arbitrary expression evaluation for golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/govaluate-%{commit}.tar.gz
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
