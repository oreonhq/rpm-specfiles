%global source0_hash none

%define         name            efont-unicode-bdf
%define         fontdir         %{_datadir}/fonts/japanese/%{name}
%define         catalogdir      %{_sysconfdir}/X11/fontpath.d
%define         catalogname     %{name}

Name:           %{name}
Version:        0.4.2
Release:        42%{?dist}
Summary:        Unicode font by Electronic Font Open Laboratory

# Automatically converted from old format: BSD and Public Domain and Baekmuk and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain AND Baekmuk AND LicenseRef-Callaway-MIT
URL:            http://openlab.jp/efont/unicode/
Source0:        http://openlab.jp/efont/dist/unicode-bdf/efont-unicode-bdf-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  %{_bindir}/bdftopcf
BuildRequires:  %{_bindir}/mkfontdir
BuildRequires:  %{_bindir}/ttmkfdir
BuildRequires:  gzip

%description
This package provides Unicode bitmap fonts provided by
Electronic Font Open Laboratory.

%prep
%setup -q

# convert documents' encoding to UTF8.
# must be done in %%prep
for f in README.{naga10,shinonome} ; do
   mv ${f} ${f}.tmp
   iconv -f EUCJP -t UTF8 ${f}.tmp > ${f} && rm -f ${f}.tmp || \
      mv ${f}.tmp ${f}
done

%build
for f in *bdf ; do
  g=${f%bdf}pcf
  bdftopcf -o $g $f
  gzip -9 $g
done

%install
# 1. install actual fonts
mkdir -p $RPM_BUILD_ROOT%{fontdir}
for g in *pcf.gz ; do
  install -m 644 $g $RPM_BUILD_ROOT%{fontdir}
done

# 2-1. create fonts.scale and fonts.dir in advance
ttmkfdir -d $RPM_BUILD_ROOT%{fontdir} -o $RPM_BUILD_ROOT%{fontdir}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{fontdir}

# 2-2. create ghost files
touch $RPM_BUILD_ROOT%{fontdir}/encodings.dir
%if 0%{?fedora} < 29
touch $RPM_BUILD_ROOT%{fontdir}/fonts.cache-1
%endif

# 2.3 create libXfont catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogdir}
pushd $RPM_BUILD_ROOT%{catalogdir}
pushd ../../..
if [ x$(pwd) != x$RPM_BUILD_ROOT ] ; then
   echo "Current directory is not $RPM_BUILD_ROOT"
   exit 1
fi
popd
ln -sf ../../..%{fontdir} fonts-%{name}
popd

%files
%license COPYRIGHT
%doc README* ChangeLog List.html

%dir %{fontdir}
%{fontdir}/*pcf.gz
%verify(not md5 size mtime) %{fontdir}/fonts.scale
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%ghost %verify(not md5 size mtime) %{fontdir}/encodings.dir

%{catalogdir}/fonts-%{name}

%changelog
%autochangelog
