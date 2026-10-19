%global source0_hash ab64e63be1290f86b4aa95d1c5d0d4572ba34513016f6f79e53eb3ed799a6704
%bcond check 0
%global goipath         github.com/facebookincubator/go2chef
Version:                1.0
%global tag             1.0
%gometa
%global common_description %{expand:
go2chef is a Go tool for bootstrapping Chef installations in a flexible and
self-contained way. With go2chef, our goal is to make bootstrapping any node
in a Chef deployment as simple as "get go2chef onto a machine and run it".}
%global golicenses      LICENSE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Tool to bootstrap a system from zero so that it's able to run Chef
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/go2chef-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       go2chef
Summary:        Tool to bootstrap a system from zero so that it's able to run Chef
BuildArch:      noarch

%description -n go2chef
Tool to bootstrap a system from zero so that it's able to run Chef

%description
%{common_description}

%package -n go2chef
Summary:        Tool to bootstrap a system from zero so that it's able to run Chef
%description -n go2chef
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
# these examples aren't useful without the repository itself
rm -r examples/{custom_binary,plugins}
# fix permissions
chmod -x examples/bundles/{chefctl,chefrepo}/bundle.ps1

%build

%gobuild -o %{gobuilddir}/bin/go2chef %{goipath}/bin
%gobuild -o %{gobuilddir}/bin/go2chef-remote %{goipath}/scripts
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles go2chef usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n go2chef -f %{oreon_filedir}/go2chef.list

%changelog

%autochangelog
