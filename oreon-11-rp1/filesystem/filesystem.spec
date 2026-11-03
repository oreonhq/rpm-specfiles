%global debug_package %{nil}

Name: filesystem
Version: 11
Release: 8%{?dist}
Summary: Base directory layout
License: MIT
URL: https://oreonhq.com/
Source1: sbin-filenames
Source2: filesystem.attr
Source3: filesystem.req
Source4: macros.filesystem
Provides: filesystem(merged-sbin)
Provides: filesystem(unmerged-sbin-symlinks)

%description
The directories and compatibility symlinks every other package installs into.

%package srpm-macros
Summary: RPM macros for the sbin merge

%description srpm-macros
Macros and the file attribute generator for the sbin merge.

%pretrans -p <lua>
posix.mkdir("/usr")
posix.mkdir("/usr/bin")
posix.mkdir("/usr/lib")
posix.mkdir("/usr/lib64")
posix.mkdir("/usr/libexec")
posix.mkdir("/usr/include")
posix.mkdir("/usr/share")
posix.symlink("bin", "/usr/sbin")
posix.symlink("usr/bin", "/bin")
posix.symlink("usr/sbin", "/sbin")
posix.symlink("usr/lib", "/lib")
posix.symlink("usr/lib64", "/lib64")
posix.mkdir("/var")
posix.mkdir("/var/tmp")
posix.mkdir("/run")
posix.mkdir("/proc")
posix.mkdir("/sys")
posix.mkdir("/tmp")
posix.chmod("/proc", 0555)
posix.chmod("/sys", 0555)
posix.chmod("/tmp", 01777)
posix.chmod("/var/tmp", 01777)

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/filesystem
mkdir -p %{buildroot}%{_fileattrsdir}
mkdir -p %{buildroot}%{_rpmconfigdir}
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/filesystem/sbin-filenames
install -m 644 %{SOURCE2} %{buildroot}%{_fileattrsdir}/filesystem.attr
install -m 755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/filesystem.req
install -m 644 %{SOURCE4} %{buildroot}%{_rpmmacrodir}/macros.filesystem
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/libexec
mkdir -p %{buildroot}/usr/include
mkdir -p %{buildroot}/usr/share/man
mkdir -p %{buildroot}/usr/share/info
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/var/tmp
mkdir -p %{buildroot}/var/log
mkdir -p %{buildroot}/var/cache
mkdir -p %{buildroot}/run
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/home
mkdir -p %{buildroot}/root
mkdir -p %{buildroot}/tmp
chmod 1777 %{buildroot}/tmp %{buildroot}/var/tmp
ln -snf bin %{buildroot}/usr/sbin
ln -snf usr/bin %{buildroot}/bin
ln -snf usr/sbin %{buildroot}/sbin
ln -snf usr/lib %{buildroot}/lib
ln -snf usr/lib64 %{buildroot}/lib64

%files
%defattr(0755,root,root,0755)
%dir /usr
%dir /usr/bin
%dir /usr/lib
%dir /usr/lib64
%dir /usr/libexec
%dir /usr/include
%dir /usr/share
%dir /usr/share/man
%dir /usr/share/info
/usr/sbin
/bin
/sbin
/lib
/lib64
%dir /etc
%dir /var
%attr(1777,root,root) /var/tmp
%dir /var/log
%dir /var/cache
/run
%ghost %attr(555,root,root) /proc
%ghost %attr(555,root,root) /sys
%attr(1777,root,root) /tmp
%dir /boot
%dir /home
%attr(550,root,root) /root

%files srpm-macros
%{_datadir}/filesystem/sbin-filenames
%{_fileattrsdir}/filesystem.attr
%{_rpmconfigdir}/filesystem.req
%{_rpmmacrodir}/macros.filesystem
