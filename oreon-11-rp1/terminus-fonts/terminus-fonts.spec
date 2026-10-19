%global source0_hash d961c1b781627bf417f9b340693d64fc219e0113ad3a3af1a3424c7aa373ef79
Version: 4.49.1
Release:        6%{?dist}
URL:     http://terminus-font.sourceforge.net/
%global foundry           %{nil}
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.TXT
%global fontlicensesex    %{nil}
%global fontdocs          README README-BG docs/README.fedora
%global fontdocsex        %{fontlicenses}
%global fontfamily        terminus
%global fontsummary       Clean fixed width font
%global fontpkgheader     %{expand:
}
%global fonts             ter-*.otb
%global fontsex           %{nil}
%global fontconfs         %{SOURCE10}
%global fontconfsex       %{nil}
%global fontappstreams    %{nil}
%global fontappstreamsex  %{nil}
%global fontdescription   %{expand:
The Terminus Font is a clean, fixed with bitmap font designed for long\
(8 and more hours per day) work with computers.\
\
I contains more than 1300 characters, covers about 120 language sets and\
supports ISO8859-1/2/5/7/9/13/15/16, Paratype-PT154/PT254, KOI8-R/U/E/F,\
Esperanto, and many IBM, Windows and Macintosh code pages, as well as\
the IBM VGA, vt100 and xterm pseudo graphic characters.\
\
The sizes present are 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,\
14x28, and 16x32. The weights are normal and bold (except for 6x12),\
plus CRT VGA-bold for 8x14 and 8x16.
}
%global archivename terminus-font-%{version}
%global kbddir %{_exec_prefix}/lib/kbd
%global console_fontdir %{kbddir}/consolefonts
%global grub2_exclude_arches s390 s390x %{arm}
%global grub2_fontdir   /usr/share/grub
%global legacy_x11_fontdir   /usr/share/fonts/terminus-fonts-legacy-x11
%global catalog %{_sysconfdir}/X11/fontpath.d
%if %{?epoch: 1}%{?!epoch: 0}
%global evr %{epoch}:%{version}-%{release}
%else
%global evr %{version}-%{release}
%endif
Source0:        https://downloads.sourceforge.net/%{fontfamily}-font/%{archivename}.tar.gz
Source10: 63-%{fontpkgname}.conf
Source21:      %{name}-console-README.fedora
Source22:      %{name}-legacy-x11-README.fedora
Source23:      %{name}-Xresources.example
Source24:      %{name}-README.fedora
Source42:      bitmapfonts2otb.py
ExcludeArch:   %{grub2_exclude_arches}
%fontpkg
# oreon:deps
BuildRequires:  /usr/bin/bdftopcf
BuildRequires:  /usr/bin/ftdump
BuildRequires:  /usr/bin/grub2-mkfont
BuildRequires:  fonts-rpm-macros
BuildRequires:  make
BuildRequires:  mkfontdir
BuildRequires:  python3
# /oreon:deps
%package console
Requires:   kbd
Requires:   kbd-misc
Summary:    Clean fixed width font (console version)
License:    OFL-1.1
%description console
%fontdescription
This package contains the fonts to use with the Linux console.

%ifnarch %{grub2_exclude_arches}
%package grub2
Requires:   grub2-common
Summary:    Clean fixed width font (grub2 version)
License:    OFL-1.1
%description grub2
%fontdescription
This package contains the fonts to use with the grub2 boot loader.
%endif

%package legacy-x11
Summary:    Clean fixed width font (legacy PCF version)
License:    OFL-1.1
Requires:   %{name} = %{evr}
%description legacy-x11
%fontdescription
This package contains the font variants to use with software still
relying on legacy PCF font rendering methods (e.g. GNU Emacs 26).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
# Convert upstream files to UTF-8 and Unix end of lines if necessary
# Optional arguments:
# -e [encoding] source OS encoding (auto-detected otherwise)
# -n            do not recode files, only adjust folding and end of lines
#linuxtext *.txt
cp -p "%{SOURCE42}" bin/
patch -s -p1 -b --suffix .br1 -fuzz=0 -i alt/br1.diff
patch -s -p1 -b --suffix .dv1 -fuzz=0 -i alt/dv1.diff
patch -s -p1 -b --suffix .ij1 -fuzz=0 -i alt/ij1.diff
patch -s -p1 -b --suffix .td1 -fuzz=0 -i alt/td1.diff
iconv -f WINDOWS-1251 -t utf-8 -o README-BG README-BG

%build

./configure --prefix=%{_prefix} \
            --x11dir=%{legacy_x11_fontdir} --psfdir=%{console_fontdir}
env GZIP=--best make %{?_smp_mflags} PCF='$(PCF_10646_1) $(PCF_8BIT)' pcf psf psf-vgaw otb
ls -l *.otb
%ifnarch %{grub2_exclude_arches}
for bdf in ter-*[bn].bdf; do
  /usr/bin/grub2-mkfont -o "$(basename "$bdf" .bdf).pf2" "$bdf"
done
%endif
mkdir -p docs/console docs/legacy-x11
cp -p "%{SOURCE21}" docs/console/README.fedora
cp -p "%{SOURCE22}" docs/legacy-x11/README.fedora
cp -p "%{SOURCE23}" docs/legacy-x11/Xresources.example
cp -p "%{SOURCE24}" docs/README.fedora
%fontbuild
%install
make DESTDIR="%{buildroot}" PCF='$(PCF_10646_1) $(PCF_8BIT)' install-psf install-psf-ref install-psf-vgaw install-pcf
%ifnarch %{grub2_exclude_arches}
install -m 0755 -d %{buildroot}%{grub2_fontdir}
install -m 0644 -t %{buildroot}%{grub2_fontdir} ter-*.pf2
%endif
install -m 0755 -d %{buildroot}%{catalog}
ln -s "$(echo '%{catalog}/%{fontfamily}:unscaled' | sed -e 's|[^/]||g' -e 's|/|../|g' -e 's|/../$||')%{legacy_x11_fontdir}" "%{buildroot}%{catalog}/%{fontfamily}:unscaled"
test -d "%{buildroot}%{catalog}/%{fontfamily}:unscaled/"
mkfontdir %{buildroot}%{legacy_x11_fontdir}
test -f "%{buildroot}%{catalog}/%{fontfamily}:unscaled/fonts.dir"
font_counter=0
for fntfile in %{fonts}
do
    if test -f "${fntfile}"; then
       font_counter="$(expr "${font_counter}" + 1)"
    else
       echo "Missing font file or wildcard: ${fntfile}"
       exit 2
    fi
done
if test "$font_counter" -lt 18 || test "$font_counter" -gt 18
then
    echo "Weird number of font files: $font_counter"
    exit 2
fi
%fontinstall
cat<<EOF
/=======================================================================
| _arch                %{_arch}
| _build_arch          %{_build_arch}
| grub2_exclude_arches %{grub2_exclude_arches}
\=======================================================================
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list
%files -n adf-gillius-fonts-console -f %{oreon_filedir}/adf-gillius-fonts-console.list
%files -n adf-gillius-fonts-grub2 -f %{oreon_filedir}/adf-gillius-fonts-grub2.list
%files -n adf-gillius-fonts-legacy-x11 -f %{oreon_filedir}/adf-gillius-fonts-legacy-x11.list

%changelog

%autochangelog
