%global source0_hash bca620ab670328ad732d161e4ce8d9d9fc832533cb7440e98c50e112b805ac5e
%define fontdir %{_datadir}/fonts/%{name}
%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:           zvbi
Version:        0.2.44
Release:        %autorelease
Summary:        Raw VBI, Teletext and Closed Caption decoding library

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND MIT
URL:            https://github.com/zapping-vbi/zvbi
Source0:        https://github.com/zapping-vbi/zvbi/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         zvbi-0.2.24-tvfonts.patch
Patch1:         zvbi-0.2.25-openfix.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bdftopcf
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libICE-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mkfontdir
BuildRequires:  systemd-units
BuildRequires:  tzdata

%description
ZVBI provides functions to capture and decode VBI data.

%package devel
Summary:        Development files for zvbi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for zvbi.

%package fonts
Summary:        Fonts from zvbi converted to X11
BuildArch:      noarch

%description fonts
Fonts from zvbi converted for use with X11.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
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
for font in *.bdf; do
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
%{_sbindir}/zvbid
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
