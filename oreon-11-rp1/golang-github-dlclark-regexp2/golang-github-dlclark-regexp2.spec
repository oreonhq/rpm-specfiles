%global source0_hash ce8b8c3b93846b679547abc14f3d9798e27bf7c13032182a6bea5c0f58dc78ad
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/dlclark/regexp2
Version:                2.8.0
%gometa
%global common_description %{expand:
Regexp2 is a feature-rich RegExp engine for Go. It doesn't have constant time
guarantees like the built-in regexp package, but it allows backtracking and is
compatible with Perl5 and .NET. You'll likely be better off with the RE2 engine
from the regexp package and should only use this if you need to write very
complex patterns or require compatibility with .NET.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Regex engine for Go based on the .NET engine
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/regexp2-%{version}.tar.gz
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
