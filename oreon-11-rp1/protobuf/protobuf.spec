# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 440848dffa209beb8a04e41cc352762e44f8e91342b2a43aab6af9b30713c2f6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond java 0
%else
%bcond java %{undefined rhel}
%endif

%bcond_with check

Summary:        Protocol Buffers - Google's data interchange format
Name:           protobuf
Version:        33.5
%global so_version 33
Release:        1%{?dist}

%global version_protoc %{version}
%global version_cpp 6.%{version}
%global version_csharp 3.%{version}
%global version_java 4.%{version}
%global version_javascript 3.%{version}
%global version_objectivec 4.%{version}
%global version_php 4.%{version}
%global version_ruby 4.%{version}

License:        BSD-3-Clause AND MIT
URL:            https://github.com/protocolbuffers/protobuf
Source0:        %{url}/archive/v%{version}/protobuf-%{version}.tar.gz
Source1:        ftdetect-proto.vim
Source2:        protobuf-init.el
Source4:        protoc.1

Patch:          protobuf-6.31.1-system-gtest.patch

Patch:          protobuf-6.35.5-upb-fix-big-endian.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  emacs
BuildRequires:  zlib-devel
BuildRequires:  cmake(absl)
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel

Requires:       protobuf-cpp%{?_isa} = %{version_cpp}-%{release}

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

Protocol buffers are a flexible, efficient, automated mechanism for serializing
structured data – think XML, but smaller, faster, and simpler. You define how
you want your data to be structured once, then you can use special generated
source code to easily write and read your structured data to and from a variety
of data streams and using a variety of languages. You can even update your data
structure without breaking deployed programs that are compiled against the
"old" format.

%package cpp
Summary:        Protocol Buffers C++ libraries
Version:        %{version_cpp}

Provides:       bundled(utf8_range) = 1.0

%description cpp
This package contains the C++ libraries for Protocol Buffers.

See also protobuf-lite.

%package compiler
Summary:        Protocol Buffers compiler
Version:        %{version_protoc}

Requires:       protobuf-cpp%{?_isa} = %{version_cpp}-%{release}

Provides:       bundled(utf8_range) = 1.0
Conflicts:      protobuf3-compiler

%description compiler
This package contains Protocol Buffers compiler for all programming languages.

%package devel
Summary:        Protocol Buffers C++ development headers and libraries
Version:        %{version_cpp}

Requires:       protobuf-cpp%{?_isa} = %{version_cpp}-%{release}
Requires:       protobuf-compiler%{?_isa} = %{version_protoc}-%{release}
Requires:       protobuf-lite%{?_isa} = %{version_cpp}-%{release}
Requires:       zlib-devel

Provides:       protobuf-lite-devel = %{version_cpp}-%{release}
Provides:       bundled(utf8_range) = 1.0
Provides:       upb-static

Obsoletes:      protobuf-lite-devel < 3.25.1-4
Obsoletes:      protobuf-lite-static < 3.19.6-4
Obsoletes:      protobuf-static < 3.19.6-4

Conflicts:      protobuf3-devel
Conflicts:      protobuf3-lite-devel

%description devel
This package contains Protocol Buffers compiler for all languages and C++
headers and libraries. It contains the headers and libraries for both
libprotobuf and libprotobuf-lite.

%package static
Summary:        Protocol Buffers C++ development static libraries
Version:        %{version_cpp}

Requires:       protobuf-devel%{?_isa} = %{version_cpp}-%{release}

Provides:       protobuf-lite-static

%description static
This package contains Protocol Buffers compiler for all languages and C++
static libraries. It contains the headers and libraries for both libprotobuf
and libprotobuf-lite.

%package lite
Summary:        Protocol Buffers LITE_RUNTIME libraries
Version:        %{version_cpp}

Provides:       bundled(utf8_range) = 1.0

%description lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

See also protobuf-cpp.

%package vim
Summary:        Vim syntax highlighting for Google Protocol Buffers descriptions
License:        BSD-3-Clause

BuildArch:      noarch

Requires:       vim-filesystem
Conflicts:      protobuf3-vim

%description vim
This package contains syntax highlighting for Google Protocol Buffers
descriptions in Vim editor

%if %{with java}
%ifarch %{java_arches}

%package java
Summary:        Java Protocol Buffers runtime library
Version:        %{version_java}
License:        BSD-3-Clause

BuildArch:      noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

Requires:       (protobuf-compiler = %{version_protoc}-%{release} if protobuf-compiler)

%description java
This package contains Java Protocol Buffers runtime library.

%package javalite
Summary:        Java Protocol Buffers lite runtime library
Version:        %{version_java}
License:        BSD-3-Clause

BuildArch:      noarch

%description javalite
This package contains Java Protocol Buffers lite runtime library.

%package java-util
Summary:        Utilities for Protocol Buffers
Version:        %{version_java}
License:        BSD-3-Clause

BuildArch:      noarch

%description java-util
Utilities to work with protos. It contains JSON support as well as utilities to
work with proto3 well-known types.

%package javadoc
Summary:        Javadoc for protobuf-java
Version:        %{version_java}
License:        BSD-3-Clause

BuildArch:      noarch

%description javadoc
This package contains the API documentation for protobuf-java.

%package parent
Summary:        Protocol Buffer Parent POM
Version:        %{version_java}
License:        BSD-3-Clause

BuildArch:      noarch

%description parent
Protocol Buffer Parent POM.

%package bom
Summary:        Protocol Buffer BOM POM
Version:        %{version_java}
License:        BSD-3-Clause

BuildArch:      noarch

%description bom
Protocol Buffer BOM POM.

%endif
%endif

%package emacs
Summary:        Emacs mode for Google Protocol Buffers descriptions
License:        BSD-3-Clause

BuildArch:      noarch

Requires:       emacs-filesystem >= %{_emacs_version}
Conflicts:      protobuf3-emacs

%description emacs
This package contains syntax highlighting for Google Protocol Buffers
descriptions in the Emacs editor.

%prep
%oreon_sha256
%autosetup -p1

%if %{with java}
%ifarch %{java_arches}
%pom_disable_module kotlin java
%pom_disable_module kotlin-lite java

%pom_remove_dep com.google.protobuf:protobuf-kotlin java/bom
%pom_remove_dep com.google.truth:truth java

%pom_remove_plugin :maven-javadoc-plugin java
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin java

annotations=$(
    find java/util -name '*.java' -exec \
      grep -h -e '^import com\.google\.errorprone\.annotation' \
              -e '^import com\.google\.j2objc\.annotations' {} + |
      sort -u | sed 's/.*\.\([^.]*\);/\1/' | paste -sd\|
)
find java/util -name '*.java' -exec sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g' {} +

%mvn_file :protobuf-java:jar: protobuf/protobuf-java protobuf

sed -r -i 's@/protoc</protoc>@/%{_vpath_builddir}&@' java/pom.xml
%endif
%endif

find examples -type f -name '*.rb' -exec sed -r -i \
    '1{s@^(#!)([[blank:]]*/.*/env[[:blank:]]+)(ruby)@\1/usr/bin@}' '{}' '+'

%build
iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt

export PTHREAD_LIBS="-lpthread"
export CXXFLAGS="${CXXFLAGS} -Wno-error=type-limits"

%cmake \
    -Dprotobuf_ABSL_PROVIDER=package \
    -Dprotobuf_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
    -Dprotobuf_FIND_GOOGLETEST:BOOL=ON \
    -Dprotobuf_MSVC_STATIC_RUNTIME=OFF \
    -GNinja
%cmake_build

%global original_vpath_builddir %{_vpath_builddir}
%global _vpath_builddir %{_vpath_builddir}-static
%cmake \
    -Dprotobuf_BUILD_SHARED_LIBS:BOOL=OFF \
    -Dprotobuf_ABSL_PROVIDER=package \
    -Dprotobuf_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
    -Dprotobuf_FIND_GOOGLETEST:BOOL=ON \
    -Dprotobuf_MSVC_STATIC_RUNTIME=OFF \
    -GNinja
%cmake_build
%global _vpath_builddir %{original_vpath_builddir}

%if %{with java}
%ifarch %{java_arches}
%ifarch %{ix86} s390x
export MAVEN_OPTS=-Xmx1024m
%endif
srcdir=$PWD/src
java_srcdir=$PWD/java/core/src/main/resources
dependencies="<dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>com.google.guava</groupId>
      <artifactId>guava</artifactId>
      <scope>test</scope>
    </dependency>"
dependencies_util="<dependency>
      <groupId>\${project.groupId}</groupId>
      <artifactId>protobuf-java</artifactId>
    </dependency>
    <dependency>
      <groupId>com.google.guava</groupId>
      <artifactId>guava</artifactId>
    </dependency>
    <dependency>
      <groupId>com.google.code.findbugs</groupId>
      <artifactId>jsr305</artifactId>
      <version>3.0.2</version>
    </dependency>
    <dependency>
      <groupId>com.google.guava</groupId>
      <artifactId>guava-testlib</artifactId>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>com.google.code.gson</groupId>
      <artifactId>gson</artifactId>
      <version>2.8.6</version>
    </dependency>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <scope>test</scope>
    </dependency>"
build1="     "'<!-- Include core protos in the bundle as resources -->'"
     <resources>
      <resource>
        <directory>\${protobuf.source.dir}</directory>
        <includes>\n"
build2="\n        </includes>
      </resource>
    </resources>"
cd java/core
    mkdir -p src/main/java/com/google/protobuf src/main/resources/google/protobuf
    protos=$(sed -rn "/protobuf\.source\.dir/s,.*protobuf/(.+\.proto)\".*,$srcdir/google/protobuf/\1,p" generate-sources-build.xml)
    includes=$(sed -rn "/protobuf\.source\.dir/s,.*protobuf/(.+\.proto)\".*,\          <include>google/protobuf/\1</include>,p" generate-sources-build.xml)
    ../../%{_vpath_builddir}/protoc --java_out=src/main/java --proto_path=$srcdir --proto_path=$java_srcdir $java_srcdir/google/protobuf/java_features.proto $protos
    cp -p $protos src/main/resources/google/protobuf
    sed -e 's/{groupId}/com.google.protobuf/' \
        -e 's/{version}/%{version_java}/' \
        -e 's/{artifactId}/protobuf-java/' \
        -e 's/{type}/bundle/' \
        pom_template.xml > pom.xml
    awk -v dep="${dependencies}" -i inplace '{gsub(/\{dependencies\}/,dep)}1' pom.xml
    awk -v bld="${build1}${includes}${build2}" -i inplace '{gsub(/<build>/,"&" bld)}1' pom.xml
cd -
cd java/lite
    mkdir -p src/main/java/com/google/protobuf src/main/resources/google/protobuf
    protos=$(sed -rn "/protobuf\.source\.dir/s,.*protobuf/(.+\.proto)\".*,$srcdir/google/protobuf/\1,p" generate-sources-build.xml)
    includes=$(sed -rn "/protobuf\.source\.dir/s,.*protobuf/(.+\.proto)\".*,\          <include>google/protobuf/\1</include>,p" generate-sources-build.xml)
    ../../%{_vpath_builddir}/protoc --java_out=lite:src/main/java --proto_path=$srcdir --proto_path=$java_srcdir $java_srcdir/google/protobuf/java_features.proto $protos
    cp -p $protos src/main/resources/google/protobuf
    sed -e 's/{groupId}/com.google.protobuf/' \
        -e 's/{version}/%{version_java}/' \
        -e 's/{artifactId}/protobuf-javalite/' \
        -e 's/{type}/bundle/' \
        pom_template.xml > pom.xml
    awk -v dep="${dependencies}" -i inplace '{gsub(/\{dependencies\}/,dep)}1' pom.xml
    awk -v bld="${build1}${includes}${build2}" -i inplace '{gsub(/<build>/,"&" bld)}1' pom.xml
    cp -p ../core/src/main/java/com/google/protobuf/{Abstract{Parser,ProtobufList},Android,ArrayDecoders,{Boolean,Int,Double,Float,Long,Protobuf}ArrayList,ByteBufferWriter,ByteOutput,ByteString,CanIgnoreReturnValue,CheckReturnValue,CodedInputStream{,Reader},CodedOutputStream{,Writer},CompileTimeConstant,ExperimentalApi,ExtensionRegistryFactory,ExtensionSchema{,s},Field{Info,Set,Type},Generated{,MessageInfoFactory},InlineMe,Internal,InvalidProtocolBufferException,IterableByteBufferInputStream,Java8Compatibility,JavaType,Lazy{Field,StringList},ListFieldSchema{,s},ManifestSchemaFactory,MapFieldSchema{,s},Message{Info{,Factory},{Set,}Schema},NewInstanceSchema{,s},OneofInfo,Parser,PrimitiveNonBoxingCollection,Protobuf,ProtocolStringList,ProtoSyntax,RawMessageInfo,Reader,RopeByteString,Schema{,Factory,Util},SmallSortedMap,StructuralMessageInfo,TextFormatEscaper,UninitializedMessageException,UnknownFieldSchema,UnsafeUtil,Utf8,WireFormat,Writer,*Lite*}.java src/main/java/com/google/protobuf
cd -
cd java/util
    sed -e 's/{groupId}/com.google.protobuf/' \
        -e 's/{version}/%{version_java}/' \
        -e 's/{artifactId}/protobuf-java-util/' \
        -e 's/{type}/bundle/' \
        pom_template.xml > pom.xml
    awk -v dep="${dependencies_util}" -i inplace '{gsub(/\{dependencies\}/,dep)}1' pom.xml
cd -

%mvn_build -s -f -- -f java/pom.xml
%endif
%endif

%{_emacs_bytecompile} editors/protobuf-mode.el

%install
%global _vpath_builddir %{_vpath_builddir}-static
%cmake_install
%global _vpath_builddir %{original_vpath_builddir}
%cmake_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} +

install -p -m 0644 -D -t '%{buildroot}%{_mandir}/man1' '%{SOURCE4}'

install -p -m 644 -D %{SOURCE1} %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/proto.vim
install -p -m 644 -D editors/proto.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/proto.vim

%if %{with java}
%ifarch %{java_arches}
%mvn_install
%endif
%endif

mkdir -p %{buildroot}%{_emacs_sitelispdir}/protobuf
install -p -m 0644 editors/protobuf-mode.el %{buildroot}%{_emacs_sitelispdir}/protobuf
install -p -m 0644 editors/protobuf-mode.elc %{buildroot}%{_emacs_sitelispdir}/protobuf
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_emacs_sitestartdir}

%check
%if %{with check}
%ctest
%endif

%files

%files cpp
%license LICENSE
%doc CONTRIBUTORS.txt
%doc README.md

%{_libdir}/libprotobuf.so.%{so_version}{,.*}
%{_libdir}/libutf8_range.so.%{so_version}{,.*}
%{_libdir}/libutf8_validity.so.%{so_version}{,.*}

%files compiler
%{_bindir}/protoc
%{_bindir}/protoc-%{version_protoc}*
%{_mandir}/man1/protoc.1*

%{_bindir}/protoc-gen-upb
%{_bindir}/protoc-gen-upb-%{version_protoc}*
%{_bindir}/protoc-gen-upbdefs
%{_bindir}/protoc-gen-upbdefs-%{version_protoc}*
%{_bindir}/protoc-gen-upb_minitable
%{_bindir}/protoc-gen-upb_minitable-%{version_protoc}*

%{_libdir}/libprotoc.so.%{so_version}{,.*}

%files devel
%doc examples/Makefile
%doc examples/README.md
%doc examples/add_person.cc
%doc examples/addressbook.proto
%doc examples/list_people.cc

%dir %{_includedir}/google/
%{_includedir}/google/protobuf/

%{_includedir}/upb/
%{_libdir}/pkgconfig/upb.pc
%{_libdir}/libupb.a

%{_libdir}/cmake/protobuf/
%{_libdir}/pkgconfig/protobuf.pc
%{_libdir}/pkgconfig/protobuf-lite.pc
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so

%{_includedir}/utf8_range.h
%{_includedir}/utf8_validity.h
%{_libdir}/cmake/utf8_range/
%{_libdir}/pkgconfig/utf8_range.pc
%{_libdir}/libutf8_range.so
%{_libdir}/libutf8_validity.so

%files static
%{_libdir}/libprotobuf-lite.a
%{_libdir}/libprotobuf.a
%{_libdir}/libprotoc.a

%files emacs
%license LICENSE
%{_emacs_sitelispdir}/protobuf/
%{_emacs_sitestartdir}/protobuf-init.el

%files lite
%license LICENSE
%{_libdir}/libprotobuf-lite.so.%{so_version}{,.*}

%files vim
%license LICENSE
%{_datadir}/vim/vimfiles/ftdetect/proto.vim
%{_datadir}/vim/vimfiles/syntax/proto.vim

%if %{with java}
%ifarch %{java_arches}

%files java -f .mfiles-protobuf-java
%license LICENSE
%doc examples/AddPerson.java
%doc examples/ListPeople.java
%doc java/README.md

%files java-util -f .mfiles-protobuf-java-util
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files parent -f .mfiles-protobuf-parent
%license LICENSE

%files bom -f .mfiles-protobuf-bom
%license LICENSE

%files javalite -f .mfiles-protobuf-javalite
%license LICENSE

%endif
%endif

%changelog
%autochangelog
