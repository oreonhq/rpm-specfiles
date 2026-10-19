%global source0_hash b393923c5ce61c02cb5a7d26c480bc0bd22d9578ba5e0ad402a29304a2cf3d6c
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/schollz/peerdiscovery
Version:                1.6.9
%gometa
%global common_description %{expand:
Pure-Go library for cross-platform local peer discovery using UDP multicast.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure-Go library for cross-platform local peer discovery using UDP multicast
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/peerdiscovery-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/schollz/progressbar/v2)
BuildRequires:  golang(github.com/schollz/progressbar/v3)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/net/ipv4)
BuildRequires:  golang(golang.org/x/net/ipv6)
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
