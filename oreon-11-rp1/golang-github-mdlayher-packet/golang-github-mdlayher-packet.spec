%global source0_hash c236589d3110757c44923292245d5ed02df32b249097cc8a3e0c181edc1adcab
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mdlayher/packet
Version:                1.2.0
%gometa -f
%global common_description %{expand:
Package packet provides access to Linux packet sockets (AF_PACKET). MIT
Licensed.}
%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Provides access to Linux packet sockets (AF_PACKET)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/packet-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
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
