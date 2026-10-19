%global source0_hash b2a8df74a8b988d90efbba37fa020e17eeba30a3c70bf5c03a79f0eabab8831d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/anmitsu/go-shlex
%global commit          38f4b401e2be5955e3e00b843d96e3c406f5094d
%gometa
%global common_description %{expand:
Package Shlex provides a simple lexical analysis like Unix shell.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Library to make a lexical analyzer like Unix shell for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-shlex-%{commit}.tar.gz
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
