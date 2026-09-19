%global source0_hash 88d9795bf51af3496fdce2fec263363ff90929e0e7036f9c117fb2b829353b6b

Name:           spicctrl
Version:        1.9
Release:        39%{?dist}
Summary:        Sony Vaio laptop SPIC control program

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://popies.net/sonypi/
Source0:        http://popies.net/sonypi/spicctrl-%{version}.tar.bz2

ExclusiveArch:	%{ix86} x86_64

BuildRequires: make
BuildRequires:  gcc
%description
spicctrl queries and sets a variety of parameters on Sony Vaio laptop
computers, including AC Power status, battery status, screen brightness,
and bluetooth device power status

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{__sed} -i 's/ -O2 / $(RPM_OPT_FLAGS) /' Makefile

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m755 spicctrl $RPM_BUILD_ROOT%{_sbindir}
install -p -m644 spicctrl.1 $RPM_BUILD_ROOT%{_mandir}/man1

%post
if [ ! -c /dev/sonypi ]; then
	rm -f /dev/sonypi
	mknod /dev/sonypi c 10 250
fi
if [ -e /etc/modprobe.conf ]; then
	grep 'alias char-major-10-250 sonypi' /etc/modprobe.conf > /dev/null
	RETVAL=$?
	if [ $RETVAL -ne 0 ]; then
		echo 'alias char-major-10-250 sonypi' >> /etc/modprobe.conf
		echo 'options sonypi minor=250' >> /etc/modprobe.conf
	fi
fi

%files
%doc AUTHORS CHANGES LICENSE
%{_sbindir}/spicctrl
%{_mandir}/man1/spicctrl.1.gz

%changelog
%autochangelog
