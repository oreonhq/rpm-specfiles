%global source0_hash none

%global	mainver		1.19.1
#%%global	prever		.rc4

%global	baserelease		1
%global	prerpmver		%(echo "%{?prever}" | sed -e 's|\\.||g')

%global	gem_name	nokogiri

%undefine __brp_mangle_shebangs

Summary:	An HTML, XML, SAX, and Reader parser
Name:		rubygem-%{gem_name}
Version:	%{mainver}
Release:	%{?prever:0.}%{baserelease}%{?prever:.%{prerpmver}}%{?dist}

# SPDX confirmed
# MIT: see LICENSE.md
# Apache-2.0
#  1.12.0 bundles forked and modified gumbo -
#  see gumbo-parser/src/attribute.c and ext/nokogiri/gumbo.c
#  also lib/nokogiri/html5 is licensed under ASL 2.0
License:	MIT AND Apache-2.0
Provides:	bundled(gumbo-parser) = 0.10.1

URL:		https://nokogiri.org
Source0:	https://rubygems.org/gems/%{gem_name}-%{mainver}%{?prever}.gem
# %%{SOURCE2} %%{name} %%{version}
Source1:	https://github.com/sparklemotion/%{gem_name}/archive/refs/tags/v%{version}%{?prever}.tar.gz#/rubygem-%{gem_name}-%{version}%{?prever}-full.tar.gz
# Shut down libxml2 version unmatching warning
Patch0:	%{name}-1.11.0.rc4-shutdown-libxml2-warning.patch
BuildRequires:	ruby(release)
BuildRequires:	ruby(rubygems)
##
## For %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(minitest-mock)
%if !0%{?rhel}
# For test/xml/test_document_encoding.rb
# Drop rubygem(rubyzip) build dependency in RHEL
BuildRequires:	rubygem(rubyzip)
%endif
BuildRequires:	rubygems-devel
Obsoletes:		ruby-%{gem_name} <= 1.5.2-2
#BuildRequires:	ruby(racc)
##
# test suite uses EUC-JP, SHIFT-JIS, etc
BuildRequires:	glibc-all-langpacks
## Others
BuildRequires:	gcc
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	ruby-devel
# ruby27 needs this explicitly
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{gem_name}-%{version} -a 1
cp -a %{gem_name}-%{version}/{.,*} .
mv ../%{gem_name}-%{version}.gemspec .

# patches
%patch -P0 -p1

# remove bundled external libraries
sed -i \
	-e 's|, "ports/archives/[^"][^"]*"||g' \
	-e 's|, "patches/[^"][^"]*"||g' \
	%{gem_name}-%{version}.gemspec
# Make sure gem build will complain later if the previous regex is not enough.
rm -rf \
	ports \
	patches \
	%{nil}

# Actually not needed when using system libraries
sed -i -e '\@mini_portile@d' %{gem_name}-%{version}.gemspec

# Don't use mini_portile2, but build libgumbo.a first and
# tell extconf.rb the path to the archive
sed -i \
	ext/nokogiri/extconf.rb \
	-e "s@^\(def process_recipe.*\)\$@\1 ; return true@" \
	-e "s@^\([ \t]*append_cppflags\).*gumbo.*\$@\1(\"-I$(pwd)/gumbo-parser/src\")@" \
	-e "\@libs.*gumbo@s@File\.join.*@\"$(pwd)/gumbo-parser/src/libgumbo.a\"@" \
	-e "\@LIBPATH.*gumbo@s|^\(.*\)\$|# \1|" \
	%{nil}

# #line directive can confuse debuginfo, removing for now
sed -i \
	gumbo-parser/src/char_ref.c \
	-e '\@^#line [0-9]@s|^\(.*\)$|// \1|'

# Compile libgumbo.a with -fPIC
sed -i \
	gumbo-parser/src/Makefile \
	-e 's|^\(CFLAGS.*=.*\)$|\1 -fPIC|'

%build
# Ummm...
env LANG=C.UTF-8 gem build %{gem_name}-%{version}.gemspec

# 1.6.0 needs this
export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

%set_build_flags
# First build libgumbo.a
pushd gumbo-parser/src/
make libgumbo.a
popd

%gem_install

# Permission
chmod 0644 .%{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem

# Remove precompiled Java .jar file
find .%{gem_instdir}/lib/ -name '*.jar' -delete
# For now remove JRuby support
rm -rf .%{gem_instdir}/ext/java


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

# Also first copy these, clean up later
cp -a ./gumbo-parser  %{buildroot}%{gem_instdir}/

# Remove backup file
find %{buildroot} -name \*.orig_\* | xargs rm -vf

# move arch dependent files to %%gem_extdir
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd


# move bin/ files
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

# remove all shebang
for f in $(find %{buildroot}%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

# Copy document files from full source
cp -p [A-Z]* %{buildroot}%{gem_instdir}/

# cleanups
# Remove bundled gumbo parser
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
# Ah....
# test_exslt(TestXsltTransforms) [./test/test_xslt_transforms.rb:93]
# fails without TZ on sparc
export TZ="Asia/Tokyo"
#???
LANG=C.UTF-8

# Copy test files from full tarball
cp -a test/ ./%{gem_instdir}
pushd ./%{gem_instdir}

# Remove unneeded simplecov coverage test
sed -i test/helper.rb \
	-e '\@^  require.*simplecov@,\@^  end$@s|^|#|'

# Remove minitest-reporters. It does not provide any additional value while
# it blows up the dependency chain.
sed -i '/require..minitest.reporters./ s/^/#/' test/helper.rb
sed -i '/Minitest::Reporters/ s/^/#/' test/helper.rb

# PPC64LE with ruby3.1 does not seem to support GC.compact
%ifarch ppc64le
export NOKOGIRI_TEST_GC_LEVEL=major
%endif
%ifarch s390x
# With ruby 3.2 GC_LEVEL=compact seems to cause segfault:
# change to major for now
if pkg-config --atleast-version 3.2 ruby ; then
export NOKOGIRI_TEST_GC_LEVEL=major
fi
%endif

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{mainver}-1
- Prepare for Oreon 11 (RP1)
