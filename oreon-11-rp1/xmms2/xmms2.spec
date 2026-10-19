%global source0_hash 51a88d55da360120dd266b590b5c923adf49f031b7b1101515db70dbba27bf2b
Name:			xmms2
Summary:        A modular audio framework and plugin architecture
Version:		0.9.5
Release:        9%{?dist}
License:		LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
Source0:        %{name}-%{version}-clean.tar.xz
Source1:		xmms2-client-launcher.sh
Source2:		unreal_dm-free.music.and.free.beer.ogg
Patch2:			xmms2-0.9.3-gentoo-cpp-client.patch
Patch3:			xmms2-0.9.3-gentoo-faad.patch
Patch4:			xmms2-0.9.3-curl-buffer-overrun-fix.patch
Patch11:		xmms2-0.9.3-no-mind-in-a-box.patch
URL:			http://wiki.xmms2.xmms.se/
Obsoletes:		xmms2-mad < 0.8-26
Provides:		xmms2-mad = %{version}-%{release}
Obsoletes:		xmms2-mac < 0.8-24
Provides:		xmms2-mac = %{version}-%{release}
Obsoletes:		xmms2-mms < 0.8-39
Provides:		xmms2-mms = %{version}-%{release}
Obsoletes:		xmms2-nyxmms2 < 0.8-89
Provides:		xmms2-nyxmms2 = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  ecore-devel
BuildRequires:  fftw-devel
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  libao-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdiscid-devel
BuildRequires:  libmad-devel
BuildRequires:  libmms-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libofa-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libshout-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libvisual-devel
BuildRequires:  libxml2-devel
BuildRequires:  mac-devel
BuildRequires:  mpg123-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  opusfile-devel
BuildRequires:  perl-ExtUtils-ParseXS
BuildRequires:  perl-Pod-Parser
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python-unversioned-command
BuildRequires:  python3-cython
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  ruby
BuildRequires:  ruby(rubygems)
BuildRequires:  ruby-devel
BuildRequires:  sqlite-devel
BuildRequires:  waf
BuildRequires:  wavpack-devel
# /oreon:deps
%description
XMMS2 is an audio framework, but it is not a general multimedia player - it 
will not play videos. It has a modular framework and plugin architecture for 
audio processing, visualisation and output, but this framework has not been 
designed to support video. Also the client-server design of XMMS2 (and the 
daemon being independent of any graphics output) practically prevents direct 
video output being implemented. It has support for a wide range of audio 
formats, which is expandable via plugins. It includes a basic CLI interface 
to the XMMS2 framework, but most users will want to install a graphical XMMS2 
client (such as gxmms2 or esperanza).

%package devel
Summary:	Development libraries and headers for XMMS2
Requires:	glib2-devel, boost-devel
Requires:	pkgconfig
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries and headers for XMMS2. You probably need this to develop
or build new plugins for XMMS2.

%package docs
Summary:	Development documentation for XMMS2
Requires:	%{name} = %{version}-%{release}
%description docs
API documentation for the XMMS2 modular audio framework architecture.

%package perl
Summary:	Perl support for XMMS2
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:	%{name} = %{version}-%{release}
%description perl
Perl bindings for XMMS2.

%package python3
Summary:	Python3 support for XMMS2
Requires:	%{name} = %{version}-%{release}
%description python3
Python3 bindings for XMMS2.

%package ruby
Summary:	Ruby support for XMMS2
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(release)
%description ruby
Ruby bindings for XMMS2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P2 -p1 -b .cpp-client
%patch -P3 -p1 -b .faad
%patch -P4 -p1 -b .overrun
%patch -P11 -p1 -b .nomind
cp %{SOURCE2} .

# This header doesn't need to be executable
chmod -x src/include/xmmsclient/xmmsclient++/dict.h

%build

export CFLAGS="%{optflags} -DHAVE_G_FILE_QUERY_FILE_TYPE"
export CPPFLAGS="%{optflags}"
export LIBDIR="%{_libdir}"
export XSUBPP="%{_bindir}/xsubpp"
./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --with-ruby-libdir=%{ruby_vendorlibdir} --with-ruby-archdir=%{ruby_vendorarchdir} \
--with-perl-archdir=%{perl_archlib} --with-pkgconfigdir=%{_libdir}/pkgconfig -j1
./waf build -v %{?_smp_mflags}
doxygen
%install
export LIBDIR="%{_libdir}"
./waf install --destdir=%{buildroot} --prefix=%{_prefix} --libdir=%{_libdir} --with-ruby-libdir=%{ruby_vendorlibdir} --with-ruby-archdir=%{ruby_vendorarchdir} \
  --with-perl-archdir=%{perl_archlib} --with-pkgconfigdir=%{_libdir}/pkgconfig
chmod +x %{buildroot}%{_libdir}/%{name}/* %{buildroot}%{_libdir}/libxmmsclient*.so* \
	%{buildroot}%{perl_archlib}/auto/Audio/XMMSClient/XMMSClient.so %{buildroot}%{ruby_vendorarchdir}/xmmsclient_*.so
for i in %{buildroot}%{_mandir}/man1/*.gz; do
	gunzip $i;
done
for i in %{buildroot}%{_mandir}/man1/*.1 xmms2-%{version}.ChangeLog; do
	iconv -o $i.iso88591 -f iso88591 -t utf8 $i
	mv $i.iso88591 $i
done
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xmms2-devel -f %{oreon_filedir}/xmms2-devel.list
%files -n xmms2-docs -f %{oreon_filedir}/xmms2-docs.list
%files -n xmms2-perl -f %{oreon_filedir}/xmms2-perl.list
%files -n xmms2-python3 -f %{oreon_filedir}/xmms2-python3.list
%files -n xmms2-ruby -f %{oreon_filedir}/xmms2-ruby.list

%changelog

%autochangelog
