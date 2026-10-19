%global source0_hash 16e82786272ed1806a079d37914d7ba7a594db792dc4cc34c1c3737dbd4da079
%bcond_with texlive_split 0
Name:       dblatex
Version:    0.3.12
Release:        1%{?dist}
Summary:        DocBook to LaTeX/ConTeXt Publishing
BuildArch:  noarch
License:    GPL-2.0-or-later AND GPL-2.0-only AND LPPL-1.3a AND LicenseRef-DMIT AND LicenseRef-Fedora-Public-Domain
URL:        http://dblatex.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}3-%{version}.tar.bz2
Source1:    COPYING-docbook-xsl
Patch0:     dblatex-0.3.11-disable-debian.patch
Patch1:     dblatex-0.3.11-which-shutil.patch
Patch2:     dblatex-0.3.11-replace-inkscape-by-rsvg.patch
Patch3:     dblatex-0.3.12-replace-imp-by-importlib.patch
Patch4:     dblatex-0.3.12-adjust-submodule-imports.patch
Patch5:     dblatex-0.3.12-remove-shebangs-from-non-scripts.patch
%if %{with texlive_split}
%endif
Requires:       texlive-base
Requires:       texlive-collection-latex
Requires:       texlive-collection-xetex
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-xmltex texlive-xmltex-bin
Requires:       texlive-anysize
Requires:       texlive-appendix
Requires:       texlive-bibtopic
Requires:       texlive-changebar
Requires:       texlive-ec
Requires:       texlive-fancybox
Requires:       texlive-footmisc
Requires:       texlive-jknapltx
Requires:       texlive-multirow
Requires:       texlive-overpic
%if %{with texlive_split}
Requires:       texlive-passivetex
%endif
Requires:       texlive-pdfpages
Requires:       texlive-subfigure
Requires:       texlive-stmaryrd
Requires:       texlive-wasysym
Requires:       texlive-xmltex-bin
Requires:       libxslt docbook-dtds
Recommends:     ImageMagick
Recommends:     texlive-epstopdf-bin
Recommends:     transfig
Recommends:     librsvg2-tools
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dblatex = %{version}-%{release}
# /oreon:deps
%description
dblatex is a program that transforms your SGML/XMLDocBook
documents to DVI, PostScript or PDF by translating them
into pure LaTeX as a first process.  MathML 2.0 markups
are supported, too. It started as a clone of DB2LaTeX.

Authors:
--------
   Benoît Guillon <marsgui at users dot sourceforge dot net>
   Andreas Hoenen <andreas dot hoenen at arcor dot de>

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}3-%{version} -p 1
# build_scripts uses install command arguments
sed -i -e "/if not(install.install_data)/i \        install.install_data = '%{_prefix}'" setup.py
sed -i -e "s|self._install_lib = .*|self._install_lib = '%{python3_sitelib}'|" setup.py

# We do not ship contrib parts:
rm -rf lib/contrib

%build

%pyproject_wheel
%install
%pyproject_install
for file in bibtopic.sty enumitem.sty ragged2e.sty passivetex/ xelatex/; do
  rm -rf $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/misc/$file
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex
for file in ` find $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/ -name '*.sty' ` ; do
  mv $file $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/`basename $file`;
done
for file in ` find $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/ -name '*.xetex' ` ; do
  mv $file $RPM_BUILD_ROOT%{_datadir}/texlive/texmf-dist/tex/latex/dblatex/`basename $file`;
done
rmdir $RPM_BUILD_ROOT%{_datadir}/dblatex/latex/{misc,contrib/example,style}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dblatex
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/
sed -e 's/\r//' xsl/mathml2/README > README-xsltml
touch -r xsl/mathml2/README README-xsltml
cp -p %{SOURCE1} COPYING-docbook-xsl
%oreon_autofiles main

%post -p /usr/bin/texhash

%postun -p /usr/bin/texhash

%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.12-1
- Prepare for Oreon 11 (RP1)
