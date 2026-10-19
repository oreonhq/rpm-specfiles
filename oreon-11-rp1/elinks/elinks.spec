%global source0_hash 75af7ba88af99ff5069ec7b4b7a3241d5920f4089764c7297cff3c8484a9e33f
%bcond_with gpm
Name:      elinks
Summary:        A text-mode Web browser
Version:   0.20.0
Release:        1%{?dist}
License:   GPL-2.0-only
URL:       https://github.com/rkd77/elinks
Source0:        https://github.com/rkd77/elinks/releases/download/v%{version}/elinks-%{version}.tar.xz
Source2:        elinks.conf
%if %{with gpm}
%endif
Requires(preun): %{_sbindir}/alternatives
Requires(post): coreutils
Requires(post): %{_sbindir}/alternatives
Requires(postun): coreutils
Requires(postun): %{_sbindir}/alternatives
Provides: webclient
Provides: links = 1:0.97-1
Provides: text-www-browser
Patch0:        0000-elinks-0.19.0-ssl-noegd.patch
Patch1:        0001-elinks-0.15.1-utf_8_io-default.patch
Patch3:        elinks-0.11.0-getaddrinfo.patch
Patch4:        0004-elinks-0.15.0-sysname.patch
Patch5:        0005-elinks-0.15.0-xterm.patch
Patch6:        elinks-0.12pre6-list_is_singleton.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  krb5-devel
BuildRequires:  libidn2-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
%description
Elinks is a text-based Web browser. Elinks does not display any images,
but it does support frames, tables and most other HTML tags. Elinks'
advantage over graphical browsers is its speed--Elinks starts and exits
quickly and swiftly displays Web pages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n elinks-%{version}

# remove bogus serial numbers
sed -e 's/^# *serial [AM0-9]*$//' -i config/m4/*.m4

# recreate autotools files
aclocal -I config/m4
autoconf
autoheader

%build

export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) -D_GNU_SOURCE"
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
%oreon_autofiles main

%postun

if [ "$1" -ge "1" ]; then
	links=`readlink %{_sysconfdir}/alternatives/links`
	if [ "$links" == "%{_bindir}/elinks" ]; then
		%{_sbindir}/alternatives --set links %{_bindir}/elinks
	fi
fi
exit 0
%post

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
