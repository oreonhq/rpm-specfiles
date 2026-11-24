# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash abe94507c54cb18f872777b16bdca4aad32b1abdc4c52fe843f1c80fbdf992b8
%global source1_hash 5e97476b0a7692afb67e55f6f55792b818583ff1b5e6414adfed445d162e1759
%global source2_hash 6ad263d421f7ac46f3ca7053e0ef7dc500fe58c5eac5f97179bcd6a3a03dafe9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global	mainver		1.19.7

%global	baserelease		1
%global	prerpmver		%(echo "%{?prever}" | sed -e 's|\\.||g')

%global	gem_name	nokogiri

%undefine __brp_mangle_shebangs

Summary:	An HTML, XML, SAX, and Reader parser
Name:		rubygem-%{gem_name}
Version:	%{mainver}
Release:	%{?prever:0.}%{baserelease}%{?prever:.%{prerpmver}}%{?dist}

License:	MIT AND Apache-2.0
Provides:	bundled(gumbo-parser) = 0.10.1

URL:		https://nokogiri.org
Source0:	https://rubygems.org/gems/%{gem_name}-%{mainver}%{?prever}.gem
Source1:	rubygem-%{gem_name}-%{version}%{?prever}-full.tar.gz
Source2:	nokogiri-create-full-tarball.sh
Patch0:	%{name}-1.11.0.rc4-shutdown-libxml2-warning.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:	ruby(release)
BuildRequires:	ruby(rubygems)
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(minitest-mock)
%if ! 0%{?rhel} && ! 0%{?oreon}
BuildRequires:	rubygem(rubyzip)
%endif
BuildRequires:	rubygems-devel
Obsoletes:		ruby-%{gem_name} <= 1.5.2-2
BuildRequires:	glibc-all-langpacks
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	ruby-devel
BuildRequires:	gtest-devel
BuildRequires:	rubygem(racc)

%description
Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath support.

Nokogiri also features an Hpricot compatibility layer to help ease the change
to using correct CSS and XPath.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	-n ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Requires:	%{name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description	-n ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%global	version	%{mainver}%{?prever}

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%setup -q -n %{gem_name}-%{version} -a 1
cp -a %{gem_name}-%{version}/{.,*} .
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1

sed -i \
	-e 's|, "ports/archives/[^"][^"]*"||g' \
	-e 's|, "patches/[^"][^"]*"||g' \
	%{gem_name}-%{version}.gemspec
rm -rf \
	ports \
	patches \
	%{nil}

sed -i -e '\@mini_portile@d' %{gem_name}-%{version}.gemspec

sed -i \
	ext/nokogiri/extconf.rb \
	-e "s@^\(def process_recipe.*\)\$@\1 ; return true@" \
	-e "s@^\([ \t]*append_cppflags\).*gumbo.*\$@\1(\"-I$(pwd)/gumbo-parser/src\")@" \
	-e "\@libs.*gumbo@s@File\.join.*@\"$(pwd)/gumbo-parser/src/libgumbo.a\"@" \
	-e "\@LIBPATH.*gumbo@s|^\(.*\)\$|# \1|" \
	%{nil}

sed -i \
	gumbo-parser/src/char_ref.c \
	-e '\@^#line [0-9]@s|^\(.*\)$|// \1|'

sed -i \
	gumbo-parser/src/Makefile \
	-e 's|^\(CFLAGS.*=.*\)$|\1 -fPIC|'

sed -i \
	gumbo-parser/Makefile \
	-e '\@CFLAGS.*:=@s|^\(.*\)$|\1 %build_cflags|' \
	-e '\@CXXFLAGS.*:=@s|^\(.*\)$|\1 %build_cflags|' \
	-e 's|-std=c++11|-std=c++17|' \
	-e '\@gtest_lib.*:=@s|googletest/make/gtest_main.a|%{_libdir}/libgtest_main.so %{_libdir}/libgtest.so|' \
	%{nil}

%build
env LANG=C.UTF-8 gem build %{gem_name}-%{version}.gemspec

export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

%set_build_flags
pushd gumbo-parser/src/
make libgumbo.a
popd

%gem_install

chmod 0644 .%{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem

find .%{gem_instdir}/lib/ -name '*.jar' -delete
rm -rf .%{gem_instdir}/ext/java

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

cp -a ./gumbo-parser  %{buildroot}%{gem_instdir}/

find %{buildroot} -name \*.orig_\* | xargs rm -vf

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

for f in $(find %{buildroot}%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

cp -p [A-Z]* %{buildroot}%{gem_instdir}/

pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile* \
	Rakefile \
	Vagrantfile \
	dependencies.yml \
	ext \
	*gemspec \
	patches \
	ports \
	%{nil}
pushd gumbo-parser
find . -type f | \
	grep -v CHANGES.md | \
	grep -v THANKS | \
	grep -v README.md | \
	xargs rm -f

popd
rm -f %{buildroot}%{gem_cache}

%check
cd gumbo-parser
make build/run_tests %{?_smp_mflags}
make check
cd ..

export TZ="Asia/Tokyo"
LANG=C.UTF-8

cp -a test/ ./%{gem_instdir}
pushd ./%{gem_instdir}

sed -i test/helper.rb \
	-e '\@^  require.*simplecov@,\@^  end$@s|^|#|'

sed -i '/require..minitest.reporters./ s/^/#/' test/helper.rb
sed -i '/Minitest::Reporters/ s/^/#/' test/helper.rb

%ifarch ppc64le
export NOKOGIRI_TEST_GC_LEVEL=major
%endif
%ifarch s390x
if pkg-config --atleast-version 3.2 ruby ; then
export NOKOGIRI_TEST_GC_LEVEL=major
fi
%endif

sed -i test/xml/test_schema.rb \
	-e '\@describe.*CVE-2020-26247@N;s|unless Nokogiri|unless false \&\& Nokogiri|'

env \
	RUBYLIB=".:lib:test:%{buildroot}%{gem_extdir_mri}" \
	ruby \
	-e \
	"require 'test/helper' ; Dir.glob('test/**/test_*.rb'){|f| require f}" || \
	exit 1

for f in $SKIPTEST
do
	mv $f.skip $f
done

popd

%files
%{_bindir}/%{gem_name}
%{gem_extdir_mri}/

%dir	%{gem_instdir}/
%license	%{gem_instdir}/LICENSE*.md
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%{gem_instdir}/bin/
%{gem_instdir}/lib/

%dir	%{gem_instdir}/gumbo-parser
%dir	%{gem_instdir}/gumbo-parser/src
%doc	%{gem_instdir}/gumbo-parser/[A-Z]*
%license	%{gem_instdir}/gumbo-parser/src/README.md

%{gem_dir}/specifications/%{gem_name}-%{mainver}%{?prever}.gemspec

%files	doc
%defattr(-,root,root,-)
%doc	%{gem_instdir}/CODE_OF_CONDUCT.md
%doc	%{gem_instdir}/CONTRIBUTING.md
%doc	%{gem_instdir}/ROADMAP.md
%doc	%{gem_instdir}/SECURITY.md
%doc	%{gem_dir}/doc/%{gem_name}-%{mainver}%{?prever}/

%changelog
%autochangelog
