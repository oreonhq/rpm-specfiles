%global source0_hash b660b34ea175443404fc109cf2a1d20f699f0d62358d44807079600962c413ed

# systemd units for snapper
%global snapper_svcs snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service

Name:           snapper
Version:        0.13.0
Release:        1%{?dist}
Summary:        Tool for filesystem snapshot management

License:        GPL-2.0-only
URL:            https://snapper.io
Source0:        https://github.com/openSUSE/snapper/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-remove-ext4-info-xml.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  glibc-all-langpacks

BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  btrfs-progs-devel
BuildRequires:  libmount-devel
BuildRequires:  libselinux-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  libacl-devel
BuildRequires:  boost-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  dbus-devel
BuildRequires:  json-c-devel
BuildRequires:  ncurses-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       diffutils

%description
This package contains snapper, a tool for filesystem snapshot management.

%package libs
Summary:        Library for filesystem snapshot management
Requires:       util-linux%{?_isa}
Requires:       btrfs-progs%{?_isa}

%description libs
This package contains the snapper shared library
for filesystem snapshot management.

%package devel
Summary:        Header files and development libraries for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
Requires:       libacl-devel%{?_isa}
Requires:       boost-devel%{?_isa}
Requires:       btrfs-progs-devel
Requires:       libxml2-devel%{?_isa}
Requires:       libmount-devel%{?_isa}

%description devel
This package contains header files and documentation for developing with
snapper.

%package tests
Summary:        Integration tests for snapper
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description tests
%{summary}.

%package backup
Summary:        A backup program for snapper
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description backup
A backup program for snapshots created by snapper.

%package -n pam_snapper
Summary:        PAM module for calling snapper
BuildRequires:  pam-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n pam_snapper
A PAM module for calling snapper during user login and logout.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
find -type f -exec sed -i -e "s|/usr/lib/snapper|%{_libexecdir}/%{name}|g" {} ';'

%conf
autoreconf -vfi
%configure \
  --disable-bcachefs \
  --disable-ext4 \
  --disable-zypp \
  --enable-selinux \
  %{nil}

%build
%make_build

%install
%make_install
install -Dpm0644 data/sysconfig.snapper %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%find_lang %{name}
find %{buildroot} -name '*.la' -print -delete
rm -rf %{buildroot}%{_sysconfdir}/cron.hourly
rm -rf %{buildroot}%{_sysconfdir}/cron.daily
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING

%check
make %{?_smp_mflags} check

%post
%systemd_post %{snapper_svcs}

%preun
%systemd_preun %{snapper_svcs}

%postun
%systemd_postun_with_restart %{snapper_svcs}

%pre libs
for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i}.rpmsave.old ||:
done

%posttrans libs
for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i} ||:
done

%files -f snapper.lang
%license COPYING
%doc AUTHORS
%{_bindir}/snapper
%{_sbindir}/mksubvolume
%{_sbindir}/snapperd
%config(noreplace) %{_sysconfdir}/logrotate.d/snapper
%{_unitdir}/snapper-{timeline,cleanup,boot}.*
%{_unitdir}/snapperd.service
%{_datadir}/bash-completion/completions/snapper
%{_datadir}/zsh/site-functions/_snapper
%{_datadir}/dbus-1/system.d/org.opensuse.Snapper.conf
%{_datadir}/dbus-1/system-services/org.opensuse.Snapper.service
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/mksubvolume.8*
%{_mandir}/man8/snapperd.8*
%{_mandir}/man5/snapper-configs.5*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/installation-helper
%{_libexecdir}/%{name}/systemd-helper

%files libs
%license COPYING
%{_libdir}/libsnapper.so.*
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/configs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/config-templates
%{_datadir}/%{name}/config-templates/default
%dir %{_datadir}/%{name}/filters
%{_datadir}/%{name}/filters/*.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%files devel
%doc examples/c/*.c
%doc examples/c++-lib/*.cc
%{_libdir}/libsnapper.so
%{_includedir}/%{name}/

%files tests
%license COPYING
%dir %{_libdir}/snapper
%{_libdir}/snapper/testsuite/

%files backup
%{_sbindir}/snbk
%dir %{_sysconfdir}/%{name}/backup-configs
%dir %{_sysconfdir}/%{name}/certs
%{_unitdir}/%{name}-{backup}.*
%{_mandir}/*/snbk.8*
%{_mandir}/*/%{name}-backup-configs.5*
%{_datadir}/bash-completion/completions/snbk

%files -n pam_snapper
%{_libdir}/security/pam_snapper.so
%{_prefix}/lib/pam_snapper/
%{_mandir}/man8/pam_snapper.8*
