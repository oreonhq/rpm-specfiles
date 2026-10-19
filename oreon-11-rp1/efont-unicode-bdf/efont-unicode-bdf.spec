%global source0_hash 7d3ed2b18955ddd090adfd0865f88d23582b8f79e00e0afc22459d83e7fd9b73
%define         name            efont-unicode-bdf
%define         fontdir         %{_datadir}/fonts/japanese/%{name}
%define         catalogdir      %{_sysconfdir}/X11/fontpath.d
%define         catalogname     %{name}
Name:           %{name}
Version:        0.4.2
Release:        1%{?dist}
Summary:        Unicode font by Electronic Font Open Laboratory
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain AND Baekmuk AND LicenseRef-Callaway-MIT
URL:            http://openlab.jp/efont/unicode/
Source0:        http://openlab.jp/efont/dist/unicode-bdf/efont-unicode-bdf-%{version}.tar.bz2
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/bdftopcf
BuildRequires:  /usr/bin/mkfontdir
BuildRequires:  /usr/bin/ttmkfdir
BuildRequires:  gzip
# /oreon:deps
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
mkdir -p $RPM_BUILD_ROOT%{fontdir}
for g in *pcf.gz ; do
  install -m 644 $g $RPM_BUILD_ROOT%{fontdir}
done
ttmkfdir -d $RPM_BUILD_ROOT%{fontdir} -o $RPM_BUILD_ROOT%{fontdir}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{fontdir}
touch $RPM_BUILD_ROOT%{fontdir}/encodings.dir
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
