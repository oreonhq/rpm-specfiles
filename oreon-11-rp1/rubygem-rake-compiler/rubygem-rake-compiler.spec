%global source0_hash 47ea05125006271abbe55763f8f3cff2a17cc85bd81aa02849141a5f46e6da18

%global	gem_name	rake-compiler

%undefine       _changelog_trimtime

Summary:	Rake-based Ruby C Extension task generator
Name:		rubygem-%{gem_name}
Version:	1.3.1
Release:	2%{?dist}
# SPDX confirmed
License:	MIT
URL:		https://github.com/rake-compiler/rake-compiler
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	%{gem_name}-create-missing-test-files.sh

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	ruby(rubygems) >= 1.3.5
BuildRequires:	rubygems-devel
# %%check
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(cucumber)
BuildRequires:	rubygem(rspec) >= 3
# cucumber test needs ruby.h header and compiler
BuildRequires:	gcc
BuildRequires:	ruby-devel
Requires:	ruby(rubygems) >= 1.3.5
Requires:	rubygem(rake) >= 0.8.3
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
rake-compiler aims to help Gem developers while dealing with
Ruby C extensions, simplifiying the code and reducing the duplication.

It follows *convention over configuration* and set an standarized
structure to build and package C extensions in your gems.

This is the result of expriences dealing with several Gems 
that required native extensions across platforms and different 
user configurations where details like portability and 
clarity of code were lacking. 

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
mv ../%{gem_name}-%{version}.gemspec .

# rpmlint cosmetic
find ./lib/rake -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# be_true -> be_truthy, be_false -> be_falsey
grep -rl be_true  features/ | xargs sed -i 's|be_true|be_truthy|'
grep -rl be_false features/ | xargs sed -i 's|be_false|be_falsey|'

# Don't strip binary for default. Also kill unneeded "-pipe" from LDFLAGS
sed -i tasks/bin/cross-ruby.rake \
	-e '\@LDFLAGS=@d'

# Cucumber 7 change
sed -i cucumber.yml -e "s|~@java|'not @java'|"

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
    Gemfile \
    Rakefile \
    appveyor.yml \
    cucumber.yml \
    features/ \
    spec/ \
    tasks/ \
    tmp/ \
    %{nil}
popd

%check
rm -rf .%{gem_instdir}/spec
cp -a spec/ .%{gem_instdir}/

pushd .%{gem_instdir}
ruby -Ilib -S rspec spec/

export CUCUMBER_PUBLISH_QUIET=true
ruby -Ilib -S cucumber
popd

%files
%{_bindir}/rake-compiler

%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History.md

%{gem_instdir}/bin/
%{gem_libdir}

%{gem_spec}

%files doc
%{gem_docdir}

%changelog
%autochangelog
