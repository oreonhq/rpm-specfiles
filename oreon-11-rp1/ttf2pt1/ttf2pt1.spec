%global source0_hash ae926288be910073883b5c8a3b8fc168fde52b91199fdf13e92d72328945e1d0
Name: ttf2pt1
Version: 3.4.4
Release:        1%{?dist}
Summary:        TrueType to Adobe Type 1 font converter
Summary(sv): Konverterare från TrueType till Adobe Type 1
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD-with-advertising
URL: http://%name.sourceforge.net
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0: ttf2pt1-destdir.patch
Patch1: ttf2pt1-freetype.patch
Patch2: ttf2pt1-sed.patch
Patch3: ttf2pt1-doc.patch
Patch4: ttf2pt1-c99.patch
Patch5: ttf2pt1-gcc14.patch
Requires: t1utils
# oreon:deps
BuildRequires:  fakeroot
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  t1lib-devel
# /oreon:deps
%description
Ttf2pt1 is a font converter from the True Type format (and some other formats
supported by the FreeType library as well) to the Adobe Type1 format.

%description -l sv
Ttf2pt1 är en konverterare för typsnitt från formatet True Type (och
några andra format som stödjs av biblioteket FreeType) till formatet
Adobe Type 1.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make CFLAGS_SYS='%optflags -D_GNU_SOURCE' CFLAGS_FT="-DUSE_FREETYPE `pkg-config --cflags freetype2`" LIBS_FT="`pkg-config --libs freetype2`" VERSION=%version all
rm -rf __dist_other
mkdir -p __dist_other/other
cp -p other/bz* other/Makefile other/README* __dist_other/other
make -C other cmpf dmpf
%install
fakeroot make DESTDIR=%buildroot INSTDIR=%_prefix TXTFILES= MANDIR=%_mandir VERSION=%version install
rm -r %buildroot/%_libexecdir
rm %buildroot%_datadir/%name/scripts/{convert,convert.cfg.sample,frommap,html2man,inst_dir,inst_file,mkrel,unhtml}
mv %buildroot/%_datadir/%name/other/cmpf %buildroot/%_bindir/%{name}_cmpf
mv %buildroot/%_datadir/%name/other/dmpf %buildroot/%_bindir/%{name}_dmpf
cp other/cntstems.pl %buildroot/%_bindir/%{name}_cntstems
cp other/lst.pl %buildroot/%_bindir/%{name}_lst
cp other/showdf %buildroot/%_bindir/%{name}_showdf
cp other/showg %buildroot/%_bindir/%{name}_showg
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
