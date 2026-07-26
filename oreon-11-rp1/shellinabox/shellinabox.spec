%global source0_hash 27a5ec6c3439f87aee238c47cc56e7357a6249e5ca9ed0f044f0057ef389d81e

%global username shellinabox

Name:           shellinabox
Version:        2.20
Release:        28%{?dist}
Summary:        Web based AJAX terminal emulator
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/%{name}/%{name}

Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        shellinaboxd.sysconfig
Source2:        shellinaboxd.service
Source3:        shellinaboxd.init

Patch0:         %{name}-ssh-options.patch
Patch1:         %{name}-gcc11.patch
Patch2: shellinabox-configure-c99.patch

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

Requires:       openssl

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:      systemd
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%endif

%if 0%{?rhel} == 6
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(postun):   /sbin/service
%endif

%description
Shell In A Box implements a web server that can export arbitrary command line
tools to a web based terminal emulator. This emulator is accessible to any
JavaScript and CSS enabled web browser and does not require any additional
browser plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# Create a sysusers.d config file
cat >shellinabox.sysusers.conf <<EOF
u shellinabox - 'Shellinabox' %{_sharedstatedir}/shellinabox -
EOF

%build
autoreconf -vif
%configure --disable-runtime-loading
make %{?_smp_mflags}
chmod 644 %{name}/*

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

install -p -m 755 -D shellinaboxd %{buildroot}%{_sbindir}/shellinaboxd
install -p -m 644 -D shellinaboxd.1 %{buildroot}%{_mandir}/man1/shellinaboxd.1
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/shellinaboxd
install -p -m 644 shellinabox/white-on-black.css %{buildroot}%{_datadir}/%{name}
install -p -m 644 shellinabox/color.css %{buildroot}%{_datadir}/%{name}
install -p -m 644 shellinabox/monochrome.css %{buildroot}%{_datadir}/%{name}

%if 0%{?fedora} || 0%{?rhel} >= 7

# Systemd unit files
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/shellinaboxd.service

%else

# Initscripts
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_initrddir}/shellinaboxd

%endif

install -m0644 -D shellinabox.sysusers.conf %{buildroot}%{_sysusersdir}/shellinabox.conf

%pre
%if 0%{?fedora} || 0%{?rhel} >= 7

%post
%systemd_post shellinaboxd.service

%preun
%systemd_preun shellinaboxd.service

%postun
%systemd_postun_with_restart shellinaboxd.service

%endif

%if 0%{?rhel} == 6

%post
/sbin/chkconfig --add shellinaboxd

%preun
if [ "$1" = 0 ]; then
        /sbin/service shellinaboxd stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del shellinaboxd
fi

%postun
if [ "$1" -ge "1" ]; then
        /sbin/service shellinaboxd condrestart >/dev/null 2>&1 || :
fi

%endif

%files
%{!?_licensedir:%global license %%doc}
%doc AUTHORS NEWS README README.Fedora
%doc shellinabox/styles.css shellinabox/print-styles.css
%doc shellinabox/shell_in_a_box.js
%config(noreplace) %{_sysconfdir}/sysconfig/shellinaboxd
%{_mandir}/man1/shellinaboxd.1.*
%{_datadir}/%{name}
%{_sbindir}/shellinaboxd
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/shellinaboxd.service
%else
%{_initrddir}/shellinaboxd
%endif
%attr(750,%{username},%{username}) %{_sharedstatedir}/%{name}
%{_sysusersdir}/shellinabox.conf

%changelog
%autochangelog
