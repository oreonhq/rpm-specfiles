%global source0_hash 6f1ddaa9fbc90ea5c00b949e0981b78c5014e109de88804ae2512209091eae56
%global _hardened_build 1
%global beta    beta15
Name:           hddtemp
Version:        0.4.4
Release:        1%{?dist}
Summary:        Hard disk temperature tool
License:        GPL-2.0-or-later
URL:            http://savannah.nongnu.org/projects/hddtemp/
Source0:        http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}-%{beta}.tar.bz2
Source1:        %{name}.db
Source2:        %{name}.service
Source3:        %{name}.sysconfig
Source4:        %{name}.pam
Source5:        %{name}.consoleapp
Patch0:         0001-Try-attribute-190-if-194-doesn-t-exist.patch
Patch1:         http://ftp.debian.org/debian/pool/main/h/hddtemp/hddtemp_0.3-beta15-53.diff.gz
Patch2:         %{name}-0.3-beta15-autodetect-717479.patch
Patch3:         0001-Allow-binding-to-a-listen-address-that-doesn-t-exist.patch
Patch4:         fix-model-length.patch
Patch5:         ru.po.patch
Patch6:         %{name}-nvme.patch
Patch7:         hddtemp-configure-c99.patch
Requires:       %{_bindir}/consolehelper
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
hddtemp is a tool that gives you the temperature of your hard drive by
reading S.M.A.R.T. information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{beta}

%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P0 -p1
%patch -P4 -p1
%patch -P5 -p0
%patch -P6 -p1
%patch -P7 -p1

sed -i -e 's|/etc/hddtemp.db|%{_datadir}/misc/hddtemp.db|' doc/hddtemp.8
chmod -x contribs/analyze/*
rm COPYING ; cp -p GPL-2 COPYING
cp -p debian/changelog changelog.debian

%build

%configure --disable-dependency-tracking
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_sbindir}/hddtemp %{buildroot}%{_libexecdir}
install -Dpm 644 %{S:1} %{buildroot}%{_datadir}/misc/hddtemp.db
install -Dpm 644 %{S:2} %{buildroot}%{_unitdir}/hddtemp.service
install -Dpm 644 %{S:3} %{buildroot}%{_sysconfdir}/sysconfig/hddtemp
install -dm 755 %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/hddtemp
install -Dpm 644 %{S:4} %{buildroot}%{_sysconfdir}/pam.d/hddtemp
install -Dpm 644 %{S:5} %{buildroot}%{_sysconfdir}/security/console.apps/hddtemp
%find_lang %{name}
%oreon_autofiles main

%post

%systemd_post hddtemp.service
%preun

%systemd_preun hddtemp.service
%postun

%systemd_postun_with_restart hddtemp.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
