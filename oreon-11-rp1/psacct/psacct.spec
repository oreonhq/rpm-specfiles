%global source0_hash 4c15bf2b58b16378bcc83f70e77d4d40ab0b194acf2ebeefdb507f151faa663f
%define with_last     0
Summary:        Utilities for monitoring process activities
Name: psacct
Version: 6.6.4
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/acct/
Source0:        https://mirrors.kernel.org/gnu/acct/acct-%{version}.tar.gz
Source1: psacct.service
Source2: psacct-logrotate.in
Source3: accton-create
Patch1: psacct-6.6.2-unnumberedsubsubsec.patch
Patch2: psacct-6.6.1-SEGV-when-record-incomplete.patch
Patch3: psacct-6.6.4-lastcomm-manpage-pid-twice.patch
Patch4: psacct-6.6.4-sprintf-buffer-overflow.patch
Patch5: psacct-6.6.4-specfile-tweaks-file-locs.patch
Patch6: f42-fix-ftbfs.patch
Conflicts: filesystem < 3
Requires: coreutils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
The psacct package contains several utilities for monitoring process
activities, including ac, lastcomm, accton and sa. The ac command
displays statistics about how long users have been logged on. The
lastcomm command displays information about previous executed
commands. The accton command turns process accounting on or off. The
sa command summarizes information about previously executed
commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir acct-%{version}
%oreon_prep
%build

%configure --enable-linux-multiformat
make
%install
mkdir -p %{buildroot}{/sbin,%{_bindir},%{_mandir},%{_sbindir}}
make install prefix=%{buildroot}%{_prefix} \
        bindir=%{buildroot}%{_bindir} sbindir=%{buildroot}%{_sbindir} \
        infodir=%{buildroot}%{_datadir}/info mandir=%{buildroot}%{_mandir}
cp dump-acct.8 %{buildroot}%{_mandir}/man8/
rm -f %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}/var/account
touch %{buildroot}/var/account/pacct && chmod 0600 %{buildroot}/var/account/pacct
mkdir -p %{buildroot}/etc/logrotate.d
sed -e 's|%%{_bindir}|%{_bindir}|g' -e 's|%%{_sbindir}|%{_sbindir}|g' %{SOURCE2} > %{buildroot}/etc/logrotate.d/psacct
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_libexecdir}/psacct
install -m 755 %{SOURCE3} %{buildroot}%{_libexecdir}/psacct/
%if ! %{with_last}
rm -f %{buildroot}%{_bindir}/last %{buildroot}%{_mandir}/man1/last.1*
%oreon_autofiles main
%endif
%post

%systemd_post psacct.service
touch /var/account/pacct && chmod 0600 /var/account/pacct
%preun

%systemd_preun psacct.service
%postun

%systemd_postun_with_restart psacct.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.4-26
- Import
