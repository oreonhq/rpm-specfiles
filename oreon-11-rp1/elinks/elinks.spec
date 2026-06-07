%global source0_hash a993a4870cadce60abbc724cf6a5c2a80f6be9020243b9e5ce075c16c6665c04

%if 0%{?rhel} >= 10 || 0%{?rescue} || (0%{?oreon} >= 11)
%bcond_with gpm
%else
%bcond_without gpm
%endif

Name:      elinks
Summary:   A text-mode Web browser
Version:   0.19.0
Release:   2%{?dist}
License:   GPL-2.0-only
URL:       https://github.com/rkd77/elinks
Source:        https://github.com/rkd77/elinks/releases/download/v%{version}/elinks-%{version}.tar.xz
Source2:        elinks.conf

BuildRequires: automake
BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: gettext
%if %{with gpm}
BuildRequires: gpm-devel
%endif
BuildRequires: krb5-devel
BuildRequires: libidn2-devel
BuildRequires: lua-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
Requires(preun): %{_sbindir}/alternatives
Requires(post): coreutils
Requires(post): %{_sbindir}/alternatives
Requires(postun): coreutils
Requires(postun): %{_sbindir}/alternatives
Provides: webclient
Provides: links = 1:0.97-1
Provides: text-www-browser

# Prevent crash when HOME is unset (bug #90663).
Patch0:        0000-elinks-0.19.0-ssl-noegd.patch

# UTF-8 by default
Patch1:        0001-elinks-0.15.1-utf_8_io-default.patch

# Make getaddrinfo call use AI_ADDRCONFIG.
Patch3:        elinks-0.11.0-getaddrinfo.patch

# Don't put so much information in the user-agent header string (bug #97273).
Patch4:        0004-elinks-0.15.0-sysname.patch

# Fix xterm terminal: "Linux" driver seems better than "VT100" (#128105)
Patch5:        0005-elinks-0.15.0-xterm.patch

# let list_is_singleton() return false for an empty list (#1075415)
Patch6:        elinks-0.12pre6-list_is_singleton.patch

%description
Elinks is a text-based Web browser. Elinks does not display any images,
but it does support frames, tables and most other HTML tags. Elinks'
advantage over graphical browsers is its speed--Elinks starts and exits
quickly and swiftly displays Web pages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print \$1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n elinks-0.19.0

# remove bogus serial numbers
sed -e 's/^# *serial [AM0-9]*$//' -i config/m4/*.m4

# recreate autotools files
aclocal -I config/m4
autoconf
autoheader

%build
export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) -D_GNU_SOURCE"

# make the code build with lua-5.4.x
CFLAGS="$CFLAGS -DLUA_COMPAT_5_3"

%configure \
    --enable-256-colors             \
    --enable-bittorrent             \
    --with-gssapi                   \
    --with-lua                      \
    --with-openssl                  \
    %{?with_gpm:--with-gpm}         \
    %{!?with_gpm:--without-gpm}     \
    --without-gnutls                \
    --without-spidermonkey          \
    --without-x

%make_build -j1

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
install -D -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/elinks.conf
touch $RPM_BUILD_ROOT%{_bindir}/links
true | gzip -c > $RPM_BUILD_ROOT%{_mandir}/man1/links.1.gz
%find_lang elinks

%postun
if [ "$1" -ge "1" ]; then
	links=`readlink %{_sysconfdir}/alternatives/links`
	if [ "$links" == "%{_bindir}/elinks" ]; then
		%{_sbindir}/alternatives --set links %{_bindir}/elinks
	fi
fi
exit 0

%post
#Set up alternatives files for links
%{_sbindir}/alternatives --install %{_bindir}/links links %{_bindir}/elinks 90 \
  --slave %{_mandir}/man1/links.1.gz links-man %{_mandir}/man1/elinks.1.gz
links=`readlink %{_sysconfdir}/alternatives/links`
if [ "$links" == "%{_bindir}/elinks" ]; then
	%{_sbindir}/alternatives --set links %{_bindir}/elinks
fi


%preun
if [ $1 = 0 ]; then
	%{_sbindir}/alternatives --remove links %{_bindir}/elinks
fi
exit 0

%files -f elinks.lang
%license COPYING
%doc README.md
%ghost %verify(not md5 size mtime) %{_bindir}/links
%{_bindir}/elinks
%ghost %verify(not md5 size mtime) %{_mandir}/man1/links.1.gz
%config(noreplace) %{_sysconfdir}/elinks.conf
%{_mandir}/man1/elinks.1*
%{_mandir}/man5/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.0-2
- Import
