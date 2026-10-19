%global source0_hash 8976437e333757a84f7762c0bbf2e381afc000d3c485a1e42bcd3d7cb4efc1d7
%bcond_without html2ps_enables_ImageMagick
%bcond_without html2ps_enables_djpeg
%bcond_without html2ps_enables_netpbm
%bcond_with html2ps_enables_tex
%define my_subversion b7
Name:           html2ps
Version:        1.0
Release:        1%{?dist}
Summary:        HTML to PostScript converter
License:        GPL-2.0-or-later
URL:            http://user.it.uu.se/~jan/%{name}.html
Source0:        http://user.it.uu.se/~jan/%{name}-%{version}%{my_subversion}.tar.gz
Source1:        xhtml2ps.desktop
Patch0:         http://ftp.de.debian.org/debian/pool/main/h/%{name}/%{name}_1.0b5-5.diff.gz
Patch1:         %{name}-1.0b5-xdg-open.patch
Patch2:         %{name}-1.0b5-config.patch
Patch3:         %{name}-1.0b7-Remove-deprecated-variable.patch
Patch4:         html2ps-1.0b7-Fix-perl-5.22-warnings.patch
BuildArch:      noarch
Requires:       ghostscript
Requires:       paper
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
%if %{with html2ps_enables_tex}
Requires:       tex(dvips)
Requires:       tex(tex)
%endif
%if %{without html2ps_enables_ImageMagick}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Image::Magick\\)
%if %{with html2ps_enables_djpeg}
Requires:       libjpeg-turbo-utils
%endif
%if %{with html2ps_enables_netpbm}
Requires:       netpbm-progs
%endif
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
    's|paperconf|paper --no-size|g' \
     debian/patches/03_html2ps.dpatch

# 03_html2ps.dpatch is against 1.0b5, adjust it to 1.0b6
< debian/patches/03_html2ps.dpatch sed -e 's|/opt/misc/|/it/sw/share/www/|' | \
    patch -p1

%patch -P 4 -p1

%build

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
%oreon_autofiles xhtml2ps usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xhtml2ps -f %{oreon_filedir}/xhtml2ps.list

%changelog

%autochangelog
