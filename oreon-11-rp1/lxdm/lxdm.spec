%global source0_hash edf8effe1b5803baefc82aa856c095f16714b4f3bfb872b427cca0529deeab64

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=540034

%{!?_unitdir: %global _unitdir %{_prefix}/lib/systemd/system/}

%global git_snapshot 1

%if 0%{?git_snapshot}
%global git_rev  2d4ba970e9bf97ec7d9c2730c940cabc58c54d27
%global git_date 20220831
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

%global main_version 0.5.3
%global use_lxdm_user  0
%if 0%{?fedora} >= 42
%global use_lxdm_user  1
%endif

%if %{use_lxdm_user}
%global tempfiles_user lxdm
%else
%global tempfiles_user root
%endif

Name:           lxdm
Version:        %{main_version}%{?git_version:^%{?git_version}}
Release:        14%{?dist}
Summary:        Lightweight X11 Display Manager

# src/*.c	GPL-3.0-or-later
# src/gdm/		GPL-2.0-or-later AND LGPL-2.1-or-later
# src/greeter.c	GPL-2.0-or-later
# SPDX confirmed
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lxde.org

%if 0%{?git_snapshot}
Source0:        %{name}-%{main_version}-D%{?git_version}.tar.bz2
%else
Source0:        http://downloads.sourceforge.net/sourceforge/lxdm/%{name}-%{version}.tar.xz
%endif

# systemd service file and preset
Source1:        lxdm.service
Source2:        lxdm.preset

# The default contents of /var/lib/lxdm/lxdm.conf (c.f. lxdm.c:lxdm_save_login)
Source5:        lxdm_conf_login

# Fedora pam setting
# F-39: remove pam_console.so (bug 1822227, bug 2166692)
Source10:		pam.lxdm

# Shell script to create tarball from git scm
Source100:      create-tarball-from-git.sh

## Patches needing discussion with the upstream

## Distro specific patches ##

# Distro artwork, start on vt1
Patch50:        lxdm-0.4.1-config.patch
Patch60:        lxdm-0.5.1-ssh-agent-on-start.patch
# Remove /bin, /sbin from PATH with usrmove
Patch61:        lxdm-0.5.3-path-usrmove.patch

BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pam-devel
BuildRequires:  intltool >= 0.40.0
%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
%endif
Requires:       pam
Requires:       /sbin/shutdown
Requires:       desktop-backgrounds-compat
Requires:		%{_bindir}/ssh-agent
# Loading jpegxl format img requires the below
%if 0%{?fedora} >= 42
%if 0%{?fedora} >= 43
Requires:       gdk-pixbuf2%{?_isa} >= 2.44
%else
Requires:       jxl-pixbuf-loader%{?_isa}
%endif
%endif
# needed for anaconda to boot into runlevel 5 after install
Provides:       service(graphical-login) = lxdm

BuildRequires:  systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%if %{use_lxdm_user}
%if 0%{?fedora} <= 43
Requires(pre):      shadow-utils
%endif
%endif

%description
LXDM is the future display manager of LXDE, the Lightweight X11 Desktop 
environment. It is designed as a lightweight alternative to replace GDM or 
KDM in LXDE distros. It's still in very early stage of development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{?git_version:-n %{name}-%{main_version}-D%{?git_version}}

%patch -P50 -p1 -b .config
%patch -P60 -p1 -b .ssh_agent
%patch -P61 -p1 -b .usemove

# Reset X after logout (bug 1269917)
sed -i.reset data/lxdm.conf.in \
	-e '\@reset@s|^.*$|reset=1|' 
# Fedora 42 changed default background file format
%if 0%{?fedora} >= 42
sed -i.f42 data/lxdm.conf.in \
	-e '\@bg=@s|default.png|default.jxl|'
%endif

install -cpm 644 \
	%{SOURCE10} \
	pam/lxdm

cat << EOF > tempfiles.lxdm.conf
d /run/%{name} 0755 %{tempfiles_user} %{tempfiles_user}
d %{_localstatedir}/lib/%{name} 0755 %{tempfiles_user} %{tempfiles_user}
EOF

%build
# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
%{?git_version:sh autogen.sh}
%configure \
	--enable-gtk3 \
	--disable-silent-rules \
	--disable-consolekit \
	%{nil}
make %{?_smp_mflags}

%if %{use_lxdm_user}
cat > %{name}.sysusers.conf <<EOF
#Type Name ID GECOS         Home directory Shell
u     %{name} -  'LXDM daemon' %{_localstatedir}/lib/%{name} -
EOF
%endif

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
%find_lang %{name}

# these files are not in the package, but should be owned by lxdm 
touch %{buildroot}%{_sysconfdir}/%{name}/xinitrc
mkdir -p %{buildroot}/run/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
install -m644 -p %{SOURCE5} %{buildroot}%{_localstatedir}/lib/%{name}/%{name}.conf

install -Dpm 644 tempfiles.lxdm.conf %{buildroot}%{_prefix}/lib/tmpfiles.d/lxdm.conf

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -m644 -p -D %{SOURCE2} %{buildroot}%{_unitdir}-preset/83-fedora-lxdm.preset
%if %{use_lxdm_user}
install -Dpm 644 %{name}.sysusers.conf %{buildroot}%{_sysusersdir}/%{name}.conf
%endif

%pre
%if %{use_lxdm_user}
%if 0%{?fedora} <= 43
getent group %{tempfiles_user} &>/dev/null || \
   %{_sbindir}/groupadd -r %{tempfiles_user}
getent passwd %{tempfiles_user} &> /dev/null || \
   %{_sbindir}/useradd \
   -c 'LXDM daemon' \
   -g %{tempfiles_user} \
   -d %{_localstatedir}/lib/%{name} \
   -r \
   -s /sbin/nologin \
   %{tempfiles_user} 2>/dev/null
%endif
%endif
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files -f %{name}.lang
# FIXME add ChangeLog and NEWS if not empty
%doc AUTHORS
%license COPYING
%doc README TODO
%license gpl-2.0.txt
%license lgpl-2.1.txt

%dir %{_sysconfdir}/%{name}
%ghost %config(noreplace,missingok) %{_sysconfdir}/%{name}/xinitrc
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/Xsession
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/LoginReady
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PostLogin
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PostLogout
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PreLogin
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PreReboot
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/PreShutdown
%config %attr(640,%{tempfiles_user},%{tempfiles_user}) %{_sysconfdir}/%{name}/lxdm.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%if %{use_lxdm_user}
%{_sysusersdir}/%{name}.conf
%endif

%{_bindir}/%{name}-config
%{_sbindir}/%{name}
%{_sbindir}/lxdm-binary
%{_libexecdir}/lxdm-greeter-gtk
%{_libexecdir}/lxdm-greeter-gdk
%{_libexecdir}/lxdm-numlock
%{_libexecdir}/lxdm-session

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/config.ui
%{_datadir}/%{name}/lxdm.glade
%{_datadir}/%{name}/themes/

%{_tmpfilesdir}/lxdm.conf
%dir %attr(-,%{tempfiles_user},%{tempfiles_user}) /run/%{name}

%{_unitdir}/lxdm.service
%{_unitdir}-preset/83-fedora-lxdm.preset

%dir %attr(-,%{tempfiles_user},%{tempfiles_user}) %{_localstatedir}/lib/%{name}
%config(noreplace) %verify(not md5 size mtime) %attr(-,%{tempfiles_user},%{tempfiles_user}) %{_localstatedir}/lib/%{name}/%{name}.conf

%changelog
%autochangelog
