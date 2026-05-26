# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 fbb934d7253a4ca6cd55f638b0bf97016db4a253d66acfa2b8fa76bad2db9e62
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global forgeurl https://github.com/libimobiledevice/usbmuxd
%global commit 0b1b233b57d581515978a09e5a4394bfa4ee4962
%global date 20240915
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           usbmuxd
Version:        1.1.1^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Daemon for communicating with Apple's iOS devices
License:        GPL-3.0-only OR GPL-2.0-only
URL:            https://libimobiledevice.org
Source0:        https://github.com/libimobiledevice/usbmuxd/archive/0b1b233b57d581515978a09e5a4394bfa4ee4962/usbmuxd-0b1b233b57d581515978a09e5a4394bfa4ee4962.tar.gz
Source1:        %{name}.sysusers
Source2:        %{name}.tmpfiles

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd
%{?sysusers_requires_compat}

BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  libusbx-devel

Requires:       systemd-udev
Recommends:     systemd

%description
usbmuxd is a daemon used for communicating with Apple's iPod Touch, iPhone, 
iPad and Apple TV devices. It allows multiple services on the device to be 
accessed simultaneously.

%prep
%oreon_verify_sources
%autosetup -p1 -n %{name}-%{commit}

%if %{defined commit}
echo %{version} > .tarball-version
%endif

# Set the owner of the device node to be usbmuxd
sed -i.owner 's/OWNER="usbmux"/OWNER="usbmuxd"/' udev/39-usbmuxd.rules.in
sed -i.user 's/--user usbmux/--user usbmuxd/' systemd/usbmuxd.service.in

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/lib/lockdown/
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/usbmuxd.conf
install -Dpm0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/usbmuxd.conf

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post usbmuxd.service

%preun
%systemd_preun usbmuxd.service

%postun
%systemd_postun_with_restart usbmuxd.service 

%files
%license COPYING.GPLv2 COPYING.GPLv3
%doc AUTHORS README.md
%{_unitdir}/usbmuxd.service
%{_udevrulesdir}/39-usbmuxd.rules
%{_sbindir}/usbmuxd
%{_datadir}/man/man8/usbmuxd.8.gz
%attr(2775, usbmuxd, usbmuxd) %dir %{_localstatedir}/lib/lockdown/
%{_sysusersdir}/usbmuxd.conf
%{_tmpfilesdir}/usbmuxd.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1^%{date}git%{shortcommit}-1
- Prepare for Oreon 11 (RP1)
