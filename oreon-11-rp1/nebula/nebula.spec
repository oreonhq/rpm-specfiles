%global source0_hash 12972f5a1dc37b89dff6af91685f7f7eb643b7f75da760c036d1e8d850387e54
%bcond check 1
%global goipath         github.com/slackhq/nebula
Version:                1.10.3
%gometa -L -f
Name:           nebula
Release:        1%{?dist}
Summary:        A scalable overlay networking tool with a focus on performance, simplicity and security
License:        Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND GPL-2.0-only AND ISC AND MIT AND Zlib
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        nebula.service
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A scalable overlay networking tool with a focus on performance, simplicity and
security.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

export LDFLAGS="-X main.Build=%{version}-Fedora $(LDFLAGS)"
%global gomodulesmode GO111MODULE=on
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/nebula
install -m 0640 -vp examples/config.yml %{buildroot}%{_sysconfdir}/nebula
install -m 0644 -vDp %{SOURCE3}         %{buildroot}%{_unitdir}/nebula.service
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%ifarch s390x
%gocheck -d github.com/slackhq/nebula/service
%else
%gotest ./...
%endif
%endif
%post

%systemd_post nebula.service
%preun

%systemd_preun nebula.service
%postun

%systemd_postun_with_restart nebula.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
