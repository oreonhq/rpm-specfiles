%global source0_hash 553a02566a199455ac8e87542ff485cfed3bcb31def0921fdc6216fef542e231
Summary:        Java bindings for BLAS
Name: jblas
Version: 1.2.5
Release:        1%{?dist}
License: BSD-3-Clause
URL: http://jblas.org
ExcludeArch: %{ix86}
Source0:        https://github.com/jblas-project/jblas/archive/jblas-%{version}.tar.gz
Patch0: 0001-Try-to-load-libraries-directly-on-Linux.patch
Patch1: 0001-Stop-using-javah.patch
Patch2: 0001-options-check-for-dynamic-libs-had-a-typo.patch
Patch3: 0001-javadoc-add-summaries-to-tables.patch
Patch4: 0002-Fix-path-to-stylesheet-and-overview.patch
%global blaslib openblas
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  gcc-gfortran
BuildRequires:  java-25-devel
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  junit
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem-RedCloth
BuildRequires:  rubygem-ffi
BuildRequires:  rubygem-fog-json
BuildRequires:  rubygem-hitimes
BuildRequires:  rubygem-nokogiri
BuildRequires:  rubygem-posix-spawn
BuildRequires:  rubygem-redcarpet
# /oreon:deps
%description
Wraps BLAS (e.g. OpenBLAS) using generated code through JNI. Allows Java
programs to use the full power of BLAS/LAPACK through a convenient interface.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch:      noarch
%description javadoc
This package contains the API documentation for %{name}.

%prep

%autosetup -p1 -n %{name}-%{name}-%{version}
rm -rf src/main/resources/lib/static

# turn off javadoc warnings, we don't care
sed -i.bak -r 's/overview=/additionalparam="-Xdoclint:none" \0/' build.xml

sed -i.bak -r 's/-SNAPSHOT//' build.xml

ln -s pom.xml %{name}.pom

%mvn_file org.jblas:jblas %{name}

# [javac] error: Source option 5 is no longer supported. Use 6 or later.
# [javac] error: Target option 1.5 is no longer supported. Use 1.6 or later.
sed -r -i 's/source="1.7"/source="11"/g; s/target="1.7"/target="11"/g; s/compiler="javac1.7"//g' build.xml

%build

libdir="$(cd "/usr/lib/$(gcc -print-multi-os-directory)"; pwd)"
export LC_ALL=C.UTF-8
export JAVA_HOME=$(java -XshowSettings:properties -version |& sed -r -n 's/.*java.home = (.*)/\1/p')
./configure --libpath="$libdir" --libs=%{blaslib} --dynamic-libs
%make_build CFLAGS="%{optflags} -fPIC"
ant minimal-jar
ln -s jblas-minimal-*.jar %{name}.jar
ant javadoc
rm -rf javadoc/src-html
%mvn_artifact %{name}.pom %{name}.jar
%install
%mvn_install -J javadoc
shopt -s globstar
install -pm755 src/main/resources/lib/dynamic/Linux/**/libjblas.so \
        -Dt %buildroot%{_libdir}/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jblas-javadoc -f %{oreon_filedir}/jblas-javadoc.list

%changelog

%autochangelog
