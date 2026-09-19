%global source0_hash a18446040cfaadd51c1ce77bb06ba6860372a70a04e36962e2635253a1f693a3

# Don't provide any font Provides
%global	__fontconfig_provides	%{nil}
# ... and it seems that the above method no longer works
# on F-15 (bug 677760)
%global	__font_provides	%{nil}

Summary:   Japanese Console for Linux Frame Buffer Device
Name:      jfbterm
Version:   0.4.7
Release:   61%{?dist}
# COPYING		BSD-2-Clause
# SPDX confirmed
License:   BSD-2-Clause
Source0:   http://downloads.sourceforge.jp/jfbterm/13501/jfbterm-%{version}.tar.gz
Patch0:    jfbterm-0.4.6-conf.patch
#Patch1:    jfbterm-0.4.6-Makefile.patch
Patch1:    jfbterm-0.4.7-remove-sticky.patch
#Patch2:   jfbterm-0.4.6-x86_64.patch
Patch3:    jfbterm-0.4.7-infinite_loop.patch
# What is patch4 for??
#Patch4:    jfbterm-0.4.7-configure-header.patch
Patch5:    jfbterm-0.4.7-userspace.patch
Patch10:   jfbterm-0.4.7-remove-warning.patch
Patch11:   jfbterm-0.4.7-mmap-newkernel.patch
Patch12:   jfbterm-0.4.7-hang-onexit.patch
Patch13:   jfbterm-0.4.7-pagemask_userspace.patch
# Some people see jfbterm hang or segv with invalid ut_id
# (bug 698532)
Patch15:   jfbterm-0.4.7-hang-on-utmp-refresh-with-invalid-utid.patch
Patch16:   jfbterm-0.4.7-wrong-inline-gcc5.patch
Patch17:   jfbterm-configure-c99.patch

URL:         http://jfbterm.sourceforge.jp/

BuildRequires:   gcc
BuildRequires:   gzip
# BuildRequires:   autoconf
# for tic
BuildRequires:   ncurses
# Now efont-unicode-bdf is split.
BuildRequires:   efont-unicode-bdf
BuildRequires:   xorg-x11-fonts-misc
BuildRequires:   japanese-bitmap-fonts
BuildRequires:   jisksp16-1990-fonts
BuildRequires:   make
# Now fonts are symlinks so really these rpms are required.
#Requires:   efont-unicode-bdf
#Requires:   xorg-x11-fonts-base
#Requires:   xorg-x11-fonts-misc
#Requires:   japanese-bitmap-fonts

%description
JFBTERM/ME takes advantages of framebuffer device that is 
supported since linux kernel 2.2.x (at least on ix86 architecture) 
and make it enable to display multilingual text on console. 
It is developed on ix86 architecture, and it will works on 
other architectures such as linux/ppc.

Features:
   * It works with framebuffer device instead of VGA.
   * It supports pcf format font
   * It is not so fast because it doesn't take any advantages 
     of accelaration.
   * It also support coding systems other than ISO-2022, 
     such as SHIFT-JIS by using iconv(3).
   * It is userland program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .conf
%patch -P1 -p1 -b .remove_sticky
%patch -P5 -p1 -b .userspace
%patch -P3 -p1 -b .infinite_loop
# ???
#%%patch4 -p1 -b .conf_header
%patch -P10 -p1 -b .remove_warn
%patch -P11 -p1 -b .nmap_newkernel
%patch -P12 -p1 -b .hang_onexit
%patch -P13 -p1 -b .pagemask
%patch -P15 -p1 -b .utid_with_refresh
%patch -P16 -p1 -b .inline_gcc5
%patch -P17 -p1

#autoconf
touch Makefile.in aclocal.m4 config.h.in configure stamp-h.in

%build
# Copy fonts for a moment.
cp -p %{_datadir}/fonts/japanese/efont-unicode-bdf/b16.pcf.gz fonts/

%configure --enable-direct-color
touch stamp-h
%{__make} %{?_smp_mflags}

tic -C terminfo.jfbterm > jfbterm.termcap

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_sysconfdir}
%{__mkdir_p} %{buildroot}%{_datadir}/fonts/jfbterm

%{__make} DESTDIR=%{buildroot} install

%{__mv} %{buildroot}%{_sysconfdir}/jfbterm.conf.sample \
   %{buildroot}%{_sysconfdir}/jfbterm.conf

%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__install} -m 644 jfbterm.1 %{buildroot}%{_mandir}/man1
%{__install} -m 644 jfbterm.conf.5 %{buildroot}%{_mandir}/man5

%{__mkdir_p} %{buildroot}%{_datadir}/terminfo/j
tic -o %{buildroot}%{_datadir}/terminfo terminfo.jfbterm

# install fonts by symlink
# for fc5 and above, X11R6 directory is no longer used.
#%%{__rm} -rf %{buildroot}%{_datadir}/fonts/jfbterm/*

cp -p \
   %{_datadir}/fonts/japanese/efont-unicode-bdf/b16.pcf.gz \
   %{buildroot}%{_datadir}/fonts/jfbterm/

# For hanglg16, see https://bugzilla.redhat.com/show_bug.cgi?id=1952723
for font in \
   shnm8x16r.pcf.gz shnmk16.pcf.gz jisksp16-1990.pcf.gz \
   8x16.pcf.gz gb16fs.pcf.gz \
%if 0%{?fedora} < 34
   hanglg16.pcf.gz \
%endif
   ; do
   status=1
   for path in \
      %{_datadir}/fonts/japanese-bitmap-fonts \
      %{_datadir}/fonts/{japanese,ja}/misc \
      %{_datadir}/fonts/jisksp16-1990-fonts \
      %{_datadir}/fonts/jisksp16-1990 \
      %{_datadir}/fonts/japanese-bitmap \
      %{_datadir}/X11/fonts/misc \
       ; do
      if [ -f $path/$font -a $status = 1 ] ; then
         cp -p $path/$font %{buildroot}%{_datadir}/fonts/jfbterm/
         status=0
         break
      fi
   done
   if [ $status = 1 ] ; then exit 1 ; fi
done

status=1
for num in `seq 1 15` ; do
   font=8x13-ISO8859-${num}.pcf.gz
   path=%{_datadir}/X11/fonts/misc
   if [ -f $path/$font ] ; then
    cp -p $path/$font %{buildroot}%{_datadir}/fonts/jfbterm/
    status=0
   fi
done
if [ $status = 1 ] ; then exit 1 ; fi

%{__cat} > 60-jfbterm.perms <<EOF
# permission definitions
<console> 0660 /dev/tty0    0660 root
<console> 0600 /dev/console 0600 root
EOF

%{__mkdir_p} -m 755 %{buildroot}%{_sysconfdir}/security/console.perms.d
%{__install} -m 644 60-jfbterm.perms \
   %{buildroot}%{_sysconfdir}/security/console.perms.d/

# Change documents' fonts to UTF-8
%{__sed} -i -e 's|\r||' AUTHORS

for f in AUTHORS ChangeLog ; do
   %{__mv} ${f} ${f}.orig
   iconv -f ISO-2022-JP -t UTF8 ${f}.orig > ${f} && \
   %{__rm} -f ${f}.orig || %{__mv} ${f}.orig ${f}
done
%{__mv} README.ja README.ja.orig
iconv -f EUCJP -t UTF8 README.ja.orig > README.ja && \
   %{__rm} -f README.ja.orig || %{__mv} README.ja.orig README.ja

# Remove terminfo from FC-7
%{__rm} -rf %{buildroot}%{_datadir}/terminfo/

%files
%doc AUTHORS
%license COPYING
%doc ChangeLog
%doc NEWS
%doc README*
%doc jfbterm.termcap
%{_bindir}/jfbterm
%config(noreplace) %{_sysconfdir}/jfbterm.conf
%config(noreplace) %{_sysconfdir}/security/console.perms.d/60-jfbterm.perms
%{_datadir}/fonts/jfbterm
%dir %{_datadir}/fonts
%{_mandir}/man1/jfbterm.1*
%{_mandir}/man5/jfbterm.conf.5*

%changelog
%autochangelog
