%global source0_hash 720f600817217257aa4c822e67814495dcb6c8d6326cdde5fe3ba1e457d9915d

%global udevdir %(pkg-config --variable=udevdir udev)

Name:       fbterm
Version:    1.7
Release:    34%{?dist}
License:    GPL-2.0-or-later
URL:        http://code.google.com/p/fbterm/
Source0:    https://github.com/fujiwarat/fbterm/releases/download/v%{version}/%{name}-%{version}.tar.gz

#Patch0:    %%{name}-1.2-kernel-header.patch
#Patch1:    %%{name}-1.3-setcap.patch
#Patch2:    %%{name}-1.4-iminput.patch
#Patch3:    %%{name}-1.6-rpmpack.patch
#Patch4:    %%{name}-1.6-el5.patch
Patch5:     %{name}-1.7-u16-build.patch

Summary:    A frame-buffer terminal emulator
Summary(zh_CN): 运行在帧缓冲的快速终端仿真器
Summary(zh_TW): 運行在frame-buffer的快速終端模擬機

BuildRequires: autoconf, automake
BuildRequires: fontconfig-devel gpm-devel
BuildRequires: gcc-c++
BuildRequires: pkgconfig(udev)
BuildRequires: make
Requires: fontconfig
# ncurses-term has /usr/share/terminfo/f/fbterm
Requires: ncurses-term
Obsoletes: fbterm-udevrules < %{version}-%{release}

%description
FbTerm is a fast terminal emulator for Linux with frame-buffer device. 
Features include: 
- mostly as fast as terminal of Linux kernel while accelerated scrolling
  is enabled on frame-buffer device 
- select font with fontconfig and draw text with freetype2, same as 
  Qt/Gtk+ based GUI apps 
- dynamically create/destroy up to 10 windows initially running default
  shell 
- record scroll back history for every window 
- auto-detect text encoding with current locale, support double width 
  scripts like  Chinese, Japanese etc 
- switch between configurable additional text encodings with hot keys
  on the fly 
- copy/past selected text between windows with mouse when gpm server 
  is running

%if 0%{?fedora} >= 9
%package udevrules
Summary:    udev rules that grant regular user access
Requires:   udev

%description udevrules
Regular users might use some applications that require access to frame-buffer device.
For example, ibus-fbterm requires access to /dev/fb0.
This sub-package enables regular user for such access.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%%patch0 -p0 -b .kernel-header
#%%patch1 -p0 -b .setcap
#%%patch2 -p0 -b .iminput
#%%patch3 -p0 -b .rpmpack
#%%if 0%{?fedora} >= 9
#%%else
#%%patch4 -p0 -b .el5
#%%endif
%patch -P5 -p1 -b .u16

%build
autoreconf -iv
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
%__chmod 755 %{buildroot}/%{_bindir}/%{name}

%if 0%{?fedora} >= 9
%post
setcap 'cap_sys_tty_config+ep' %{_bindir}/%{name}
%endif

%files 
%doc AUTHORS ChangeLog COPYING README
%if 0%{?fedora} >= 9
%{_bindir}/%{name}
%else
%attr(4755,root,root) %{_bindir}/%{name}
%endif
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
