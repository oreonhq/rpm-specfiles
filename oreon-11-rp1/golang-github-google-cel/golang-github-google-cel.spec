%global source0_hash a5a79d49cf16d3b11b717942c33e219242b6a2ab12a4b8a929107c3451f56d17
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/google/cel-go
Version:                0.20.1
%gometa -L -f
%global common_description %{expand:
The Common Expression Language (CEL) is a non-Turing complete language designed
for simplicity, speed, safety, and portability. CEL's C-like syntax looks nearly
identical to equivalent expressions in C++, Go, Java, and TypeScript.}
%global golicenses      LICENSE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast, portable, non-Turing complete expression evaluation
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cel-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  antlr4
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%if %{without bootstrap}
%build

pushd parser/gen
antlr4 -Dlanguage=Go -package gen -visitor CEL.g4
popd
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck -d server
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
