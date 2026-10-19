%global source0_hash ab130b7fab3893d01aa44c0d39be34a26da716c1d36832fbac9fa054a1d862a0
%bcond check 1
%global goipath         github.com/metacubex/mihomo
Version:                1.19.32
%global gomodulesmode   GO111MODULE=on
%gometa -L -f
%global common_description %{expand:
A rule based network proxy tool, also be known as mihomo.}
Name:           clash-meta
Release:        1%{?dist}
Summary:        A rule based network proxy tool, also be known as mihomo
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-only AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mihomo-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        clash-meta.service
Source4:        clash-meta@.service
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

export LDFLAGS=" \
    -X github.com/metacubex/mihomo/constant.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/clash-meta "-tags=with_gvisor" %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vd                     %{buildroot}%{_unitdir}
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/clash-meta
install -m 0755 -vd                     %{buildroot}%{_localstatedir}/lib/clash-meta
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0644 -vp %{S:3}              %{buildroot}%{_unitdir}/
install -m 0644 -vp %{S:4}              %{buildroot}%{_unitdir}/
ln -r -s %{buildroot}%{_bindir}/clash-meta %{buildroot}%{_bindir}/mihomo
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
