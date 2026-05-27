%global source0_hash none

%bcond_with multiuser
%global _hardened_build 1

Summary:        A screen manager that supports multiple logins on one terminal
Name:           screen
Version:        5.0.1
Release:        6%{?dist}
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/screen
BuildRequires: make
BuildRequires:  ncurses-devel pam-devel libutempter-devel autoconf texinfo
BuildRequires:  libxcrypt-devel
BuildRequires:  automake gcc
# for %%_tmpfilesdir macro
BuildRequires:  systemd

Source0:        https://ftp.gnu.org/gnu/screen/screen-%{version}.tar.gz
Source1:        screen.pam

Patch1:         screen-5.0.0-screenrc.patch
Patch2:         screen-5.0.0-suppress_remap.patch
Patch3:         screen-5.0.1-fix-unescaped-in-email-address.patch
# https://cgit.git.savannah.gnu.org/cgit/screen.git/commit/?h=screen-v5&id=ccd0b27504707e4f3099f0b9fd7a89489c6973fb
Patch4:        screen-5.0.1-big-endian.patch

%description
The screen utility allows you to have multiple logins on just one
terminal. Screen is useful for users who telnet into a machine or are
connected via a dumb terminal, but want to use more than just one
login.

Install the screen package if you need a screen manager that can
support multiple logins on one terminal.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# Create a sysusers.d config file
cat >screen.sysusers.conf <<EOF
g screen 84
EOF

%build
./autogen.sh

%configure \
	--enable-pam \
	--enable-telnet \
	--with-pty-mode=0620 \
	--with-pty-group=$(getent group tty | cut -d : -f 3) \
	--with-system_screenrc="%{_sysconfdir}/screenrc" \
	--enable-socket-dir="%{_rundir}/screen" \

# We would like to have braille support.
sed -i -e 's/.*#.*undef.*HAVE_BRAILLE.*/#define HAVE_BRAILLE 1/;' config.h

sed -i -e 's/\(\/usr\)\?\/local\/etc/\/etc/g;' doc/screen.{1,texinfo}

for i in doc/screen.texinfo; do
    iconv -f iso8859-1 -t utf-8 < $i > $i.utf8 && mv -f ${i}{.utf8,}
done

rm -f doc/screen.info*

# fails with %{?_smp_mflags}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT%{_bindir}/screen{-%{version},}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -m 0644 etc/etcscreenrc $RPM_BUILD_ROOT%{_sysconfdir}/screenrc
cat etc/screenrc >> $RPM_BUILD_ROOT%{_sysconfdir}/screenrc

# Better not forget to copy the pam file around
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/screen

# Create the socket dir
mkdir -p $RPM_BUILD_ROOT%{_rundir}/screen

# And tell systemd to recreate it on start with tmpfs
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
cat <<EOF > $RPM_BUILD_ROOT%{_tmpfilesdir}/screen.conf
# screen needs directory in /run
%if %{with multiuser}
d %{_rundir}/screen 0755 root root
%else
d %{_rundir}/screen 0775 root screen
%endif
EOF

# Remove files from the buildroot which we don't want packaged
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

install -m0644 -D screen.sysusers.conf %{buildroot}%{_sysusersdir}/screen.conf


%files
%doc README doc/FAQ doc/README.DOTSCREEN ChangeLog
%license COPYING
%{_mandir}/man1/screen.*
%{_infodir}/screen.info*
%{_datadir}/screen
%config(noreplace) %{_sysconfdir}/screenrc
%config(noreplace) %{_sysconfdir}/pam.d/screen
%{_tmpfilesdir}/screen.conf
%if %{with multiuser}
%attr(4755,root,root) %{_bindir}/screen
%attr(755,root,root) %{_rundir}/screen
%else
%attr(2755,root,screen) %{_bindir}/screen
%attr(775,root,screen) %{_rundir}/screen
%endif
%{_sysusersdir}/screen.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.1-6
- Import
