%global source0_hash 720f600817217257aa4c822e67814495dcb6c8d6326cdde5fe3ba1e457d9915d
%global udevdir %(pkg-config --variable=udevdir udev)
Name:       fbterm
Version:    1.8
Release:        1%{?dist}
License:    GPL-2.0-or-later
URL:        http://code.google.com/p/fbterm/
Source0:        https://github.com/fujiwarat/fbterm/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch5:     %{name}-1.7-u16-build.patch
Summary:        A frame-buffer terminal emulator
Summary(zh_CN): 运行在帧缓冲的快速终端仿真器
Summary(zh_TW): 運行在frame-buffer的快速終端模擬機
Requires: fontconfig
Requires: ncurses-term
Obsoletes: fbterm-udevrules < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  gpm-devel
BuildRequires:  make
BuildRequires:  pkgconfig(udev)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
