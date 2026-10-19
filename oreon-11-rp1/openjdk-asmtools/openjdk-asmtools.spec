%global source0_hash 0a5bcf80f3fe1afe13d9c304c2fc9712b8b539061482fc134bd9b9bddd35e377
%global major 9.0
%global minor b12.ea.eb1979669
Name:           openjdk-asmtools
Version:        %{major}.0.%{minor}
Release:        1%{?dist}
Summary:        Set of tools used to assemble / disassemble proper and improper Java .class files
License:        GPL-2.0-or-later
URL:            https://github.com/openjdk/asmtools
Source0:        %{major}-%{minor}.tar.gz
Source1:        openjdk-asmtools.in
Source2:        openjdk-asmtools.1
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-headless
Requires:       javapackages-tools
Requires:       javapackages-tools
# oreon:deps
BuildRequires:  (java-21-openjdk-devel or java-25-devel or java-latest-openjdk-devel)
BuildRequires:  junit5
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-local-openjdk25
# /oreon:deps
%description
AsmTools helps develop tools to create proper and improper Java .class files.
Aids various Java .class based testing and OpenJDK development applications.
Asmtools supports latest class file formats, in lock-step with JDK development.
AsmTools consist of a set of (Java class file) assembler/dis-assemblers:
* Jasm/Jdis:
An assembler language to provide Java-like declaration of member signatures,
providing Java VM specification compliant mnemonics for byte-code instructions.
* JCod/JDec:
An assembler language to provide byte-code containers of class-file constructs.

%package        javadoc
Summary:        Javadoc for %{name}
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#This is commented till the version on the master branch is released
%autosetup -n asmtools-upstream
cd maven
sed -i "s|ln -sv|cp -r|g" mvngen.sh
sh mvngen.sh
#%%pom_remove_plugin :maven-javadoc-plugin
#%%pom_remove_plugin :maven-source-plugin
#%%pom_remove_plugin :maven-gpg-plugin
sed "s/<addClasspath.*//" -i pom.xml
sed "s/<<mainClass.*//" -i pom.xml

%build

cd maven
xmvn -version
%mvn_build --xmvn-javadoc
%install
rm -rf $RPM_BUILD_ROOT
pushd maven
%mvn_install
popd
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
for launcher in "" "-jasm" "-jdis" "-jcoder" "-jdec" "-jcdec"; do
  switch=`echo $launcher |sed "s/-//"`
  cat %{SOURCE1} | sed "s/@SCD@/$switch/"  > $RPM_BUILD_ROOT%{_bindir}/%{name}$launcher
done
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openjdk-asmtools-javadoc -f %{oreon_filedir}/openjdk-asmtools-javadoc.list

%changelog

%autochangelog
