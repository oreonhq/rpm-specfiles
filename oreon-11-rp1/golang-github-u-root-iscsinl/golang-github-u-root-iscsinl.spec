%global source0_hash 4c96b5fb6fae6715435a6d9c7d4131a2b313bfe7685e22e4d26f5e3fce000a19
%bcond check 1
%global goipath         github.com/u-root/iscsinl
Version:                0.1.0
%gometa
%global common_description %{expand:
Go iSCSI initiator netlink library.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go iSCSI initiator netlink library
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/iscsinl-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gostor/gotgt/pkg/config)
BuildRequires:  golang(github.com/gostor/gotgt/pkg/port/iscsit)
BuildRequires:  golang(github.com/gostor/gotgt/pkg/scsi)
BuildRequires:  golang(github.com/gostor/gotgt/pkg/scsi/backingstore)
BuildRequires:  golang(github.com/hugelgupf/p9/fsimpl/test/vmdriver)
BuildRequires:  golang(github.com/u-root/u-root/pkg/mount)
BuildRequires:  golang(github.com/u-root/u-root/pkg/qemu)
BuildRequires:  golang(github.com/u-root/u-root/pkg/sh)
BuildRequires:  golang(github.com/u-root/u-root/pkg/testutil)
BuildRequires:  golang(github.com/u-root/u-root/pkg/vmtest)
BuildRequires:  golang(github.com/vishvananda/netlink/nl)
BuildRequires:  golang(golang.org/x/sys/unix)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
