%global source0_hash 831d605e037587840a51426ccca3bf2aa5d74fe98a8760023d0cbb1cba86901b
%global	gem_name	syck
Summary:        Gemified version of Syck from Ruby's stdlib
Name:		rubygem-%{gem_name}
Version:	1.5.1.1
Release:        1%{?dist}
License:	MIT
URL:		http://github.com/tenderlove/syck/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A gemified version of Syck from Ruby's stdlib.  
Syck has been removed from Ruby's stdlib, and this gem is 
meant to bridge the gap for people that haven't
updated their YAML yet.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Kill syck.bundle
rm -f lib/syck.bundle
sed -i -e \
	's|"lib/syck.bundle",||' \
	%{gem_name}-%{version}.gemspec

# Kill #line for debuginfo rpm generation
sed -i -e '/^#line/d' \
	ext/syck/*.{c,h}

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}
rm -f .%{gem_cache}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
pushd .%{gem_instdir}
rm -rf \
    %{gem_name}.gemspec \
    Gemfile* \
    Rakefile \
    ext/ \
    test/ \
    %{nil}
popd
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
cat > test/helper.rb <<EOF
require 'test/unit'
require 'syck'
EOF
ruby \
	-Ilib:test:.:%{buildroot}%{gem_extdir_mri} \
	-Ilib:test:. \
	-e 'Dir.glob( "test/test_*.rb" ).sort.each {|f| require f }' \
    %{nil}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-syck-doc -f %{oreon_filedir}/rubygem-syck-doc.list

%changelog

%autochangelog
