%global source0_hash 8976437e333757a84f7762c0bbf2e381afc000d3c485a1e42bcd3d7cb4efc1d7

# Use ImageMagick for converting images other than EPS and XBM
%if 0%{?rhel}
%bcond_with html2ps_enables_ImageMagick
%else
%bcond_without html2ps_enables_ImageMagick
%endif
# Otherwise, handle JPEG images with djpeg
%bcond_without html2ps_enables_djpeg
# and with netpbm
%bcond_without html2ps_enables_netpbm

# Disable rendering MathML with TeX. The resulting PostScript cannot be
# interpreted with GhostScript, a dependency on TeX is large, and MathML is
# relatively rare. Without TeX, html2ps still renders MathML, only more
# imperfectly.
%bcond_with html2ps_enables_tex

%define my_subversion b7
Name:           html2ps
Version:        1.0
Release:        0.58.%{my_subversion}%{?dist}
Summary:        HTML to PostScript converter
# contrib/xhtml2ps/LICENSE:     GPL-2.0 text
# contrib/xhtml2ps/README:      "X-html2ps is GPL"
# contrib/xhtml2ps/xhtml2ps:    GPL-2.0-or-later
# COPYING:      GPL-2.0 text
# html2ps:      GPL-2.0-or-later
# html2ps.html: "html2ps and xhtml2ps is GPL, see COPYING"
License:        GPL-2.0-or-later
URL:            http://user.it.uu.se/~jan/%{name}.html
Source0:        http://user.it.uu.se/~jan/%{name}-1.0%{my_subversion}.tar.gz
Source1:        xhtml2ps.desktop
Patch0:         http://ftp.de.debian.org/debian/pool/main/h/%{name}/%{name}_1.0b5-5.diff.gz
# Use xdg-open in xhtml2ps
Patch1:         %{name}-1.0b5-xdg-open.patch
# Patch a config file from Debian to use dvips, avoid using weblint;
# Don't set letter as default page size, paper tool will set the default.
Patch2:         %{name}-1.0b5-config.patch
# Remove a deprecated variable, bug #822117
Patch3:         %{name}-1.0b7-Remove-deprecated-variable.patch
# Fix Perl 5.22 warnings, bug #1404275
Patch4:         html2ps-1.0b7-Fix-perl-5.22-warnings.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
# glibc-common for iconv
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
Requires:       ghostscript
# paperconf is obsolete, "paper" is the new utility.
Requires:       paper
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
%if %{with html2ps_enables_tex}
Requires:       tex(dvips)
Requires:       tex(tex)
%endif

# Remove ImageMagick dependency if the feature is disabled
%if %{without html2ps_enables_ImageMagick}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Image::Magick\\)
%if %{with html2ps_enables_djpeg}
# libjpeg-turbo-utils for djpeg
Requires:       libjpeg-turbo-utils
%endif
%if %{with html2ps_enables_netpbm}
Requires:       netpbm-progs
%endif
%endif

%description
An HTML to PostScript converter written in Perl.
* Many possibilities to control the appearance. 
* Support for processing multiple documents.
* A table of contents can be generated.
* Configurable page headers/footers.
* Automatic hyphenation and text justification can be selected. 

%package -n xhtml2ps
Summary:     GUI front-end for html2ps
Requires:    html2ps = %{version}-%{release}
Requires:    xdg-utils

%description -n xhtml2ps
X-html2ps is freely-available GUI front-end for html2ps, a HTML-to-PostScript
converter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-1.0%{my_subversion}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

# Convert to UTF-8
for F in README contrib/xhtml2ps/xhtml2ps; do
    iconv -f latin1 -t utf8 < "$F" > "$F".utf8
    touch -c -r "$F" "$F".utf8
    mv "$F".utf8 "$F"
done

patch -p1 < debian/patches/01_manpages.dpatch

# Change paperconf to paper in 03_html2ps.dpatch
sed -i \
%if 0%{?rhel} && 0%{?rhel} < 10
    's|paperconf|paper|g' \
%else
    's|paperconf|paper --no-size|g' \
%endif
     debian/patches/03_html2ps.dpatch

# 03_html2ps.dpatch is against 1.0b5, adjust it to 1.0b6
< debian/patches/03_html2ps.dpatch sed -e 's|/opt/misc/|/it/sw/share/www/|' | \
    patch -p1

%patch -P 4 -p1

%build
# Change default configuration
sed -i \
    -e 's/ImageMagick: [01]/ImageMagick: %{with html2ps_enables_ImageMagick}/' \
    -e 's/PerlMagick: [01]/PerlMagick: %{with html2ps_enables_ImageMagick}/' \
    debian/config/html2psrc
%if %{without html2ps_enables_ImageMagick}
sed -i \
    -e '/package {/ a \ \ \ \ djpeg: %{with html2ps_enables_djpeg};' \
    -e '/package {/ a \ \ \ \ netpbm: %{with html2ps_enables_netpbm};' \
    debian/config/html2psrc
%endif
sed -i \
    -E 's/(dvips|TeX): [01]/\1: %{with html2ps_enables_tex}/' \
    debian/config/html2psrc

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man{1,5}

sed -e 's;/etc/html2psrc;%{_sysconfdir}/html2psrc;' \
    -e 's;/usr/share/doc/html2ps;%{_pkgdocdir};' \
        html2ps > %{buildroot}%{_bindir}/html2ps
chmod 0755 %{buildroot}%{_bindir}/html2ps
install -p -m0644 html2ps.1 %{buildroot}%{_mandir}/man1
install -p -m0644 html2psrc.5 %{buildroot}%{_mandir}/man5
sed -e 's;/usr/bin;%{_bindir};' \
    -e 's;/usr/share/texmf-texlive;%{_datadir}/texmf;' \
    debian/config/html2psrc > %{buildroot}%{_sysconfdir}/html2psrc

install -m0755 -p contrib/xhtml2ps/xhtml2ps %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license COPYING
%doc README sample html2ps.html
%config(noreplace) %{_sysconfdir}/html2psrc
%{_bindir}/html2ps
%{_mandir}/man1/html2ps.1*
%{_mandir}/man5/html2psrc.5*

%files -n xhtml2ps
%license contrib/xhtml2ps/LICENSE
%doc contrib/xhtml2ps/README
%{_bindir}/xhtml2ps
%{_datadir}/applications/*xhtml2ps.desktop

%changelog
%autochangelog
