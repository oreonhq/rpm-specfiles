%global source0_hash cf054e388c238c1a0b403fbc18411194c24fcbe41d7eaab8e163c5e1f10fdd92
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/moby/spdystream
Version:                0.2.0
%gometa
%global common_description %{expand:
A multiplexed stream library using spdy.}
%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A multiplexed stream library using spdy
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/spdystream-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gorilla/websocket)
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
