%global source0_hash 0ff48a5cd9e9cfe8e815a24e023734919e9a3b7ad2f039243ad121cf5aabf6c6

%global         _firmwarepath    /usr/lib/firmware

Name:           wireless-regdb
Version:        2026.02.04
Release:        1%{?dist}
Summary:        Regulatory database for 802.11 wireless networking

License:        ISC
URL:            https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
BuildArch:      noarch

Requires:       udev, iw
Requires:       systemd >= 190

BuildRequires:  make
BuildRequires:  systemd-devel

Provides:       crda = 3.18_2019.03.01-3
Obsoletes:      crda <= 3.18_2019.03.01-2

Source0:        http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-2026.02.04.tar.xz
Source1:        setregdomain
Source2:        setregdomain.1
Source3:        85-regulatory.rules


%description
The wireless-regdb package provides the regulatory rules database
used by the kernels 802.11 networking stack in order to comply 
with radio frequency regulatory rules around the world.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
: # Package installs a firmware-like, prebuilt binary from upstream...


%install
make install DESTDIR=%{buildroot} MANDIR=%{_mandir} \
	FIRMWARE_PATH=%{_firmwarepath}

install -D -pm 0755 %SOURCE1 %{buildroot}%{_sbindir}/setregdomain
install -D -pm 0644 %SOURCE2 %{buildroot}%{_mandir}/man1/setregdomain.1
install -D -pm 0644 %SOURCE3 %{buildroot}%{_udevrulesdir}/85-regulatory.rules

rm -rf %{buildroot}/usr/lib/crda


%files
%{_sbindir}/setregdomain
%{_udevrulesdir}/85-regulatory.rules
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s
%{_mandir}/man1/setregdomain.1*
%{_mandir}/man5/regulatory.db.5*
%{_mandir}/man5/regulatory.bin.5*
%license LICENSE
%doc README


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2026.02.04-1
- Prepare for Oreon 11 (RP1)
