%global source0_hash b800a499df21b9993e0ceb36bce18046b3d4622df85693a8b5b40dcf21a78b4f

%global upstream_name xe-guest-utilities
%global service_name xe-linux-distribution

Summary: XAPI Virtual Machine Monitoring Scripts
Name:    %{upstream_name}-latest
Version: 8.4.0
Release: %autorelease
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/xenserver/%{upstream_name}
Source0: %{url}/archive/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
# Follow upstream to enable net.ipv4.conf.all.arp_notify
Patch0:  enable_net.ipv4.conf.all.arp_notify.patch

# XAPI project only supports ix86 and x86_64 virtual machine
ExclusiveArch: %{ix86} x86_64
BuildRequires: make
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: systemd
# the only version that has been built in Fedora
Obsoletes:     %{upstream_name} = 7.12.0
%{?systemd_requires}

%description
Scripts for monitoring XAPI project virtual machine.

Writes distribution version information and IP address to XenStore.

This package follows the latest version of %{upstream_name} upstream.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{version}
mkdir -p src/github.com/xenserver
ln -s $PWD src/github.com/xenserver/xe-guest-utilities

sed -i -e 's:/usr/share/oem/xs:%{_sbindir}:' mk/%{service_name}.service

%build
GOPATH=$PWD:%{gopath} %{gomodulesmode} make \
     GO_FLAGS='-a -ldflags "${LDFLAGS:-}%{?currentgoldflags} -B 0x$$(head -c20 /dev/urandom|od -An -tx1|tr -d '"'"' \n'"'"') -extldflags '"'"'%__global_ldflags %{?__golang_extldflags}'"'"' -compressdwarf=false" -v -x'

%install
mkdir -p %{buildroot}%{_sbindir}
mv -v build/stage/usr/sbin/* %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}/%{upstream_name}
mv -v build/stage/usr/bin/* %{buildroot}%{_libexecdir}/%{upstream_name}

mkdir -p %{buildroot}%{_unitdir}
cp -p mk/%{service_name}.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
cp -p mk/xen-vcpu-hotplug.rules %{buildroot}%{_udevrulesdir}/z10-xen-vcpu-hotplug.rules

mkdir -p %{buildroot}%{_localstatedir}/cache
touch %{buildroot}%{_localstatedir}/cache/%{service_name}

%check
mk/xe-linux-distribution

%post
%systemd_post %{service_name}.service

%preun
%systemd_preun %{service_name}.service

%postun
%systemd_postun_with_restart %{service_name}.service

%triggerun -- %{upstream_name}
if /bin/ls /etc/rc3.d/S*%{service_name} >/dev/null 2>&1; then
    # Re-enable the service if it was enabled in sysv mode
    /usr/bin/systemctl enable %{service_name} >dev/null 2>&1||:
    /bin/rm /etc/rc3.d/S*%{service_name} >/dev/null 2>&1||:
    /usr/bin/systemctl try-restart %{service_name} >dev/null 2>&1||:
fi

%files
%doc README.md
%license LICENSE
%{_sbindir}/%{service_name}
%{_sbindir}/xe-daemon
%{_unitdir}/%{service_name}.service
%{_udevrulesdir}/z10-xen-vcpu-hotplug.rules
%{_libexecdir}/%{upstream_name}
%ghost %{_localstatedir}/cache/%{service_name}

%changelog
%autochangelog
