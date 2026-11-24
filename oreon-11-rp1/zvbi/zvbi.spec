# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 817a26118e2654155ee761cd39414885986a4315fdb6617af5314090ddfffd10
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define             fontdir %{_datadir}/fonts/%{name}
%define             catalogue %{_sysconfdir}/X11/fontpath.d

Name:               zvbi
Version:            0.2.46
Release:            1%{?dist}
Summary:            Raw VBI, Teletext and Closed Caption decoding library
License:            GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND MIT
URL:                https://github.com/zapping-vbi/zvbi
Source0:            https://github.com/zapping-vbi/zvbi/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:             %{name}-0.2.24-tvfonts.patch
Patch1:             %{name}-0.2.25-openfix.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      bdftopcf
BuildRequires:      doxygen
BuildRequires:      fontconfig
BuildRequires:      gettext-devel
BuildRequires:      libICE-devel
BuildRequires:      libpng-devel
BuildRequires:      libtool
BuildRequires:      make
BuildRequires:      mkfontdir
BuildRequires:      systemd-units
BuildRequires:      tzdata

%description
ZVBI provides functions to capture and decode VBI data. The vertical blanking
interval (VBI) is an interval in a television signal that temporarily suspends
transmission of the signal for the electron gun to move back up to the first
line of the television screen to trace the next screen field. The vertical
blanking interval can be used to carry data, since anything sent during the VBI
would naturally not be displayed; various test signals, closed captioning, and
other digital data can be sent during this time period.

%package devel
Summary:            Development files for zvbi
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for zvbi

%package fonts
Summary:            Fonts from zvbi converted to X11
BuildArch:          noarch
Obsoletes:          xawtv-tv-fonts < 3.95
Provides:           xawtv-tv-fonts >= 3.95

%description fonts
Fonts from zvbi converted for use with X11

%prep
%oreon_sha256
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

cat >zvbid.service <<EOF
[Unit]
Description=Proxy Sharing V4L VBI Device Between Applications
After=syslog.target

[Service]
Type=forking
ExecStart=%{_sbindir}/zvbid

[Install]
WantedBy=multi-user.target

EOF

%build
./autogen.sh
%configure --disable-rpath --enable-v4l --enable-dvb --enable-proxy

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

pushd contrib
./x11font
for font in *.bdf
do
    bdftopcf $font | gzip -9 -c > ${font%.bdf}.pcf.gz
done
mkfontdir -x .bdf .
cat >fonts.alias <<EOF
teletext   -ets-teletext-medium-r-normal--*-200-75-75-c-120-iso10646-1
EOF
popd

%install
mkdir -p %{buildroot}%{fontdir}
%make_install

%find_lang %{name}

mkdir -p %{buildroot}%{_unitdir}
install -m644 zvbid.service %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_initrddir}

install -pm0644 contrib/*.pcf.gz %{buildroot}%{fontdir}
install -pm0644 contrib/fonts.* %{buildroot}%{fontdir}
touch %{buildroot}%{fontdir}/fonts.cache-1

mkdir -p %{buildroot}%{catalogue}
ln -sf %{fontdir} %{buildroot}%{catalogue}/%{name}

find %{buildroot}%{_libdir} -name '*.a' -delete

%check
cd test
make check

%post
%systemd_post zvbid.service

%preun
%systemd_preun zvbid.service

%postun
%systemd_postun_with_restart zvbid.service

%files -f %{name}.lang
%license COPYING.md
%doc AUTHORS BUGS ChangeLog NEWS README.md TODO
%{_bindir}/%{name}*
%if ! (0%{?fedora} >= 42)
%{_sbindir}/zvbid
%endif
%{_unitdir}/zvbid.service
%{_libdir}/libzvbi.so.0*
%{_libdir}/libzvbi-chains.so.0*
%{_mandir}/man1/zvbi*1*

%files devel
%{_includedir}/libzvbi.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-0.2.pc

%files fonts
%dir %{_datadir}/fonts/%{name}
%{fontdir}/*.gz
%{fontdir}/fonts.dir
%{fontdir}/fonts.alias
%{catalogue}/%{name}
%ghost %{fontdir}/fonts.cache-1

%changelog
%autochangelog
