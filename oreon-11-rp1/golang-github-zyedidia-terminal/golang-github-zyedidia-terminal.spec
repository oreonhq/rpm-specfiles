%global source0_hash 5721ff57df1e6d5cb201f4368467c4c9c0272489bb902c0ec6c788a230012a73
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zyedidia/terminal
%global commit          533c623e241584694ef5438ff56fa66a8b71d8db
%gometa
%global common_description %{expand:
Package Terminal is a vt10x terminal emulation backend, influenced largely by
st, rxvt, xterm, and iTerm as reference. Use it for terminal muxing, a terminal
emulation frontend, or wherever else you need terminal emulation.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Vt10x terminal emulation backend
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/terminal-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/nsf/termbox-go)
BuildRequires:  golang(github.com/zyedidia/pty)
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
