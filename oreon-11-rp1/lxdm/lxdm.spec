%global source0_hash edf8effe1b5803baefc82aa856c095f16714b4f3bfb872b427cca0529deeab64
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
%global tempfiles_user lxdm
Name:           lxdm
Version:        %{main_version}%{?git_version:^%{?git_version}}
Release:        14%{?dist}
Summary:        Lightweight X11 Display Manager
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://lxde.org
%if 0%{?git_snapshot}
Source0:        %{name}-%{main_version}-D%{git_date}git%{git_short}.tar.bz2
%else
%endif
Source1:        lxdm.service
Source2:        lxdm.preset
Source5:        lxdm_conf_login
Source10:		pam.lxdm
Source100:      create-tarball-from-git.sh
Patch50:        lxdm-0.4.1-config.patch
Patch60:        lxdm-0.5.1-ssh-agent-on-start.patch
Patch61:        lxdm-0.5.3-path-usrmove.patch
%if 0%{?git_snapshot}
%endif
Requires:       pam
Requires:       /sbin/shutdown
Requires:       desktop-backgrounds-compat
Requires:		%{_bindir}/ssh-agent
Provides:       service(graphical-login) = lxdm
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  systemd
# /oreon:deps
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

install -cpm 644 \
	%{SOURCE10} \
	pam/lxdm

cat << EOF > tempfiles.lxdm.conf
d /run/%{name} 0755 %{tempfiles_user} %{tempfiles_user}
d %{_localstatedir}/lib/%{name} 0755 %{tempfiles_user} %{tempfiles_user}
EOF

%build

export ACLOCAL_PATH=%{_datadir}/gettext/m4/
%{?git_version:sh autogen.sh}
%configure \
	--enable-gtk3 \
	--disable-silent-rules \
	--disable-consolekit \
	%{nil}
make %{?_smp_mflags}
cat > %{name}.sysusers.conf <<EOF
u     %{name} -  'LXDM daemon' %{_localstatedir}/lib/%{name} -
EOF
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
%find_lang %{name}
touch %{buildroot}%{_sysconfdir}/%{name}/xinitrc
mkdir -p %{buildroot}/run/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
install -m644 -p %{SOURCE5} %{buildroot}%{_localstatedir}/lib/%{name}/%{name}.conf
install -Dpm 644 tempfiles.lxdm.conf %{buildroot}%{_prefix}/lib/tmpfiles.d/lxdm.conf
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -m644 -p -D %{SOURCE2} %{buildroot}%{_unitdir}-preset/83-fedora-lxdm.preset
install -Dpm 644 %{name}.sysusers.conf %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main

%pre

exit 0
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
