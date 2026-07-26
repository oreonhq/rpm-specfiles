%global source0_hash none

%global extname TexMaths

Name:           libreoffice-%{extname}
Version:        0.52.4
Release:        2%{?dist}
Summary:        A LaTex Equation Editor for LibreOffice

License:        GPL-2.0-or-later
URL:            http://roland65.free.fr/texmaths/
Source0:        http://downloads.sourceforge.net/texmaths/%{extname}-%{version}.oxt

BuildRequires: libreoffice-sdk
# Needs the draw component
Requires: libreoffice-draw
# Needs at least writer or impress to be useful
Requires: libreoffice-writer
# We end up missing deps if we go with just /usr/bin/latex or similar
Requires: tex(latex)
Requires: /usr/bin/dvipng
Obsoletes: openoffice.org-ooolatex < 4.0.0-0.15

# We are actually not compiled
%global debug_package %{nil}

# The location of the installed extension.
%global loextdir %{_libdir}/libreoffice/share/extensions/%{extname}

%if 0%{?fedora} >= 37
# Fedora 37 dropped java for i686
ExclusiveArch: %{java_arches}
%endif

# EL8+ aarch64/s390x is missing libreoffice-sdk
%if 0%{?rhel}
ExcludeArch: aarch64 s390x
%endif

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
# remove binaries that are already included in latex2emf/libEMF
# copy the rest
cp -a * $RPM_BUILD_ROOT%{loextdir}
# remove documentation already in doc
rm $RPM_BUILD_ROOT%{loextdir}/{README,license.txt}

%files
%license license.txt
%doc README
%{loextdir}

%changelog
%autochangelog
