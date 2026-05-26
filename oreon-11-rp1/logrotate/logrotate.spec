Summary: Rotates, compresses, removes and mails system log files
Name: logrotate
Version: 3.22.0
Release: 5%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/logrotate/logrotate
Source0: https://github.com/logrotate/logrotate/releases/download/%{version}/logrotate-%{version}.tar.xz
Source1: https://github.com/logrotate/logrotate/releases/download/%{version}/logrotate-%{version}.tar.xz.asc

# gpg --keyserver pgp.mit.edu --recv-key 8ECCDF12100AD84DA2EE7EBFC78CE737A3C3E28E
# gpg --output cgzones.pgp --armor --export cgzones@googlemail.com
Source2: cgzones.pgp

Source3: rwtab
# oreon url source checksums begin
%global source0_sha256 42b4080ee99c9fb6a7d12d8e787637d057a635194e25971997eebbe8d5e57618
%global source0_file logrotate-3.22.0.tar.xz
# oreon url source checksums end

BuildRequires: acl
BuildRequires: automake
BuildRequires: gcc
BuildRequires: git
BuildRequires: gnupg2
BuildRequires: libacl-devel
BuildRequires: libselinux-devel
BuildRequires: make
BuildRequires: popt-devel
BuildRequires: systemd-rpm-macros
Requires: coreutils
Requires(post): systemd
Requires(preun): systemd

%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files.  Logrotate
allows for the automatic rotation compression, removal and mailing of
log files.  Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size.

Install the logrotate package if you need a utility to deal with the
log files on your system.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/logrotate-3.22.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "42b4080ee99c9fb6a7d12d8e787637d057a635194e25971997eebbe8d5e57618" || { echo "oreon: Source0 SHA256 mismatch for logrotate-3.22.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git

cat >> .gitignore << EOF
/autom4te.cache
/build
/config.h.in~
EOF
git add .gitignore
git commit -m "update .gitignore"

autoreconf -fiv
git add --all
git commit -m "force autoreconf" --allow-empty

%build
mkdir build && cd build
%global _configure ../configure
%configure --with-state-file-path=%{_localstatedir}/lib/logrotate/logrotate.status
%make_build

%check
%make_build -C build -s check

%install
%make_install -C build

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/logrotate

install -p -m 644 examples/logrotate.conf $RPM_BUILD_ROOT%{_sysconfdir}/
install -p -m 644 examples/{b,w}tmp $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/
install -p -m 644 examples/logrotate.{service,timer} $RPM_BUILD_ROOT%{_unitdir}/

# Make sure logrotate is able to run on read-only root
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d
install -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/logrotate

%pre
# If /var/lib/logrotate/logrotate.status does not exist, create it and copy
# the /var/lib/logrotate.status in it (if it exists). We have to do that in pre
# script, otherwise the /var/lib/logrotate/logrotate.status would not be there,
# because during the update, it is removed/renamed.
if [ ! -d %{_localstatedir}/lib/logrotate/ -a -f %{_localstatedir}/lib/logrotate.status ]; then
  mkdir -p %{_localstatedir}/lib/logrotate
  cp -a %{_localstatedir}/lib/logrotate.status %{_localstatedir}/lib/logrotate
fi

%post
%systemd_post logrotate.{service,timer}

# If there is any cron daemon configured, enable the systemd timer to avoid
# breaking the configuration silently when upgrading from 3.14.0-4 or
# earlier versions
%triggerin -- logrotate < 3.14.0-5
[ -e %{_sysconfdir}/crontab -o -e %{_sysconfdir}/anacrontab -o -e %{_sysconfdir}/fcrontab ] \
  && %{_bindir}/systemctl enable --now logrotate.timer &>/dev/null || :

%preun
%systemd_preun logrotate.{service,timer}

%files
%license COPYING
%doc ChangeLog.md
%{_sbindir}/logrotate
%{_unitdir}/logrotate.{service,timer}
%{_mandir}/man8/logrotate.8*
%{_mandir}/man5/logrotate.conf.5*
%config(noreplace) %{_sysconfdir}/logrotate.conf
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/{b,w}tmp
%dir %{_localstatedir}/lib/logrotate
%ghost %verify(not size md5 mtime) %attr(0640, root, root) %{_localstatedir}/lib/logrotate/logrotate.status
%config(noreplace) %{_sysconfdir}/rwtab.d/logrotate

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.22.0-5
- Import
