%global source0_hash 684ea53c1f5b71d6d1ac6086bbc96906b1f709ecc7ab536615b0f0c9e1baa3cc

Name:           asciidoc
Version:        10.2.0
Release:        19%{?dist}
Summary:        Text based document generation

License:        GPL-2.0-or-later
URL:            http://asciidoc.org
Source0:        https://github.com/asciidoc-py/asciidoc-py/archive/%{version}/%{name}-py-%{version}.tar.gz

BuildArch:      noarch

Patch1:         asciidoc-table-separator.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  (python3-wheel if python3-setuptools < 71)
BuildRequires:  dblatex
BuildRequires:  docbook-style-xsl
BuildRequires:  graphviz
BuildRequires:  libxslt
BuildRequires:  source-highlight
BuildRequires:  texlive-dvipng-bin
BuildRequires:  texlive-dvisvgm-bin
BuildRequires:  symlinks
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make

Requires:       python3
Requires:       docbook-style-xsl
Requires:       graphviz
Requires:       libxslt
Requires:       source-highlight

%description
AsciiDoc is a text document format for writing short documents,
articles, books and UNIX man pages. AsciiDoc files can be translated
to HTML and DocBook markups using the asciidoc(1) command.

%package doc
Summary:  Additional documentation and examples for asciidoc

Requires: %{name} = %{version}-%{release}

%description doc
%{summary}.

%package latex
Summary:  Support for asciidoc latex output

Requires: %{name} = %{version}-%{release}
Requires: dblatex
Requires: texlive-dvipng-bin

%description latex
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-py-%{version} -p1

%build
autoreconf -v
%configure
%make_build

%install
make install docs manpages DESTDIR=%{buildroot} PIP_NO_BUILD_ISOLATION=0
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}/share/doc/doc/{asciidoc.1,a2x.1,testasciidoc.1} %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}/%{_pkgdocdir}/doc
mv %{buildroot}/share/doc/doc/ %{buildroot}/%{_pkgdocdir}/doc
mkdir -p %{buildroot}/%{_pkgdocdir}/doc/images
mv %{buildroot}/share/doc/images/ %{buildroot}/%{_pkgdocdir}/doc/images
rm  %{buildroot}/share/doc/{BUGS.adoc,CHANGELOG.adoc,INSTALL.adoc,README.md,dblatex/dblatex-readme.txt,docbook-xsl/asciidoc-docbook-xsl.txt}

# Some tests are failing
#%%check
#export PATH="../:$PATH"
#cd tests
#%%{__python3} testasciidoc.py update
#%%{__python3} testasciidoc.py run

%files
%doc BUGS.adoc CHANGELOG.adoc COPYRIGHT README.md
%{_mandir}/man1/*.1*
%{_bindir}/a2x
%{_bindir}/asciidoc
%{python3_sitelib}/asciidoc-%{version}.dist-info/
%{python3_sitelib}/asciidoc/
%exclude %{python3_sitelib}/asciidoc/resources/filters/latex
%exclude %{python3_sitelib}/asciidoc/resources/filters/music
%exclude %{_pkgdocdir}/doc

%files doc
%doc COPYRIGHT
%{_pkgdocdir}/doc/

%files latex
%doc COPYRIGHT
%dir %{python3_sitelib}/asciidoc/resources/filters/latex

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.2.0-19
- Prepare for Oreon 11 (RP1)
