%global source0_hash 93ba6b55923f9f6a43722025ac0239ff17b5533d8dfa375cc4af3ba4beaed024
Name:		ebview
Version:	0.3.6.2
Release:        1%{?dist}
Summary:        EPWING CD-ROM dictionary viewer
License:	GPL-2.0-or-later
URL:		http://packages.qa.debian.org/e/ebview.html
Source0:        http://ftp.de.debian.org/debian/pool/main/e/ebview/ebview_%{version}.orig.tar.gz
Patch0:	ebview-0.3.6.2-format-security.patch
Patch1:	ebview-0.3.6.2-wrong-inline.patch
Source1:	%{name}.desktop
Patch101:	https://sources.debian.org/data/main/e/ebview/0.3.6.2-2/debian/patches/dont-use-pangox.patch
Patch102:	https://sources.debian.org/data/main/e/ebview/0.3.6.2-2/debian/patches/link-ebview.diff
Patch103:	ebview-0.3.6.2-c99.patch
Patch104:	ebview-0.3.6.2-c23.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  eb-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(pango)
# /oreon:deps
%description
EBView is a EPWING dictionary browser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .format
%patch -P1 -p1 -b .inline
%patch -P101 -p1 -b .pango
%patch -P102 -p1 -b .link
%patch -P103 -p1 -b .c99
%patch -P104 -p1 -b .c23

rm -f m4/glib-gettext.m4
autoreconf -i

# Fix up permission
find . -type f -exec %{__chmod} 0644 {} ';'
%{__chmod} 0755 \
	configure \
	install-sh \
	mkinstalldirs

# Defaults
%{__sed} -i.defaults \
	-e 's|gnome-moz-remote|xdg-open|' \
	-e 's|Kochi |Sazanami |' \
	src/preference.c

# encodings
iconv -f EUCJP -t UTF-8 README > README.tmp && \
	( touch -r README README.tmp ; %{__mv} -f README.tmp README )

%{__sed} -i -e 's|\r||' \
	doc/ja/menu.html \
	doc/ja/body.html

for f in doc/ja/*.html ; do
	iconv -f EUC-JP -t UTF-8 $f | \
		%{__sed} -e 's|EUC-JP|UTF-8|' > $f.tmp && \
		%{__mv} -f $f.tmp $f || \
		%{__rm} -f $f.tmp
done
iconv -f ISO-8859-1 -t UTF-8 doc/en/index.html > doc/en/index.html.tmp && \
	%{__mv} -f doc/en/index.html.tmp doc/en/index.html || \
	%{__rm} -f doc/en/index.html.tmp

# Clearly mark this as unused
rm -f intl/*.{c,h}

%build

%configure \
	--with-eb-conf=%{_libdir}/eb.conf
%make_build -k
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="%{__install} -c -p" \
	bindir=$RPM_BUILD_ROOT%{_bindir}  \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%{__install} -cpm 644 pixmaps/%{name}.xpm \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps/
%{find_lang} %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
