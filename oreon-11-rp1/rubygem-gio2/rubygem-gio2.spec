%global source0_hash 83d575cb78aae746ee916f3b3ac09edba195ec2023a8cca3a309934e7fb420cf
%global	header_dir	%{ruby_vendorarchdir}
%global	glibminver	3.0.9
%global	obsoleteevr	0.90.7-1.999
%global	gem_name	gio2
%undefine        _changelog_trimtime
Summary:        Ruby binding of gio-2.0.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	gio2-%{version}-test-missing-files.tar.gz
Source2:	gio2-create-missing-test-files.sh
Requires:	ruby(release)
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}
Obsoletes:		ruby-%{gem_name} < %{version}-%{release}
Provides:		ruby-%{gem_name} = %{version}-%{release}
Provides:		ruby(%{gem_name}) = %{version}-%{release}
Obsoletes:		ruby-%{gem_name}-devel < %{obsoleteevr}
Obsoletes:		rubygem-gio2-devel < 2.2.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(fiddle)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gobject-introspection-devel
BuildRequires:  rubygems-devel
BuildRequires:  shared-mime-info
# /oreon:deps
%description
Ruby/GIO2 is a Ruby binding of gio-2.0.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GIO2 development environment
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-devel
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# fiddle is in default gem
sed -i -e '\@dependency.*fiddle@d' %{gem_name}-%{version}.gemspec

#%%patch0 -p1

# Fix up Rakefile for "gnome2-raketask" requirement
sed -i -e "/require.*gnome2-raketask/s|^\(.*\)|begin\n  \1\nrescue LoadError\n  require 'rubygems'\n  require 'gnome2-raketask'\nend\n|" \
	Rakefile

# Fix up test/load-test.rb
sed -i -e "/glib-test-init/s|^.*$|require 'glib-test-init'|" \
	test/run-test.rb

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install
find . -name \*.gem | xargs chmod 0644
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/
pushd %{buildroot}
rm -rf .%{gem_instdir}/{ext/,test/}
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
tar xf %{SOURCE1}
mkdir test || :
cp -a gio2/test/* test
cd ..
cp -a %{gem_name}-%{version} %{gem_name}
cd -
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
sed -i test/test-resolver.rb -e 's|\(test_lookup_records_async\)$|\1 ; omit "network needed"|'
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -rrubygems -Ilib:test:%{buildroot}%{gem_extdir_mri} test/run-test.rb || \
	false
cd ..
: unlink %{gem_name}
cd -
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gio2-doc -f %{oreon_filedir}/rubygem-gio2-doc.list
%files -n rubygem-gio2-devel -f %{oreon_filedir}/rubygem-gio2-devel.list

%changelog

%autochangelog
