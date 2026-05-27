%global source0_hash 2890c3da2642cd44c5f3bfed2c9b2c1db83da5cec09cc17e0fa72e17541fb4b9

Summary: Tool for decoding raw image data from digital cameras
Name: dcraw
Version: 9.28.0
Release: 28%{?dist}
License: GPL-2.0-or-later
URL: http://www.dechifro.org/dcraw/
Source0: http://www.dechifro.org/dcraw/archive/dcraw-%{version}.tar.gz
Patch0: dcraw-9.21-lcms2-error-reporting.patch
Patch1: dcraw-CVE-2018-5801.patch
Patch2: dcraw-CVE-2017-13735.patch
Patch3: dcraw-CVE-2017-14608.patch
Patch4: dcraw-CVE-2018-19655.patch
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: libjpeg-devel
BuildRequires: lcms2-devel
BuildRequires: jasper-devel
Provides: bundled(dcraw)

%description
This package contains dcraw, a command line tool to decode raw image data
downloaded from digital cameras.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n dcraw

%build
%{__cc} %optflags $RPM_LD_FLAGS \
    -Wl,--no-as-needed \
    -lm -ljpeg -llcms2 -ljasper \
    -DLOCALEDIR="\"%{_datadir}/locale\"" \
    -o dcraw dcraw.c
# build language catalogs
for catsrc in dcraw_*.po; do
    lang="${catsrc%.po}"
    lang="${lang#dcraw_}"
    msgfmt -o "dcraw_${lang}.mo" "$catsrc"
done

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 dcraw %{buildroot}%{_bindir}

# install language catalogs
for catalog in dcraw_*.mo; do
    lang="${catalog%.mo}"
    lang="${lang#dcraw_}"
    install -d -m 0755 "%{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES"
    install -m 0644 "$catalog" "%{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/dcraw.mo"
done

install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -m 0644 dcraw.1 %{buildroot}%{_mandir}/man1/dcraw.1
# localized manpages
rm -f %{name}-man-files
touch %{name}-man-files
for manpage in dcraw_*.1; do
    lang="${manpage%.1}"
    lang="${lang#dcraw_}"
    install -d -m 0755 "%{buildroot}%{_mandir}/${lang}/man1"
    install -m 0644 "${manpage}" "%{buildroot}%{_mandir}/${lang}/man1/dcraw.1"
    echo "%%lang($lang) %%{_mandir}/${lang}/man1/*" >> %{name}-man-files
done

%find_lang %{name}

%files -f %{name}.lang -f %{name}-man-files
%{_bindir}/dcraw
%{_mandir}/man1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.28.0-28
- Prepare for Oreon 11 (RP1)
