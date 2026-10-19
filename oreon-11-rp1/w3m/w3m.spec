%global source0_hash fdc7d55d3c0104db26aa9759db34f37e5eee03f44c868796e3bbfb8935c96e39
%global build_options  --enable-m17n --enable-unicode --enable-nls --with-editor=/bin/vi --with-mailer="gnome-open mailto:%s" --with-browser=gnome-open --with-charset=UTF-8 --with-gc --with-termlib=ncurses --enable-nntp --enable-gopher --enable-image=x11,fb --with-imagelib=gtk2 --enable-keymap=w3m
%global gitdate 20230121
%{?perl_default_filter}
%global __requires_exclude perl\\(w3mhelp-
Name:     w3m
Version:  0.5.3
Release:        1%{?dist}
License:  MIT AND Unicode-DFS-2015
URL:      http://w3m.sourceforge.net/
%ifnarch s390 s390x
%endif
Requires: perl(NKF)
Source0:        https://github.com/tats/%{name}/archive/v%{version}+git%{gitdate}/%{name}-%{version}+git%{gitdate}.tar.gz
Source1: w3mconfig
Patch0: https://github.com/tats/w3m/pull/273/commits/edc602651c506aeeb60544b55534dd1722a340d3.patch#/w3m-0.5.3-fix-oob-access.patch
Summary:        Pager with Web browsing abilities
Provides: webclient
Provides: text-www-browser
# oreon:deps
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  gettext-devel
BuildRequires:  gpm-devel
BuildRequires:  gtk2-devel
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  nkf
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
# /oreon:deps
%description
The w3m program is a pager (or text file viewer) that can also be used
as a text-mode Web browser. W3m features include the following: when
reading an HTML document, you can follow links and view images using
an external image viewer; its internet message mode determines the
type of document from the header; if the Content-Type field of the
document is text/html, the document is displayed as an HTML document;
you can change a URL description like 'http://hogege.net' in plain
text into a link to that URL.
If you want to display the inline images on w3m, you need to install
w3m-img package as well.

%package img
Summary: Helper program to display the inline images for w3m
BuildRequires:  gtk2-devel
BuildRequires:  gdk-pixbuf2-xlib-devel
Requires: ImageMagick
Requires: %{name}%{?_isa} = %{version}-%{release}
%description img
w3m-img package provides a helper program for w3m to display the inline
images on the terminal emulator in X Window System environments and the
linux framebuffer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-git%{gitdate} -p1

%build

export CFLAGS="$CFLAGS -std=gnu17"
%configure %{build_options}
%make_build
%install
%make_install
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/w3m/config
rm -f doc*/w3m.1
%find_lang w3m
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n w3m-img -f %{oreon_filedir}/w3m-img.list

%changelog

%autochangelog
