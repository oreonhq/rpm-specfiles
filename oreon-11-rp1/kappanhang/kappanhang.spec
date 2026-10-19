%global source0_hash adc59d6cede0b1bce7aa8b402d6bbbe4bc8dafc24ae70bf0110571c227771884
%bcond check 1
%global goipath         github.com/AD8IM/kappanhang
%global commit          9c78dad0fda42314b781ac8daaa145ed60d93dff
%gometa -L -f
Name:           kappanhang
Version:        0
Release:        1%{?dist}
Summary:        Remotely connect to an Icom RS-BA1 server
License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
Remotely open audio channels and a serial port to an Icom RS-BA1 server (for
ex. Icom IC-705 transceiver).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/kappanhang %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
