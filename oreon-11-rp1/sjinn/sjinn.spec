%global source0_hash 0ba8aaf1ce4312f712b9a826151fcde94df7a8f83eaea335a4260c87e14a4123

Name:           sjinn
Version:        1.01
Release:        35%{?dist}
Summary:        Simple tool for sending & receiving data from RS-232 devices

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sjinn.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

# installer should use 0644 permissions for man page
# https://sourceforge.net/tracker/?func=detail&aid=3294964&group_id=26187&atid=386394
Patch0:         sjinn-install-args.patch

# Add DESTDIR as argument for install
# https://sourceforge.net/tracker/?func=detail&aid=3294967&group_id=26187&atid=386394
Patch1:         sjinn-install-DESTDIR.patch

# Uncompress man pages
# https://sourceforge.net/tracker/?func=detail&aid=3294981&group_id=26187&atid=386394
Patch2:         sjinn-uncompress-man-pages.patch

# Fix optstring for proper -r handling
# https://sourceforge.net/tracker/?func=detail&aid=3324235&group_id=26187&atid=386394
Patch3:         sjinn-optarg-r-fix.patch
Patch4: sjinn-configure-c99.patch

%description
S-Jinn is a free, lightweight, open-source Linux application written in
C. It is a simple command-line tool designed for sending & receiving
data from PC controlled TIA/EIA-232 (RS-232) test, measurement,
and control devices.

Depending on your application you may be able to use stty or
C-Kermit, but I believe you will find that S-Jinn is easier-to-use,
more intuitive, and more concise in the area of command-line and/or
scripted RS-232 data acquisition and control.

Popular Linux communications packages like Minicom will also
communicate with RS-232 devices, but they are better suited to modems,
computers, network devices, etc. They typically lack support for any
combination of UART communication settings required by many of the
RS-232 test, measurement, and control devices on the market.

Most communications packages also lack command-line support. Some
provide scripting languages, but S-Jinn frees you from
application-specific languages. S-Jinn simply directs the data to
STDOUT where you can display it, pipe it, and/or redirect it to
be processed by your favorite Unix shell and/or scripting language
regardless of whether you prefer Bash, Python, Perl, Expect, or you
name it.

Other S-Jinn features include the ability to:

    * Control RS-232 DTR and RTS lines from the command-line

    * Display DTR, RTS, CTS & DSR status

    * Send control characters (including the NULL character)

    * Send values in hex

    * Specify read length

    * Set programmable delay times for both send & read.

    * Support for virtually all baud rates, parity, and data lengths
      found in standard PC UARTS

    * Output Formatting: ASCII, hex, ASCII-over-hex, wrap text,
      truncate lines, suppress trailing line feeds

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
tar -xzf scripts.tar.gz
gunzip rs232.1.gz

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

# Fix some file permissions
chmod -x INSTALL COPYING README EXAMPLES FAQS ChangeLog Makefile \
        configure.in *.1 *.[ch] scripts/*

# Fix end-of-line encoding
sed -i 's/\r//' COPYING

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" prefix=%{_prefix}

%install
rm -rf %{buildroot}
make INSTALL="install -cDp" DESTDIR=%{buildroot} prefix=%{_prefix} \
        mandir=%{_mandir}/man1 install

%files
%{_bindir}/rs232
%{_bindir}/%{name}
%{_mandir}/man1/*
%license COPYING
%doc README EXAMPLES FAQS ChangeLog scripts

%changelog
%autochangelog
