%global source0_hash d29b495f447a20ae315339014fd6cd9f8588613bfc79e8da4b75a96e1b824482
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/safchain/ethtool
%global commit          874930cb3ce012efd5e6ce9d84679ce3430a85da
%gometa
%global common_description %{expand:
The Ethtool package aims to provide a library giving a simple access to the
Linux SIOCETHTOOL ioctl operations. It can be used to retrieve informations from
a network device like statistics, driver related informations or even the peer
of a VETH interface.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Simple ethtool "like" library for GO
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ethtool-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/sys/unix)
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
