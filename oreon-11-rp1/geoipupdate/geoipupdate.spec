%global source0_hash 5c08b39d2ac49ad492138b3d618dddac130065852b6237ec450bac856ace7e0a
%global source1_hash none
%bcond check 1
%global goipath github.com/maxmind/geoipupdate/v7
Version:        8.0.0
%gometa -L -f
Name:           geoipupdate
Release:        1%{?dist}
Summary:        Update GeoIP2 binary databases from MaxMind
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        https://github.com/maxmind/geoipupdate/archive/refs/tags/v%{version}.tar.gz#/geoipupdate-%{version}.tar.gz
Source2:        go-vendor-tools.toml
Source3:        geoipupdate.cron
Obsoletes:      geoipupdate-cron6 < %{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  crontabs
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
The GeoIP Update program performs automatic updates of GeoIP2 binary databases.

%package cron
Summary:        Cron job to do weekly updates of GeoIP databases
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       crontabs
Obsoletes:      GeoIP-update < 1.6.0
Provides:       GeoIP-update = 1.6.0
%description cron
Cron job for weekly updates to GeoIP2 binary databases from MaxMind.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%goprep -A
%global gomodulesmode GO111MODULE=on
GO111MODULE=on go mod vendor

%build

%global gomodulesmode GO111MODULE=on
export LDFLAGS='-X main.defaultConfigFile=%{_sysconfdir}/GeoIP.conf -X main.defaultDatabaseDirectory=%{_datadir}/GeoIP '
%gobuild -o %{gobuilddir}/bin/geoipupdate %{goipath}/cmd/geoipupdate
ln -s %{gobuilddir} build
make BUILDDIR=%{gobuilddir} CONFFILE=%{_sysconfdir}/GeoIP.conf DATADIR=%{_datadir}/GeoIP data
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                         %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/*     %{buildroot}%{_bindir}/
install -m 0755 -vd                         %{buildroot}%{_sysconfdir}
install -m 0644 -vp conf/GeoIP.conf.default %{buildroot}%{_sysconfdir}/GeoIP.conf
install -m 0755 -vd                         %{buildroot}%{_datadir}/GeoIP
install -m 0755 -vd                         %{buildroot}%{_sysconfdir}/cron.weekly
install -m 0755 -vp %{S:3}                  %{buildroot}%{_sysconfdir}/cron.weekly/geoipupdate
install -m 0755 -vd                         %{buildroot}%{_mandir}/man1
install -m 0644 -vp _build/geoipupdate.1    %{buildroot}%{_mandir}/man1/geoipupdate.1
install -m 0755 -vd                         %{buildroot}%{_mandir}/man5
install -m 0644 -vp _build/GeoIP.conf.5     %{buildroot}%{_mandir}/man5/GeoIP.conf.5
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list
%files -n geoipupdate-cron -f %{oreon_filedir}/geoipupdate-cron.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.1.1-7
- Import
