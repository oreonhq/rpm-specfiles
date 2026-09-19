%global source0_hash 5f524962c588087ae3642b45628c3aae147bf8c148ab1b1312578ece599b34f9

%global gem_name hoe
%undefine _changelog_trimtime

Summary:    	Hoe is a simple rake/rubygems helper for project Rakefiles
Name:       	rubygem-%{gem_name}
Version:    	4.6.1
Release:    	1%{?dist}
# SPDX confirmed
License:    	MIT
URL:        	https://github.com/seattlerb/hoe
Source0:    	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Rescue Hoe.spec task when Manifest.txt
# seattlerb-Bugs-28571
Patch0:		rubygem-hoe-3.0.6-rescue-missing-Manifest.patch
# Workaround for "Fedora" ruby 2.7 psych
# ruby -e 'require "psych"; gem "psych"; require "psych";' produces 
# /usr/share/gems/gems/psych-3.1.0/lib/psych/parser.rb:34:in `<class:Parser>': 
# superclass mismatch for class Mark (TypeError)
Patch1:		rubygem-hoe-3.21.0-always-search-gem-for-psych.patch

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
# %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(rake)
BuildArch:  	noarch
Provides:   	rubygem(%{gem_name}) = %{version}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps generate
rubygems and includes a dynamic plug-in system allowing for easy
extensibility. Hoe ships with plug-ins for all your usual project
tasks including rdoc generation, testing, packaging, and deployment.
Plug-ins Provided:
* Hoe::Clean
* Hoe::Debug
* Hoe::Deps
* Hoe::Flay
* Hoe::Flog
* Hoe::Inline
* Hoe::Package
* Hoe::Publish
* Hoe::RCov
* Hoe::Signing
* Hoe::Test
See class rdoc for help. Hint: ri Hoe

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Patches
%patch -P0 -p0
%patch -P1 -p1

# Allow RubyInline 3.8.4
sed -i -e '/RubyInline/s|~> 3\.9|>= 3.8.4|' \
	lib/hoe/inline.rb

# Allow rake-compiler 1.0 and above
sed -i -e '/rake-compiler/s|~> 1\.0|>= 1.0|' \
	lib/hoe/compiler.rb

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

pushd .%{gem_instdir}
# Umm...
%_fixperms .

popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{_prefix}/* \
	%{buildroot}%{_prefix}/

chmod 0644 %{buildroot}%{gem_dir}/cache/*gem

find %{buildroot}/%{gem_instdir}/bin -type f | xargs chmod 0755
find %{buildroot}/%{_bindir} -type f | xargs chmod 0755

chmod 0755 %{buildroot}/%{gem_instdir}/template/bin/file_name.erb
# Don't remove template files
#rm -f %{buildroot}/%{gem_instdir}/template/.autotest.erb

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}

# Save original Rakefile
sed -i.isolate -e \
	'/Hoe\.plugin :isolate/d' Rakefile
# Make sure that hoe currently building are loaded
export RUBYLIB=$(pwd)/lib

unset SOURCE_DATE_EPOCH
rake test -v --trace

mv Rakefile{.isolate,}
popd

%files
%{_bindir}/sow
%dir %{gem_instdir}/
%{gem_instdir}/bin/
%{gem_instdir}/lib/
%{gem_instdir}/template/
%{gem_spec}
%doc %{gem_instdir}/[A-Z]*

%files	doc
%{gem_docdir}

%changelog
%autochangelog
