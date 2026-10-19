%global source0_hash 30539ad96348d0f9373e5b027d5b0f67de18cec51a3b04686f3056b9cb5262d4
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/franela/goreq
%global commit          bcd34c9993f899273c74baaa95e15386cd97b6e7
%gometa
%global common_description %{expand:
Minimal and simple request library for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Minimal and simple request library for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/goreq-%{commit}.tar.gz
Patch0:         0001-Import-github.com-franela-goblin-as-goblin.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/franela/goblin)
BuildRequires:  golang(github.com/onsi/gomega)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
