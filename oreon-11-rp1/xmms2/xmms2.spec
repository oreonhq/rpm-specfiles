%global source0_hash 51a88d55da360120dd266b590b5c923adf49f031b7b1101515db70dbba27bf2b

Name:			xmms2
Summary: 		A modular audio framework and plugin architecture
Version:		0.9.5
Release:		9%{?dist}
License:		LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
# We can't use the upstream source tarball as-is, because it includes an mp4 decoder.
# Also, the ogg sample included is not under a FOSS license.
# https://github.com/xmms2/xmms2-devel/releases/download/%%{version}/xmms2-%%{version}.tar.xz
# Cleaning it is simple, just rm -rf src/plugins/mp4 mind.in.a.box-lament_snipplet.ogg
Source0:		%{name}-%{version}-clean.tar.xz
Source1:		xmms2-client-launcher.sh
# CC-BY
# taken from http://ccmixter.org/files/unreal_dm/38156
Source2:		unreal_dm-free.music.and.free.beer.ogg
# Apply c++ client fix from gentoo
Patch2:			xmms2-0.9.3-gentoo-cpp-client.patch
# Apply fix to faad plugin from gentoo
Patch3:			xmms2-0.9.3-gentoo-faad.patch
# Apply fix for curl buffer overrun
Patch4:			xmms2-0.9.3-curl-buffer-overrun-fix.patch
# Swap mind.in.a.box for free.music.and.free.beer
Patch11:		xmms2-0.9.3-no-mind-in-a-box.patch
URL:			http://wiki.xmms2.xmms.se/
BuildRequires:		git
BuildRequires:		python3-devel
BuildRequires:		python3-cython
BuildRequires:		python-unversioned-command
BuildRequires:		sqlite-devel
BuildRequires:		flac-devel
BuildRequires:		libofa-devel
BuildRequires:		libcdio-paranoia-devel
BuildRequires:		libdiscid-devel
BuildRequires:		libsmbclient-devel
BuildRequires:		libmpcdec-devel
BuildRequires:		gnome-vfs2-devel
BuildRequires:		pkgconfig(jack)
BuildRequires:		fftw-devel
BuildRequires:		libsamplerate-devel
BuildRequires:		libxml2-devel
BuildRequires:		alsa-lib-devel
BuildRequires:		libao-devel
BuildRequires:		libshout-devel
BuildRequires:		ruby-devel
BuildRequires:		ruby
BuildRequires:		ruby(rubygems)
BuildRequires:		perl-devel
BuildRequires:		perl-generators
BuildRequires:		boost-devel
BuildRequires:		pulseaudio-libs-devel
BuildRequires:		libmodplug-devel
BuildRequires:		ecore-devel
BuildRequires:		mpg123-devel
BuildRequires:		libmad-devel
BuildRequires:		doxygen
BuildRequires:		perl-Pod-Parser
BuildRequires:		pkgconfig(avahi-client)
BuildRequires:		pkgconfig(avahi-glib)
BuildRequires:		pkgconfig(avahi-compat-libdns_sd)
BuildRequires:		libvisual-devel
BuildRequires:		wavpack-devel
BuildRequires:		SDL-devel
BuildRequires:		glib2-devel
BuildRequires:		readline-devel
BuildRequires:		ncurses-devel
BuildRequires:		mac-devel
BuildRequires:		fluidsynth-devel
BuildRequires:		opusfile-devel
BuildRequires:		libmms-devel
BuildRequires:		libcurl-devel
BuildRequires:		flex
BuildRequires:		bison
# For /usr/share/perl5/ExtUtils/xsubpp
BuildRequires:		perl-ExtUtils-ParseXS
BuildRequires:		gcc
BuildRequires:		gcc-c++
BuildRequires:		waf
BuildRequires:		openssl-devel-engine, openssl-devel

Obsoletes:		xmms2-mad < 0.8-26
Provides:		xmms2-mad = %{version}-%{release}

Obsoletes:		xmms2-mac < 0.8-24
Provides:		xmms2-mac = %{version}-%{release}

Obsoletes:		xmms2-mms < 0.8-39
Provides:		xmms2-mms = %{version}-%{release}

Obsoletes:		xmms2-nyxmms2 < 0.8-89
Provides:		xmms2-nyxmms2 = %{version}-%{release}

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

# make the docs
doxygen

%install
export LIBDIR="%{_libdir}"
./waf install --destdir=%{buildroot} --prefix=%{_prefix} --libdir=%{_libdir} --with-ruby-libdir=%{ruby_vendorlibdir} --with-ruby-archdir=%{ruby_vendorarchdir} \
  --with-perl-archdir=%{perl_archlib} --with-pkgconfigdir=%{_libdir}/pkgconfig

# exec flags for debuginfo
chmod +x %{buildroot}%{_libdir}/%{name}/* %{buildroot}%{_libdir}/libxmmsclient*.so* \
	%{buildroot}%{perl_archlib}/auto/Audio/XMMSClient/XMMSClient.so %{buildroot}%{ruby_vendorarchdir}/xmmsclient_*.so

# Convert to utf-8
for i in %{buildroot}%{_mandir}/man1/*.gz; do
	gunzip $i;
done
for i in %{buildroot}%{_mandir}/man1/*.1 xmms2-%{version}.ChangeLog; do
	iconv -o $i.iso88591 -f iso88591 -t utf8 $i
	mv $i.iso88591 $i
done

install -m0755 %{SOURCE1} %{buildroot}%{_bindir}

%ldconfig_scriptlets

%files
%license COPYING COPYING.GPL COPYING.LGPL
%doc AUTHORS xmms2-%{version}.ChangeLog README.mdown
%{_bindir}/%{name}*
%{_bindir}/_xmms2-migrate-collections-v0
%{_bindir}/s4
%{_bindir}/sqlite2s4
%{_libdir}/libxmmsclient*.so.*
%{_libdir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libxmmsclient*.so
%{_libdir}/pkgconfig/%{name}-*.pc

%files docs
%doc doc/xmms2/html

%files perl
%{perl_archlib}/Audio/
%{perl_archlib}/auto/Audio/

%files python3
%{python3_sitearch}/xmmsclient/

%files ruby
%{ruby_vendorlibdir}/xmmsclient.rb
%{ruby_vendorlibdir}/xmmsclient/
%{ruby_vendorarchdir}/xmmsclient_ecore.so
%{ruby_vendorarchdir}/xmmsclient_ext.so
%{ruby_vendorarchdir}/xmmsclient_glib.so

%changelog
%autochangelog
