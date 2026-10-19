%global source0_hash 6a4eb132f1c677921419dbfdd71950174dc5ce5847ad5b4f6bb7be25440cd7b0
%{!?_hardened_build:%global _hardened_build 1}
Name:             fbb
URL:              https://sourceforge.net/projects/linfbb/
Version:          7.0.11
Release:        1%{?dist}
License:          GPL-2.0-or-later
Summary:        Packet radio mailbox and utilities
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Source0:        http://downloads.sourceforge.net/lin%{name}/%{name}-%{version}.tar.bz2
Source1:          epurmess.ini
Source2:          fbb.service
Source3:          fbb-icon.svg
Source4:          fbb.desktop
Source5:          org.fbb.gui.policy
Source6:          README.Fedora
Patch:           fbb-7.0.8-beta-sample-conf.patch
Patch:           fbb-7.0.11-var-lib.patch
Patch:           fbb-7.0.11-non-interactive.patch
Patch:           fbb-7.0.9-write-port-errors.patch
Patch:           fbb-7.0.9-stdout.patch
Patch:           fbb-7.0.11-ncurses-fix.patch
Patch:           fbb-remove-XmGrabTheFocus.patch
Patch:           fbb-7.0.11-x11-access-macro-fix.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  lesstif-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libax25-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  systemd
# /oreon:deps
%description
F6FBB BBS software for bulletins and messages distribution via Packet Radio
and wired networks.

%package          doc
Requires:         %{name} = %{version}-%{release}
Summary:          Documentation for fbb
BuildArch:        noarch
%description doc
Documentation for fbb.

%package          gui
Requires:         %{name}%{?_isa} = %{version}-%{release}
Summary:          GUI for fbb
%description gui
GUI for fbb.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?prerel:-%{prerel}}

cp %{SOURCE6} README.Fedora

# recode ISO-8859-15 (French) to UTF-8, reported upstream
for f in doc/satdoc-f.doc src/*.c include/*.h;
do
  iconv -f ISO8859-15 -t UTF8 -o $f.utf-8 $f
  mv $f.utf-8 $f
done

%build

autoreconf -fi
%configure
make %{?_smp_mflags} CFLAGS="%{optflags} %{?_hardened_build:-pie} -fcommon" \
  LDFLAGS="%{?__global_ldflags} %{?_hardened_build:-pie -Wl,-z,relro,-z,now}"
%install
make install DESTDIR=%{buildroot}
make installconf DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_var}/lib/fbb/{binmail/mail{0..9},docs,fbbdos/{readonly,yapp},\
log,mail/mail{0..9},oldmail,sat,wp}
mv %{buildroot}%{_docdir}/fbb/fbb.conf.sample %{buildroot}%{_sysconfdir}/ax25/fbb/fbb.conf
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/ax25/fbb/epurmess.ini
pushd %{buildroot}%{_sysconfdir}/ax25/fbb
mv port.sys.sample port.sys
cd lang
mv english.ent.sample english.ent
mv francais.ent.sample francais.ent
popd
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/fbb.service
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/fbb.svg
install -dD %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_datadir}/polkit-1/actions/org.fbb.gui.policy
touch %{buildroot}%{_var}/lib/fbb/{ERROR.SYS,dirmes.sys,etat.sys,heard.bin,inf.sys,\
statis.dat,themes.dat,tpstat.sys,wfbid.sys,sat/satel.dat,wp/wp.sys}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post fbb.service
%preun

%systemd_preun fbb.service
%postun

%systemd_postun_with_restart fbb.service
%files -f %{oreon_filedir}/main.list
%files -n fbb-doc -f %{oreon_filedir}/fbb-doc.list
%files -n fbb-gui -f %{oreon_filedir}/fbb-gui.list

%changelog

%autochangelog
