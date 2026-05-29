%global source0_hash b5cac76c4a6945bdcf25857f187168147fde3402b33a6b1a3b1c00361719982c

Name:           lucene
Version:        10.3.2
Release:        %autorelease
Epoch:          0
Summary:        High-performance, full-featured text search engine
# License breakdown is present in NOTICE.txt file
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND BSD-2-Clause
URL:            https://lucene.apache.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://dlcdn.apache.org/lucene/java/10.3.2/lucene-10.3.2-src.tgz
Source1:        aggregator.pom
Source2:        aggregator-analysis.pom

Source3:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-common/10.3.2/lucene-analysis-common-10.3.2.pom
Source4:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-icu/10.3.2/lucene-analysis-icu-10.3.2.pom
Source5:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-kuromoji/10.3.2/lucene-analysis-kuromoji-10.3.2.pom
Source6:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-morfologik/10.3.2/lucene-analysis-morfologik-10.3.2.pom
Source7:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-nori/10.3.2/lucene-analysis-nori-10.3.2.pom
Source8:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-opennlp/10.3.2/lucene-analysis-opennlp-10.3.2.pom
Source9:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-phonetic/10.3.2/lucene-analysis-phonetic-10.3.2.pom
Source10:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-smartcn/10.3.2/lucene-analysis-smartcn-10.3.2.pom
Source11:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-stempel/10.3.2/lucene-analysis-stempel-10.3.2.pom

Source12:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-backward-codecs/10.3.2/lucene-backward-codecs-10.3.2.pom
Source13:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-benchmark/10.3.2/lucene-benchmark-10.3.2.pom
Source14:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-classification/10.3.2/lucene-classification-10.3.2.pom
Source15:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-codecs/10.3.2/lucene-codecs-10.3.2.pom
Source16:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-core/10.3.2/lucene-core-10.3.2.pom
Source17:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-demo/10.3.2/lucene-demo-10.3.2.pom
Source18:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-expressions/10.3.2/lucene-expressions-10.3.2.pom
Source19:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-facet/10.3.2/lucene-facet-10.3.2.pom
Source20:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-grouping/10.3.2/lucene-grouping-10.3.2.pom
Source21:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/10.3.2/lucene-highlighter-10.3.2.pom
Source22:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-join/10.3.2/lucene-join-10.3.2.pom
Source23:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-luke/10.3.2/lucene-luke-10.3.2.pom
Source24:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/10.3.2/lucene-memory-10.3.2.pom
Source25:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/10.3.2/lucene-misc-10.3.2.pom
Source26:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-monitor/10.3.2/lucene-monitor-10.3.2.pom
Source27:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/10.3.2/lucene-queries-10.3.2.pom
Source28:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/10.3.2/lucene-queryparser-10.3.2.pom
Source29:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-replicator/10.3.2/lucene-replicator-10.3.2.pom
Source30:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-sandbox/10.3.2/lucene-sandbox-10.3.2.pom
Source31:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial3d/10.3.2/lucene-spatial3d-10.3.2.pom
Source32:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-suggest/10.3.2/lucene-suggest-10.3.2.pom
Source33:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-test-framework/10.3.2/lucene-test-framework-10.3.2.pom


BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)

BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 10.1.0-4
Obsoletes:      %{name}-parent < 9
Obsoletes:      %{name}-solr-grandparent < 9


%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package analysis-common
Summary:        Lucene module: analysis-common
Obsoletes:      %{name}-analysis < 9

%description analysis-common
%{summary}.

%package analysis-icu
Summary:        Lucene module: analysis-icu
Obsoletes:      %{name}-analyzers-icu < 9

%description analysis-icu
%{summary}.

%package analysis-kuromoji
Summary:        Lucene module: analysis-kuromoji
Obsoletes:      %{name}-analyzers-kuromoji < 9

%description analysis-kuromoji
%{summary}.

%package analysis-nori
Summary:        Lucene module: analysis-nori
Obsoletes:      %{name}-analyzers-nori < 9

%description analysis-nori
%{summary}.

%package analysis-phonetic
Summary:        Lucene module: analysis-phonetic
Obsoletes:      %{name}-analyzers-phonetic < 9

%description analysis-phonetic
%{summary}.

%package analysis-smartcn
Summary:        Lucene module: analysis-smartcn
Obsoletes:      %{name}-analyzers-smartcn < 9

%description analysis-smartcn
%{summary}.

%package analysis-stempel
Summary:        Lucene module: analysis-stempel
Obsoletes:      %{name}-analyzers-stempel < 9

%description analysis-stempel
%{summary}.

%package backward-codecs
Summary:        Lucene module: backward-codecs

%description backward-codecs
%{summary}.

%package classification
Summary:        Lucene module: classification

%description classification
%{summary}.

%package codecs
Summary:        Lucene module: codecs

%description codecs
%{summary}.

%package core
Summary:        Lucene module: core
Obsoletes:      %{name} < 9

%description core
%{summary}.

%package expressions
Summary:        Lucene module: expressions

%description expressions
%{summary}.

%package facet
Summary:        Lucene module: facet

%description facet
%{summary}.

%package grouping
Summary:        Lucene module: grouping

%description grouping
%{summary}.

%package highlighter
Summary:        Lucene module: highlighter

%description highlighter
%{summary}.

%package join
Summary:        Lucene module: join

%description join
%{summary}.

%package memory
Summary:        Lucene module: memory

%description memory
%{summary}.

%package misc
Summary:        Lucene module: misc

%description misc
%{summary}.

%package monitor
Summary:        Lucene module: monitor

%description monitor
%{summary}.

%package queries
Summary:        Lucene module: queries

%description queries
%{summary}.

%package queryparser
Summary:        Lucene module: queryparser

%description queryparser
%{summary}.

%package sandbox
Summary:        Lucene module: sandbox

%description sandbox
%{summary}.

%package spatial3d
Summary:        Lucene module: spatial3d

%description spatial3d
%{summary}.

%package suggest
Summary:        Lucene module: suggest

%description suggest
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

find -mindepth 1 -maxdepth 1 ! -name lucene ! -name LICENSE.txt ! -name NOTICE.txt ! -name README.md -exec rm -rf {} +
mv -t . lucene/*
rmdir lucene

cp %SOURCE1 pom.xml

function add_pom {
  source=${1}
  prefix=${2}
  module=${source}
  module=${module##*/${prefix}}
  module=${module%%%%-%{version}.pom}
  cp ${source} ${module}/pom.xml
}

for source in $(echo %{sources} | tr ' ' '\n' | grep -v 'lucene-analysis-.*\.pom' | grep 'lucene-.*\.pom'); do
  add_pom ${source} "lucene-"
  %pom_add_parent org.fedoraproject.xmvn.lucene:aggregator:any ${module}
  %pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" "compile" ${module}
done

pushd analysis
cp %SOURCE2 pom.xml
%pom_add_parent org.fedoraproject.xmvn.lucene:aggregator:any

for source in $(echo %{sources} | tr ' ' '\n' | grep 'lucene-analysis-.*\.pom'); do
  add_pom ${source} "lucene-analysis-"
  %pom_add_parent org.fedoraproject.xmvn.lucene:aggregator-analysis:any ${module}
done
popd

%pom_disable_module benchmark
%pom_disable_module demo
%pom_disable_module luke
%pom_disable_module replicator
%pom_disable_module test-framework

%pom_disable_module morfologik analysis
%pom_disable_module opennlp analysis

%mvn_package :aggregator __noinstall
%mvn_package :aggregator-analysis __noinstall

%build
# Tests have unpackaged dependencies
%mvn_build -s -f -j

%install
%mvn_install

%files analysis-common -f .mfiles-lucene-analysis-common
%files analysis-icu -f .mfiles-lucene-analysis-icu
%files analysis-kuromoji -f .mfiles-lucene-analysis-kuromoji
%files analysis-nori -f .mfiles-lucene-analysis-nori
%files analysis-phonetic -f .mfiles-lucene-analysis-phonetic
%files analysis-smartcn -f .mfiles-lucene-analysis-smartcn
%files analysis-stempel -f .mfiles-lucene-analysis-stempel
%files backward-codecs -f .mfiles-lucene-backward-codecs
%files classification -f .mfiles-lucene-classification
%files codecs -f .mfiles-lucene-codecs

# core is a common dependency of all other modules
%files core -f .mfiles-lucene-core
%license LICENSE.txt NOTICE.txt
%doc README.md

%files expressions -f .mfiles-lucene-expressions
%files facet -f .mfiles-lucene-facet
%files grouping -f .mfiles-lucene-grouping
%files highlighter -f .mfiles-lucene-highlighter
%files join -f .mfiles-lucene-join
%files memory -f .mfiles-lucene-memory
%files misc -f .mfiles-lucene-misc
%files monitor -f .mfiles-lucene-monitor
%files queries -f .mfiles-lucene-queries
%files queryparser -f .mfiles-lucene-queryparser
%files sandbox -f .mfiles-lucene-sandbox
%files spatial3d -f .mfiles-lucene-spatial3d
%files suggest -f .mfiles-lucene-suggest

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.3.2-1
- Prepare for Oreon 11 (RP1)
