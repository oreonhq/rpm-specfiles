%global source0_hash 350b31d5070002e9729ea63e1d62f97596ba0062151c0f3ee16f02af67753204

Name:           slim
Version:        1.4.0
Release:        10%{?dist}
Summary:        Simple Login Manager
License:        GPL-2.0-or-later
#changed from GPLv2+ per BZ: 2173236, comment 11 and https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_2

URL:            https://sourceforge.net/projects/slim-fork/
Source0:        https://versaweb.dl.sourceforge.net/project/%{name}-fork/%{name}-%{version}.tar.gz
# stolen from xdm
Source1:        %{name}.pam
# adapted from debian to use freedesktop
Source2:        slim-update_slim_wmlist
Source3:        slim-dynwm
Source4:        slim-fedora.txt
# logrotate entry (see bz#573743)
Source5:        slim.logrotate.d
Source6:        slim-tmpfiles.conf
Source7:        slim.service
patch0:	        slim-1.4.0-fedora.patch  
patch1:         slim-1.4.0-selinux.patch

## Keyring copied on 2023-02-26 from: xfontsel.gpg

# Fedora-specific patches
#%patch  0
#%patch 1 
#slim-1.4.0-fedora.patch
#%patch 2         
#slim-1.4.0-selinux.patch
#Patch3:         slim-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXmu-devel libXft-devel libXrender-devel
BuildRequires:  libpng-devel libjpeg-devel freetype-devel fontconfig-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig gettext libselinux-devel pam-devel cmake
BuildRequires:  scrot xterm freeglut-devel libXrandr-devel
BuildRequires:  cmake

Requires:       scrot xterm /sbin/shutdown
Requires:       %{_sysconfdir}/pam.d
# we use 'include' in the pam file, so
Requires:       pam >= 0.80
# reuse the images
Requires:       f%{?fedora}-backgrounds-base

# for anaconda dnf
Provides:       service(graphical-login)

BuildRequires:    systemd
BuildRequires:    systemd-rpm-macros

%description
SLiM (Simple Login Manager) is a graphical login manager for X11.
It aims to be simple, fast and independent from the various
desktop environments.
SLiM is based on latest stable release of Login.app by Per LidÃ©n.

In the distribution, slim may be called through a wrapper, slim-dynwm,
which determines the available window managers using the freedesktop
information and modifies the slim configuration file accordingly,
before launching slim.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch 0 -p0 -b .fedora
%patch 1 -p1 -b .selinux
cp -p %{SOURCE4} README.Fedora
#%patch3 -p1 -b .gcc11 # no longer needed

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS -lXft"
%cmake -DUSE_PAM=yes -DUSE_CONSOLEKIT=no -DBUILD_SHARED_LIBS=no -DBUILD_SLIMLOCK=yes
%cmake_build

%install
%cmake_install
install -p -m755 %{SOURCE2} %{buildroot}%{_bindir}/update_slim_wmlist
install -p -m755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-dynwm
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}.conf
install -d -m755 %{buildroot}%{_sysconfdir}/pam.d
install -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/%{name}
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
rm -f %{buildroot}%{_datadir}/%{name}/themes/default/background.jpg
ln -s ../../../backgrounds/f%{?fedora}/default/f%{?fedora}-01-day.png %{buildroot}%{_datadir}/%{name}/themes/default/background.png
# install logrotate entry
install -m0644 -D %{SOURCE5} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

install -p -D %{SOURCE6} %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}/%{name}.service

# Fix lib dir according to bits of system
mkdir -p %{buildroot}/%{_libdir}/
#mv %{buildroot}/usr/lib/lib%{name}.so* %{buildroot}/%{_libdir}/ | :
# rm garbage from instaler
#rm %{buildroot}/lib/systemd/system/%{name}.service
# devel .so
# rm %{buildroot}/%{_libdir}/lib%{name}.so

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%doc ChangeLog README* THEMES TODO
%license COPYING
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/logrotate.d/%{name}
%ghost %dir %{_localstatedir}/run/%{name}
%{_bindir}/%{name}*
%{_bindir}/update_slim_wmlist
%{_mandir}/man1/%{name}*.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes/
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf

%changelog
%autochangelog
