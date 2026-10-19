%global source0_hash 902fd37fb72bf7b5e0e1f41579402988fcf10096c96cc927b32e8dcc820c5df1
%ifarch s390x
%bcond check 1
%else
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/mdlayher/netlink
Version:                1.11.2
%gometa -f
%global common_description %{expand:
Package netlink provides low-level access to Linux netlink sockets.}
%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Low-level access to Linux netlink sockets
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/netlink-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  iproute
# /oreon:deps
%description %{common_description}

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
