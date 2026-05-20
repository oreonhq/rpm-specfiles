# Exclude automatically generated requires on java interpreter which is not
# owned by any package
%global __requires_exclude ^%{_jvmdir}/jre
# Generated list of bundled packages
%global _local_file_attrs local_generator
%global __local_generator_provides cat %{_builddir}/%{buildsubdir}/bundled-provides.txt
%global __local_generator_path ^%{metadataPath}/.*$
%global debug_package %{nil}
%global javaHomePath %{_jvmdir}/jre-25-openjdk
%global mavenHomePath %{_datadir}/%{name}
%global metadataPath %{mavenHomePath}/maven-metadata
%global artifactsPath %{_datadir}
%global launchersPath %{_libexecdir}/%{name}

Name:           javapackages-bootstrap
Version:        1.27.0
Release:        %autorelease
Summary:        A means of bootstrapping Java Packages Tools
# For detailed info see the file javapackages-bootstrap-PACKAGE-LICENSING
License:        Apache-1.1 AND Apache-2.0 AND (Apache-2.0 OR EPL-2.0) AND (Apache-2.0 OR LGPL-2.0-or-later) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CPL-1.0 AND EPL-1.0 AND EPL-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND LicenseRef-Fedora-Public-Domain AND MIT AND Plexus AND SMLNJ AND Saxpath AND xpp
URL:            https://github.com/fedora-java/javapackages-bootstrap
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:         https://github.com/fedora-java/javapackages-bootstrap/releases/download/%{version}/javapackages-bootstrap-%{version}.tar.zst
# License breakdown
Source:         javapackages-bootstrap-PACKAGE-LICENSING
# 132 *.tar.zst component archives ship in Fedora SRPM (not on upstream GitHub release).
# %%prep unpacks them from Source200; or run fetch-jpb-vendor-tarballs.sh for local copies.
Source200:      https://kojipkgs.fedoraproject.org/pub/fedora/linux/releases/44/Everything/source/tree/Packages/j/javapackages-bootstrap-%{version}-2.fc44.src.rpm

Patch:          0001-Switch-Dola-to-Lua-5.5.patch

BuildRequires:  byaccj
BuildRequires:  java-25-openjdk-devel
BuildRequires:  jurand
Requires:       bash
Requires:       coreutils
Requires:       java-25-openjdk-devel
Requires:       javapackages-common
Requires:       lujavrite
Requires:       procps-ng

%description
In a nutshell, Java Packages Bootstrap (JPB) is a standalone build of all Java
software packages that are required for Java Packages Tools (JPT) to work.

In order to achieve reliable and reproducible builds of Java packages while
meeting Fedora policy that requires everything to be built from source, without
using prebuilt binary artifacts, it is necessary to build the packages in a
well-defined, acyclic order. Dependency cycles between packages are the biggest
obstacle to achieving this goal and JPT is the biggest offender -- it requires
more than a hundred of Java packages, all of which in turn build-require JPT.

JPB comes with a solution to this problem -- it builds everything that JPT needs
to work, without reliance on any Java software other than OpenJDK. JPT can
depend on JPB for everything, without depending on any other Java packages. For
example, JPB contains embedded version of XMvn, removing dependency of JPT on
XMvn, allowing JPT to be used before one builds XMvn package.

%prep
%autosetup -p1
mkdir -p archive
if ls archive/*.tar.zst >/dev/null 2>&1; then
  :
elif test -f %{SOURCE200}; then
  rpm2cpio %{SOURCE200} | (cd archive && cpio -idmv '*.tar.zst')
else
  echo "No archive/*.tar.zst and missing %{SOURCE200}" >&2
  exit 1
fi
./downstream.sh prep-from-archive

%build
JAVA_HOME=%{javaHomePath} ./mbi.sh build -parallel

%install
JAVA_HOME=%{javaHomePath} ./mbi.sh dist \
  -javaCmdPath=%{javaHomePath}/bin/java \
  -basePackageName=%{name} \
  -installRoot=%{buildroot} \
  -mavenHomePath=%{mavenHomePath} \
  -metadataPath=%{metadataPath} \
  -artifactsPath=%{artifactsPath} \
  -launchersPath=%{launchersPath} \
  -licensesPath=%{_licensedir}/%{name} \

install -D -p -m 644 downstream/dola/dola-bsx/src/main/lua/dola-bsx.lua %{buildroot}%{_rpmluadir}/%{name}-dola-bsx.lua
install -D -p -m 644 downstream/dola/dola-dbs/src/main/lua/dola-dbs.lua %{buildroot}%{_rpmluadir}/%{name}-dola-dbs.lua
install -D -p -m 644 downstream/dola/dola-generator/src/main/lua/dola-generator.lua %{buildroot}%{_rpmluadir}/%{name}-dola-generator.lua
install -D -p -m 644 downstream/dola/dola-bsx/src/main/rpm/macros.dola-bsx %{buildroot}%{_rpmmacrodir}/macros.jpb-dola-bsx
install -D -p -m 644 downstream/dola/dola-dbs/src/main/rpm/macros.dola-dbs %{buildroot}%{_rpmmacrodir}/macros.zzz-jpb-dola-dbs
install -D -p -m 644 downstream/dola/dola-generator/src/main/rpm/macros.dola-generator %{buildroot}%{_rpmmacrodir}/macros.jpb-dola-generator
install -D -p -m 644 downstream/dola/dola-generator/src/main/rpm/macros.dola-generator-etc %{buildroot}%{_sysconfdir}/rpm/macros.jpb-dola-generator-etc
install -D -p -m 644 downstream/dola/dola-generator/src/main/rpm/dolagen.attr %{buildroot}%{_fileattrsdir}/jpbdolagen.attr
install -D -p -m 644 downstream/dola/dola-bsx/src/main/conf/dola-bsx.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/00-dola-bsx.conf
install -D -p -m 644 downstream/dola/dola-dbs/src/main/conf/dola-dbs.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/04-dola-dbs.conf
install -D -p -m 644 downstream/dola/dola-generator/src/main/conf/dola-generator.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/03-dola-generator.conf
install -D -p -m 644 downstream/dola/dola-bsx-api/src/main/conf/dola-bsx-api.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/02-dola-bsx-api.conf

echo '
%%__xmvngen_debug 1
%%__xmvngen_libjvm %{javaHomePath}/lib/server/libjvm.so
%%__xmvngen_classpath %{artifactsPath}/%{name}/xmvn-generator.jar:%{artifactsPath}/%{name}/asm.jar:%{artifactsPath}/%{name}/commons-compress.jar:%{artifactsPath}/%{name}/commons-io.jar:%{artifactsPath}/%{name}/xmvn-mojo.jar:%{artifactsPath}/%{name}/kojan-xml.jar:%{artifactsPath}/%{name}/maven-model.jar:%{artifactsPath}/%{name}/plexus-utils.jar
%%__xmvngen_provides_generators org.fedoraproject.xmvn.generator.filesystem.FilesystemGeneratorFactory org.fedoraproject.xmvn.generator.jpscript.JPackageScriptGeneratorFactory org.fedoraproject.xmvn.generator.jpms.JPMSGeneratorFactory org.fedoraproject.xmvn.generator.maven.MavenGeneratorFactory
%%__xmvngen_requires_generators org.fedoraproject.xmvn.generator.filesystem.FilesystemGeneratorFactory org.fedoraproject.xmvn.generator.jpscript.JPackageScriptGeneratorFactory org.fedoraproject.xmvn.generator.maven.MavenGeneratorFactory
%%__xmvngen_post_install_hooks org.fedoraproject.xmvn.generator.transformer.TransformerHookFactory
%%jpb_env PATH=/usr/libexec/javapackages-bootstrap:%{javaHomePath}/bin:$PATH
%%java_home %{javaHomePath}
' >%{buildroot}%{_rpmmacrodir}/macros.jpbgen

# Dynamically generate bundled Provides
./downstream.sh bundled-provides >bundled-provides.txt

%check
%{buildroot}%{launchersPath}/xmvn --version

%files
%{mavenHomePath}
%{metadataPath}/*
%{artifactsPath}/*
%{launchersPath}/*
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*
%{_javaconfdir}/%{name}

%license %{_licensedir}/%{name}
%doc README.md
%doc AUTHORS

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.27.0-1
- Prepare for Oreon 11 (RP1)
