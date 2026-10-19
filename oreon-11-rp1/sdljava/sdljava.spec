%global source0_hash cb2e3b798ae599d0126e5a9b806da76a608a809babf69bd5d288db361c779859
Name:           sdljava
Version:        0.9.1
Release:        1%{?dist}
Summary:        Java binding to the SDL API
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sdljava.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-runtest.sh
Patch0:         sdljava-0.9.1-regen.patch
Patch1:         sdljava-0.9.1-ftgl213.patch
Patch2:         sdljava-0.9.1-ruby19.patch
ExclusiveArch:  %{java_arches}
Requires:       java-25
Requires:       javapackages-filesystem
Requires:       jdom
# oreon:deps
BuildRequires:  //bin/ruby
BuildRequires:  SDL-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  ant-openjdk25
BuildRequires:  font(dejavusans)
BuildRequires:  fontconfig
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  jdom
BuildRequires:  make
BuildRequires:  rubygems
BuildRequires:  swig
BuildRequires:  xml-commons-apis
# /oreon:deps
%description
sdljava is a Java binding to the SDL API being developed by Ivan Ganza.

sdljava provides the ability to write games and other applications
from the java programming language. sdljava is designed to be fast,
efficient and easy to use.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Some examples for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       font(dejavusans)
Requires:       javapackages-tools
%description demo
Demonstrations and samples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

find -name '*.jar' -or -name '*.class' -or -name '*.bat' -name '*.so' -delete
rm -r etc/build/gljava/windows etc/build/windows

# Newer ftgl no longer exports the FTFace class
rm src/org/gljava/opengl/ftgl/FTFace.java
iconv -f ISO_8859-2 -t UTF8 docs/CHANGES_0_9_1 > docs/CHANGES_0_9_1.tmp
touch -r docs/CHANGES_0_9_1 docs/CHANGES_0_9_1.tmp
mv docs/CHANGES_0_9_1.tmp docs/CHANGES_0_9_1

# patch in gcc include path so that swig can find it
GCC_PATH=`gcc -print-search-dirs | grep install | cut -f 2 -d " "`
sed -i "s#@GCC_INCLUDE_PATH@#$GCC_PATH/include#g" \
  etc/build/linux/Makefile \
  etc/build/gljava/linux/Makefile \
  etc/build/gljava/linux/ftgl/Makefile

# adjust testdata path in demos
find ./testsrc -name '*.java' | xargs sed -i \
  -e 's|testdata|%{_datadir}/%{name}/testdata|g'

# use system versions of jdom
build-jar-repository -p lib jdom

# copy the Linux Makefiles into place
cp etc/build/linux/Makefile src/sdljava/native
cp etc/build/gljava/linux/Makefile src/org/gljava/opengl/native
cp etc/build/gljava/linux/ftgl/Makefile src/org/gljava/opengl/native/ftgl

# and remove the swig generated code so that it gets regenerated
rm src/sdljava/native/SDL*_wrap.c src/sdljava/native/SDL_types.h
rm src/org/gljava/opengl/native/glew_wrap.c

%build

%ifarch ppc
export ARCH_DEFINE="-D__powerpc__ -D__LONG_DOUBLE_128__"
%endif
%ifarch ppc64
export ARCH_DEFINE="-D__powerpc__ -D__powerpc64__ -D__LONG_DOUBLE_128__"
%endif
%ifarch ppc64le
export ARCH_DEFINE="-D__powerpc__ -D__powerpc64__ -D__LITTLE_ENDIAN__ -D\"__BYTE_ORDER__=1234\" -D\"_CALL_ELF=2\" -D__LONG_DOUBLE_128__"
%endif
%ifarch s390x
export ARCH_DEFINE="-D__s390x__ -D__LONG_DOUBLE_128__"
%endif
%ifarch %{ix86}
export ARCH_DEFINE="-D__i386__"
%endif
%ifarch %{arm}
export ARCH_DEFINE="-D__arm__ -D__ARMEL__ -D__ARM_EABI__"
%ifnarch armv5tel
export ARCH_DEFINE="$ARCH_DEFINE -D__ARM_PCS_VFP"
%endif
%endif
if [ -z "$ARCH_DEFINE" ]; then
  export ARCH_DEFINE="-D__%{_arch}__"
fi
export JAVA_HOME=%{_jvmdir}/java
pushd src/sdljava/native
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
make libsdljava_gfx.so CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd
pushd src/org/gljava/opengl/native
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd
pushd src/org/gljava/opengl/native/ftgl
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC"
popd
ant jar javadoc
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_jnidir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -m 644 lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_jnidir}/%{name}.jar
install -m 755 lib/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
pushd bin
rm runtest.sh
rm run-bsh.sh
for i in `ls -1 *.sh`; do
   sed -i -e 's|./runtest.sh|%{_bindir}/%{name}-runtest.sh|g' $i
   FN=`echo $i | awk 'BEGIN { FS="." }{ print $1 }'`
   install -m 755 $i $RPM_BUILD_ROOT%{_bindir}/%{name}-$FN.sh
done
popd
cp -a testdata $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s $(fc-match -f "%{file}" "sans") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arial.ttf
ln -s $(fc-match -f "%{file}" "sans:bold") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arialbd.ttf
ln -s $(fc-match -f "%{file}" "sans:italic") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/ariali.ttf
ln -s $(fc-match -f "%{file}" "sans:bold:italic") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/testdata/arialbi.ttf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sdljava-javadoc -f %{oreon_filedir}/sdljava-javadoc.list
%files -n sdljava-demo -f %{oreon_filedir}/sdljava-demo.list

%changelog

%autochangelog
