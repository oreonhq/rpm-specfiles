%global source0_hash 68c1d5fbb11864403ae39c1a5937f13afd80b03e68041368831ef58cb613578e
Name:           plocate
Version:        1.1.25
Release:        1%{?dist}
Summary:        Much faster locate
License:        GPL-2.0-or-later AND GPL-2.0-only
URL:            https://plocate.sesse.net/
Source0:        https://plocate.sesse.net/download/plocate-%{version}.tar.gz
Source1:        plocate.sysusers
Conflicts:      mlocate
Provides:       locate
Obsoletes:      mlocate < 0.26-500
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  meson
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
plocate is a locate(1) based on posting lists, giving much faster
searches on a much smaller index. It is a drop-in replacement for
mlocate in nearly all aspects, and is fast on SSDs and non-SSDs alike.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dsystemunitdir=%_unitdir -Dinstall_systemd=true
%meson_build
cat >locate.1 <<EOF
.so man1/plocate.1
EOF
cat >updatedb.conf <<EOF
PRUNEFS = "9p afs autofs binfmt_misc ceph cgroup cgroup2 cifs coda configfs curlftpfs debugfs devfs devpts devtmpfs ecryptfs ftpfs fuse.ceph fuse.cryfs fuse.encfs fuse.glusterfs fuse.gvfsd-fuse fuse.mfs fuse.rclone fuse.rozofs fuse.sshfs fusec fusesmb gfs gfs2 gpfs hugetlbfs iso9660 lustre lustre_lite mfs mqueue ncpfs nfs nfs4 ocfs ocfs2 proc pstore ramfs pstorefs rootfs rpc_pipefs securityfs smbfs sysfs tmpfs tracefs udev udf usbfs"
PRUNEPATHS = "/tmp /media /dev /sys /proc /run /var/cache /var/spool"
EOF
%install
%meson_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/plocate.conf
ln -s plocate %{buildroot}%{_bindir}/locate
install -p -D -m 0644 -t %{buildroot}%{_mandir}/man1/ locate.1
install -p -D -m 0644 -t %{buildroot}%{_sysconfdir}/ updatedb.conf
%global plocate_start_now %{_localstatedir}/lib/rpm-state/plocate_start_now
%oreon_autofiles main

%post

%systemd_post plocate-updatedb.service plocate-updatedb.timer
if [ $1 == 1 ] && [ -d /run/systemd ]; then
     touch %{plocate_start_now} || :
fi
%preun

%systemd_preun plocate-updatedb.service plocate-updatedb.timer
%postun

%systemd_postun_with_restart plocate-updatedb.service plocate-updatedb.timer
%posttrans

if [ -f %{plocate_start_now} ]; then
   rm %{plocate_start_now} || :
   if systemctl is-enabled plocate-updatedb.timer &>/dev/null; then
      systemctl start --no-block plocate-updatedb.timer plocate-updatedb.service || :
   fi
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
