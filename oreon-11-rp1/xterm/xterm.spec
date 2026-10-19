%global source3_hash a2342029672532256110ef28a0ea1addb7f6fd1f08aacc382d0fbe2308f178c2
%global source2_hash eec7eccb51a27ae633784d1b1ef42eb775130c782ea51a6c47fa7a901484d6db
%global source1_hash 0911b18c35befc6662729f3a22088489cfd8583eb887a614aca2bcb22ded42ce
%global source0_hash 969be283670deadd66934865c4de6c5ab045e3a3facc2b228decf91a20d8c36c
%bcond_with trace
Summary:        Terminal emulator for the X Window System
Name: xterm
Version: 411
Release:        1%{?dist}
URL: https://invisible-island.net/xterm
License: MIT AND X11 AND HPND AND CC-BY-4.0
Recommends: xorg-x11-fonts-misc
Source0:        https://invisible-island.net/archives/xterm/%{name}-%{version}.tgz
Source1:        https://invisible-island.net/archives/xterm/%{name}-%{version}.tgz.asc
Source2: https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
Source3: https://invisible-island.net/archives/xterm/16colors.txt
Patch1: xterm-defaults.patch
Patch2: xterm-desktop.patch
Patch3: xterm-man-paths.patch
%global x11_app_defaults_dir %(pkg-config --variable appdefaultdir xt)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libutempter-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-posix)
# /oreon:deps
%description
The xterm program is a terminal emulator for the X Window System. It
provides DEC VT102 and Tektronix 4014 compatible terminals for
programs that can't use the window system directly.

%package resize
Summary: Set environment and terminal settings to current window size
%description resize
Prints a shell command for setting the appropriate environment variables to
indicate the current size of the window from which the command is run.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

for f in THANKS; do
	iconv -f iso8859-1 -t utf8 -o ${f}{_,} &&
		touch -r ${f}{,_} && mv -f ${f}{_,}
done

%build

%configure \
	--enable-meta-sends-esc \
	--disable-backarrow-key \
	--enable-exec-xterm \
%{?with_trace: --enable-trace} \
	--enable-warnings \
	--with-app-defaults=%{x11_app_defaults_dir} \
	--with-icon-theme=hicolor \
	--with-icondir=%{_datadir}/icons \
	--with-utempter \
	--with-tty-group=tty \
	--disable-full-tgetent \
	--with-pcre2 \
	--enable-readline-mouse \
	--enable-logging
%make_build
%install
%make_install
cp -fp %{SOURCE3} 16colors.txt
desktop-file-install \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	xterm.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -m644 -p xterm.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xterm-resize -f %{oreon_filedir}/xterm-resize.list

%changelog

%autochangelog
