%global source0_hash 38eab056651c66db96441461d0bb4d6651ebdf8393f941e20d0f9bc921459703
%bcond check 0
%global goipath         github.com/mdlayher/ethernet
%global commit          0394541c37b7f86a10e0b49492f6d4f605c34163
%gometa
%global common_description %{expand:
The Golang package ethernet implements marshaling and unmarshaling of IEEE
802.3 Ethernet II frames and IEEE 802.1Q VLAN tags.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Implements marshaling and unmarshaling of IEEE 802.3 Ethernet II frames and IEEE 802.1Q VLAN tags
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ethernet-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       etherecho
Summary:        Broadcast a message to all machines in the same network segment
BuildArch:      noarch

%description -n etherecho
Broadcast a message to all machines in the same network segment

%description
%{common_description}

%package -n etherecho
Summary:        Broadcast a message to all machines in the same network segment
%description -n etherecho
etherecho broadcasts a message to all machines in the same network segment, and
listens for other messages from other etherecho servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/etherecho %{goipath}/cmd/etherecho
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles etherecho usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n etherecho -f %{oreon_filedir}/etherecho.list

%changelog

%autochangelog
