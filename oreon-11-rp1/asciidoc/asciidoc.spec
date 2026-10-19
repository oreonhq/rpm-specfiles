%global source0_hash 8e1fb9691952cc4f13357e1ef58172e566c5f88e3c44222d4a8693585f884507
Name:           asciidoc
Version:        10.2.1
Release:        1%{?dist}
Summary:        Text based document generation
License:        GPL-2.0-or-later
URL:            http://asciidoc.org
Source0:        https://github.com/asciidoc-py/asciidoc-py/archive/refs/tags/%{version}.tar.gz#/%{name}-py-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3
Requires:       docbook-style-xsl
Requires:       graphviz
Requires:       libxslt
Requires:       source-highlight
# oreon:deps
BuildRequires:  (python3-wheel if python3-setuptools < 71)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dblatex
BuildRequires:  docbook-style-xsl
BuildRequires:  graphviz
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  source-highlight
BuildRequires:  symlinks
BuildRequires:  texlive-dvipng-bin
BuildRequires:  texlive-dvisvgm-bin
# /oreon:deps
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
%global oreon_srcdir %{name}-py-%{version}
%oreon_prep
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
%oreon_autofiles asciidoc-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles asciidoc-latex usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n asciidoc-doc -f %{oreon_filedir}/asciidoc-doc.list
%files -n asciidoc-latex -f %{oreon_filedir}/asciidoc-latex.list

%changelog

%autochangelog
