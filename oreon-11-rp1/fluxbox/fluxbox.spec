%global source0_hash d47a58edba857f3c36bf8430bbd17834693ad0e6aa431d3507039f022af7aee8

Name:           fluxbox
Version:        1.3.7
Release:        29%{?dist}

Summary:        Window Manager based on Blackbox

License:        MIT
URL:            http://fluxbox.org

Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source3:        fluxbox-xsessions.desktop
Source5:        fluxbox-applications.desktop

Patch0:         fluxbox-startfluxbox-pulseaudio.patch
Patch1:         %{name}-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  imlib2-devel
BuildRequires:  zlib-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  libtool
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       artwiz-aleczapka-fonts
%if ( 0%{?fedora} >= 31) || (0%{?rhel} >= 8)
Requires:       python3-pyxdg
%else
Requires:       pyxdg
%endif

# provide clean upgrade path from old fluxconf tool (#662836)
Provides: fluxconf = 0.9.9-9
Obsoletes: fluxconf < 0.9.9-9

%description
Fluxbox is yet another window-manager for X.  It's based on the Blackbox 0.61.1
code. Fluxbox looks like blackbox and handles styles, colors, window placement
and similar thing exactly like blackbox (100% theme/style compatibility).  So
what's the difference between fluxbox and blackbox then?  The answer is: LOTS!

Have a look at the homepage for more info ;)

%package pulseaudio
Summary:        Enable pulseaudio support
Requires:       %{name} = %{version}-%{release}
Requires:       alsa-plugins-pulseaudio
Requires:       pulseaudio pulseaudio-module-x11 pulseaudio-utils
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:      noarch
%endif

%description pulseaudio
Enable pulseaudio support.

%package vim-syntax
Summary:        Fluxbox syntax scripts for vim
Requires:       %{name} = %{version}-%{release}
Requires:       vim-filesystem
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:      noarch
%endif

%description vim-syntax
Enable vim syntax highlighting support for fluxbox configuration files (menu,
keys, apps).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build
%configure \
  --enable-xft \
  --enable-xinerama \
  --enable-imlib2 \
  --enable-nls \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir} \

%make_build LIBTOOL=/usr/bin/libtool

%install
%make_install

# this is for desktop integration
mkdir -p %{buildroot}%{_datadir}/xsessions/
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 0644 -p %{SOURCE3} %{buildroot}%{_datadir}/xsessions/fluxbox.desktop
install -m 0644 -p %{SOURCE5} %{buildroot}%{_datadir}/applications/fluxbox.desktop

desktop-file-validate %{buildroot}%{_datadir}/xsessions/fluxbox.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/fluxbox.desktop

# fix 388971
mkdir -p %{buildroot}%{_sysconfdir}
touch -r ChangeLog %{buildroot}%{_sysconfdir}/fluxbox-pulseaudio

# vim syntax files
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/syntax/
install -m 0644 -p 3rd/vim/vim/syntax/fluxapps.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/fluxapps.vim
install -m 0644 -p 3rd/vim/vim/syntax/fluxkeys.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/fluxkeys.vim
install -m 0644 -p 3rd/vim/vim/syntax/fluxmenu.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/fluxmenu.vim

%files
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/%{name}
%{_datadir}/xsessions/fluxbox.desktop
%{_datadir}/applications/fluxbox.desktop

%files pulseaudio
%{_sysconfdir}/fluxbox-pulseaudio

%files vim-syntax
%{_datadir}/vim/vimfiles/syntax/flux*.vim

%changelog
%autochangelog
