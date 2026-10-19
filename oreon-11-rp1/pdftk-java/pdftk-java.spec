%global source0_hash af1f18987e8f325952d540a3ea4fbb647e5a3baccdfe381ae91487d1d0c5c568
%global commit e4292c8f1bd2580a44d3cbf3570a4505bd3a74b6
Summary:        GCJ-free toolkit for manipulating PDF documents
Name:           pdftk-java
Version:        3.3.3
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND APAFML AND Apache-2.0
URL:            https://gitlab.com/pdftk-java/pdftk
Source0:        https://gitlab.com/pdftk-java/pdftk/-/archive/v%{version}/pdftk-%{version}.tar.gz
Patch0:         pdftk-java-3.3.1-classpath.patch
Patch1:         pdftk-java-3.3.3-bcprov-1.7x.patch
Patch2:         pdftk-java-3.3.2-bcprov-1.5x.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25-headless
Requires:       bouncycastle
Requires:       apache-commons-lang3
Requires:       javapackages-tools
Provides:       bundled(itext) = 2.1.7-4.2.0.modified_by_pdftk
Provides:       pdftk = %{version}-%{release}
Obsoletes:      pdftk < 2.03-1
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  apache-commons-lang3
BuildRequires:  bouncycastle
BuildRequires:  javapackages-local-openjdk25
# /oreon:deps
%description
If PDF is electronic paper, then pdftk-java is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses. PDFtk is a simple
tool for doing everyday things with PDF documents: Merge PDF documents, split
PDF pages into a new document, decrypt input as necessary (password required),
encrypt output as desired, burst a PDF document into single pages, report on
PDF metrics, including metadata and bookmarks, uncompress and re-compress page
streams, and repair corrupted PDF (where possible).

Pdftk-java is a port of the original GCJ-based PDFtk to Java. The GNU Compiler
for Java (GCJ) is a portable, optimizing, ahead-of-time compiler for the Java
programming language, which had no new developments since 2009 and was finally
removed in 2016 from the GCC development tree before the release of GCC 7.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pdftk-v%{version}-%{commit}
%patch -P0 -p1 -b .classpath
%patch -P2 -p1 -b .bcprov-1.5x

%build

ant -Dant.build.javac.target=1.8 -Dant.build.javac.source=1.8 jar
%install
install -D -p -m 0644 build/jar/pdftk.jar $RPM_BUILD_ROOT%{_javadir}/pdftk.jar
install -D -p -m 0644 pdftk.1 $RPM_BUILD_ROOT%{_mandir}/man1/pdftk.1
%jpackage_script com.gitlab.pdftk_java.pdftk "" "" bcprov:commons-lang3:pdftk pdftk true
%oreon_autofiles main

%check

sed -e 's| pdftk"|"|' $RPM_BUILD_ROOT%{_bindir}/pdftk > pdftk
chmod 755 pdftk
export CLASSPATH="$RPM_BUILD_ROOT%{_javadir}/pdftk.jar"
set -euo pipefail
./pdftk test/files/duck.pdf test/files/duck.pdf output two-ducks.pdf
./pdftk two-ducks.pdf dump_data | grep -q "NumberOfPages: 2"
./pdftk test/files/duck.pdf rotate 1east output rotated-duck.pdf
./pdftk rotated-duck.pdf dump_data | grep -q "PageMediaRotation: 90"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
