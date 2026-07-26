%global source0_hash 0d23c54ec3b1cf4d34cb93ccec7590704667ab1beb80dcf1b209a4d522d5995f

%if 0%{?fedora}
%global editor  xterm -e sensible-editor
%global pkgs    sensible-utils xterm
%else
%global editor  emacs
%global pkgs    emacs
%endif

Name:           grace
Version:        5.1.25
Release:        46%{?dist}
Summary:        Numerical Data Processing and Visualization Tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
# cephes is LGPL, see also Source3 and Source4
URL:            http://plasma-gate.weizmann.ac.il/Grace/
Source0:        ftp://plasma-gate.weizmann.ac.il/pub/grace/src/grace5/grace-%{version}.tar.gz
Source1:        grace.desktop
Source3:        cephes-license.email
Source4:        LICENSE.cephes
Source5:        http://ftp.de.debian.org/debian/pool/main/g/grace/grace_5.1.25-6.debian.tar.xz
Source6:        FontDataBase
Patch0:         grace-detect-netcdf.diff
Patch1:         grace-configure-c99-1.patch
Patch2:         grace-configure-c99-2.patch
Patch3:         grace-c99.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fftw2-devel
BuildRequires:  gcc-gfortran
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  netcdf-devel
BuildRequires:  t1lib-devel
BuildRequires:  urw-base35-fonts-devel
BuildRequires:  xbae-devel
BuildRequires:  zlib-devel
Requires:       %{pkgs}
Requires:       urw-base35-fonts-common
Requires:       xdg-utils
%description
Grace is a Motif application for two-dimensional data
visualization. Grace can transform the data using free equations, FFT,
cross- and auto-correlation, differences, integrals, histograms, and
much more. The generated figures are of high quality.  Grace is a very
convenient tool for data inspection, data transformation, and for
making figures for publications.

%package        devel
Summary:        Files needed for grace development
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
Install these files if you need to compile software that requires grace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -D -a 5

# avoid duplicating debian patch
patch -p1 < debian/patches/binary_nostrip.diff
patch -p1 < debian/patches/gracerc.diff
patch -p1 < debian/patches/source-hardening.diff
patch -p1 < debian/patches/tmpnam_to_mkstemp.diff

# remove bundled libraries
rm -rf Xbae T1lib

%build
cp %{SOURCE3} %{SOURCE4} .
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export CFLAGS="$RPM_OPT_FLAGS -fPIC -std=gnu17"
%else
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%endif
export FFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure \
    --enable-editres \
    --with-editor="%{editor}" \
    --with-helpviewer="xdg-open %s" \
    --with-printcmd="lpr" \
    --enable-grace-home=%{_datadir}/%{name} \
    --disable-pdfdrv \
    --with-x \
    --with-f77=gfortran \
    --with-extra-incpath=%{_includedir}/netcdf \
    --with-bundled-xbae=no

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f doc/*.1
mkdir -pm 755                               \
    %{buildroot}%{_bindir}                  \
    %{buildroot}%{_includedir}              \
    %{buildroot}%{_libdir}                  \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps \
    %{buildroot}%{_datadir}/applications    \
    %{buildroot}%{_mandir}/man1             \
    %{buildroot}%{_sysconfdir}/%{name}

# Let's have some sanity
pushd %{buildroot}%{_datadir}/%{name}

install -pm 755 bin/* %{buildroot}%{_bindir}
rm %{buildroot}%{_bindir}/gracebat
ln -s xmgrace %{buildroot}%{_bindir}/gracebat
rm -rf bin
ln -s ../../bin bin

cp -p lib/* %{buildroot}%{_libdir}
rm -rf lib
ln -s ../../%_lib lib

install -pm 644 include/* %{buildroot}%{_includedir}
rm -rf include
ln -s ../../include include

# use fonts from urw-base53-legacy and install custom fontdb,
# see bz#1502175
rm -rf fonts/type1
ln -s %{urw_base35_fontpath} fonts/type1
rm fonts/FontDataBase
install -pm 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/%{name}/FontDataBase
ln -s ../../../..%{_sysconfdir}/%{name}/FontDataBase fonts/FontDataBase

# additional symlinks is also required
install -d -m0755 %{buildroot}/%{urw_base35_fontpath}
pushd %{buildroot}/%{urw_base35_fontpath}
for f in %{urw_base35_fontpath}/*.t1 ; do
    ln -s $(basename $f) $(basename $f .t1).pfb
done
popd

install -pm 644 doc/*.1 %{buildroot}%{_mandir}/man1/

# doc and example directories are removed from GRACE_HOME and put in %%doc
rm -rf doc examples
ln -s %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/{doc,examples} .

# the convcal source file shouldn't be installed, it is removed here
rm -f auxiliary/convcal.c

# remove grconvert if built
rm -f %{buildroot}%{_bindir}/grconvert

# move config files to %%{_sysconfdir} and do symlinks
for conf in gracerc templates gracerc.user; do
    mv $conf %{buildroot}%{_sysconfdir}/%{name}
    ln -s ../../..%{_sysconfdir}/%{name}/$conf $conf
done
popd

# Desktop stuff
install -pm 644 debian/icons/grace.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
for sz in 16 22 24 32; do
    install -Dpm 644 debian/icons/grace${sz}.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/grace.png
done
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications          \
    %{SOURCE1}

# clean up docs
rm -rf __dist_doc
mkdir __dist_doc
cp -a doc __dist_doc
rm __dist_doc/doc/Makefile __dist_doc/doc/*.sgml

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ChangeLog CHANGES COPYRIGHT DEVELOPERS README
%doc cephes-license.email LICENSE.cephes
%doc examples/ __dist_doc/doc/
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/convcal
%{_bindir}/fdf2fit
%{_bindir}/gracebat
%{_bindir}/xmgrace
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/include
%exclude %{_datadir}/%{name}/lib
%{_datadir}/applications/grace.desktop
%{_datadir}/icons/hicolor/*/apps/grace.png
%{_mandir}/man1/*.1*
%{urw_base35_fontpath}/*.pfb

%files devel
%license grace_np/LICENSE
%{_includedir}/grace_np.h
%{_datadir}/%{name}/include
%{_libdir}/libgrace_np.a
%{_datadir}/%{name}/lib

%changelog
%autochangelog
