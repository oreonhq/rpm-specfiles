%global source0_hash 205a9492ff84801a1a85638a1e3fd4ad779fd2f77022c597c1d45055d1a0d184
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mvo5/goconfigparser
Version:                0.3
%global tag             0.2.2
%gometa
%global common_description %{expand:
This parser is build as a Go equivalent of the Python ConfigParser module and is
aimed for maximum compatibility for both the file format and the API. This
should make it easy to use existing python style configuration files from Go and
also ease the porting of existing python code.}
%global golicenses      COPYING
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang implementation of Python ConfigParser
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/goconfigparser-%{tag}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/check.v1)
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
