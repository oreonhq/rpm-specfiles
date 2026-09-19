%global source0_hash 4fffab9652c760199c074533d1d3929bea55ab4233b11e735b0f1856d1ceec57

Summary: A heuristic autodialer for PPP connections
Name: wvdial
Version: 1.61
Release: 37%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://alumnit.ca/wiki/?WvDial
#Old location for <1.61 was http://alumnit.ca/download/wvdial-%%{version}.tar.gz
Source0: http://wvstreams.googlecode.com/files/wvdial-%{version}.tar.gz

#allow specifying the remotename at startup-time
Patch1: wvdial-1.60-remotename.patch
#added support for up to 9 alternative numbers instead of 4(#178025)
Patch2: wvdial-1.54-9nums.patch
#change Compuserve "Classic" login prompt to the "new" style (#146664)
Patch3: wvdial-1.60-compuserve.patch
#fixed wvdial.conf (5) manpage (#440161)
Patch4: wvdial-manpages.patch
# Patches from Debian
Patch5: wvdial-1.61-typo_pon.wvdial.1.patch
Patch6: wvdial-1.61-ftbfs_with_gcc_4.5.patch
# _BSD_SOURCE is deprecated.
Patch7: wvdial-1.61-use_DEFAULT_SOURCE.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: libwvstreams-devel lockdev-devel openssl-devel
BuildRequires: pkgconfig
Requires: ppp

%description
WvDial automatically locates and configures modems and can log into
almost any ISP's server without special configuration. You need to
input the username, password, and phone number, and then WvDial will
negotiate the PPP connection using any mechanism needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .remotename
%patch -P2 -p1 -b .9nums
%patch -P3 -p1 -b .compuserve
%patch -P4 -p1 -b .manpages
%patch -P5 -p1 -b .typo_pon_wvdial
%patch -P6 -p1 -b .ftbfs_with_gcc_45
%patch -P7 -p1 -b ._DEFAULT_SOURCE

%build
%configure
make \
	CPPOPTS="%{optflags} -DUSE_LOCKDEV=1" \
	LDOPTS="%{?__global_ldflags}" \
	LOCKDEV=-llockdev \
	XX_LIBS="-lcrypt -llockdev" \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	PPPDIR=%{_sysconfdir}/ppp/peers $@

%install
%make_install \
	PREFIX=%{buildroot}%{_prefix} \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir} \
	PPPDIR=%{buildroot}%{_sysconfdir}/ppp/peers
rm %{buildroot}%{_sysconfdir}/ppp/peers/wvdial-pipe
touch %{buildroot}%{_sysconfdir}/wvdial.conf

%files
%doc CHANGES* README* TODO FAQ
%license COPYING*
%{_bindir}/wvdialconf
%{_bindir}/wvdial
%{_mandir}/man1/wvdialconf.*
%{_mandir}/man1/wvdial.*
%{_mandir}/man5/wvdial.conf*
%attr(0600,root,daemon)	%config(noreplace) %{_sysconfdir}/ppp/peers/wvdial
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/wvdial.conf

%changelog
%autochangelog
