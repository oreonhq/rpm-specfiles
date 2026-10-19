%global source0_hash fde97c82b9d1a69244f714b531b17eca2ccbb4ddb7e9d5d979e669f2c4341027
%bcond_with modular_x
%bcond_with modular_xss
%global xssconfigdir %{_datadir}/xscreensaver/config
%global xssexthacksconfdir %{_datadir}/xscreensaver/hacks.conf.d
%global xssbindir %{_libexecdir}/xscreensaver
%bcond_with matrixview
%global patchext %{nil}%{!?with_matrixview:.p}
Summary:        Really Slick Screensavers
Name: rss-glx
Version: 0.9.1%{patchext}
Release:        65%{?dist}
License: GPL-2.0-only
URL: http://rss-glx.sourceforge.net/
Source0:        rss-glx_%{version}.tar.bz2
Source1: README.fedora
Source2: rss-glx-rm-matrixview.sh
Source3: rss-glx-0.9.1-0.9.1.p.diff
Source4: rss-glx-matrixview.conf
Source5: rss-glx.conf
Patch0: rss-glx-0.9.0.p-optflags.patch
Patch10: rss-glx-0.9.1.p-6-autoreconf.patch.bz2
Patch11: rss-glx-0.9.1.p-linker.patch
Patch12: rss-glx-0.9.1.p-pixelcity.patch
Patch13: rss-glx-gcc11.patch
Patch14: rss-glx-ImageMagick7.patch
Patch15: rss-glx-ImageMagick7-configure.patch
%if %{with modular_x}
%else
%endif
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  bzip2-devel
BuildRequires:  freealut-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  make
BuildRequires:  quesoglc-devel
BuildRequires:  sed
BuildRequires:  xorg-x11-devel
# /oreon:deps
%description
A port of the Really Slick Screensavers to GLX. Provides several visually
impressive and graphically intensive screensavers.

Note that this package contains only the display hacks themselves; you will
need to install the appropriate subpackage for your desktop environment in
order to use them as screensavers.

%package xscreensaver
Summary: Really Slick Screensavers
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with modular_xss}
Requires(post): xscreensaver-base >= 1:5.03-3
Requires(postun): xscreensaver-base >= 1:5.03-3
%else
Requires: xscreensaver-base < 1:5.03-3
%endif
Requires: xscreensaver-gl-base
%description xscreensaver
A port of the Really Slick Screensavers to GLX. Provides several visually
impressive and graphically intensive screensavers.

This package contains files needed to use the hacks with xscreensaver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

cat << EOF

Build settings:
%if %{with modular_x}
- with modular X
%else
- with monolithic X
%endif
%if %{with matrixview}
- with matrixview hack
%else
- without matrixview hack
%endif
%if %{with modular_xss}
- with modular xscreensaver support
%else
- without modular xscreensaver support
%endif
EOF

%autosetup -p1 -n rss-glx_%{version}

%build

%configure \
    --with-configdir=%{xssconfigdir} \
    --program-prefix=rss-glx-
%make_build
%install
install -m 0644 "%SOURCE1" "%SOURCE2" "%SOURCE3" .
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/lib*.{,l}a
rm %{buildroot}%{_bindir}/rss-glx-rss-glx_install.pl
mkdir -p %{buildroot}%{xssbindir}
mkdir -p %{buildroot}%{xssexthacksconfdir}
%if %{with matrixview}
install -m 0644 "%SOURCE4" %{buildroot}%{xssexthacksconfdir}/rss-glx.conf
%else
install -m 0644 "%SOURCE5" %{buildroot}%{xssexthacksconfdir}/rss-glx.conf
%endif
cd %buildroot/%{_bindir}/
for file in rss-glx*; do
    ln -snf "%{_bindir}/${file}" "%{buildroot}%{xssbindir}/${file}"
done
cd %buildroot/%{xssconfigdir}/
for file in *.xml; do
    mv -f ${file} rss-glx-${file}
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with modular_xss}
%post xscreensaver

if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks
fi
%postun xscreensaver

if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks || :
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n rss-glx-xscreensaver -f %{oreon_filedir}/rss-glx-xscreensaver.list

%changelog

%autochangelog
