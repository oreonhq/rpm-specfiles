%global source0_hash c4545539b17caa042110a356bf6f02631061a990e234b328670cb2ec8eecb9be
%global extname TexMaths
Name:           libreoffice-%{extname}
Version:        0.52.6
Release:        1%{?dist}
Summary:        A LaTex Equation Editor for LibreOffice
License:        GPL-2.0-or-later
URL:            http://roland65.free.fr/texmaths/
Source0:        http://downloads.sourceforge.net/texmaths/%{extname}-%{version}.oxt
Requires: libreoffice-draw
Requires: libreoffice-writer
Requires: tex(latex)
Requires: /usr/bin/dvipng
Obsoletes: openoffice.org-ooolatex < 4.0.0-0.15
%global debug_package %{nil}
%global loextdir %{_libdir}/libreoffice/share/extensions/%{extname}
# oreon:deps
BuildRequires:  libreoffice-sdk
# /oreon:deps
%description
TexMaths is a LaTeX equation editor for LibreOffice.  It is derived from
OOoLatex, originally developed by Geoffroy Piroux.

As its predecessor, TexMaths is a LibreOffice extension that allows you to
enter and edit LaTeX equations directly into LibreOffice documents.

%prep

%setup -q -c
# Fix FSF address
sed -i -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/' license.txt

%install
mkdir -p $RPM_BUILD_ROOT%{loextdir}
cp -a * $RPM_BUILD_ROOT%{loextdir}
rm $RPM_BUILD_ROOT%{loextdir}/{README,license.txt}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
