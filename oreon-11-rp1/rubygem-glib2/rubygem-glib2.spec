%global source0_hash f5f2a0c012271c75ee552bfd86c2535331e2ae642390cd2fa3e3a94bfd275115

%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	glib2

%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of GLib-2.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# F-19 %%_bindir/ruby wrapper pollutes environ, which makes
# g_spawn_async() test failure
Patch100:	rubygem-glib2-3.5.1-rubywrapper-pollutes-env.patch

Requires:	ruby(release)
# Explicitly require mri for g_spawn_async() test
BuildRequires:	gcc

BuildRequires:	%{_bindir}/ruby-mri
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(pkg-config)
BuildRequires:	rubygem(native-package-installer)
BuildRequires:	ruby-devel
BuildRequires:	glib2-devel
# For patch
#BuildRequires:	rubygem(rake-compiler)
## %%check
BuildRequires:	rubygem(test-unit)
Requires:	rubygems
# Ruby-GetText-Package support in glib2.rb
# Seems no longer needed
#Requires:	rubygem(gettext)
# If someone uses gnome2-win32-binary-downloader.rb, please explicitly
# require the following by yourself
#Requires:	rubygem(mechanize)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/GLib2 is a Ruby binding of GLib-2.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GLib development environment
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	ruby-devel
# mkmf-gnome2.rb
Requires:	rubygem(pkg-config)
Requires:	rubygem(native-package-installer)
# gnome2-raketask.rb
Requires:	rubygem(rake-compiler)
# Not needed
#Requires:	rubygem(cairo)
# Obsoletes / Provides
# ruby(%%{gem_name}-devel) Provides is for compatibility
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Patches and etc
%patch -P100 -p1

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# Make pkg-config devel dependency (not runtime)
sed -i \
	-e '\@pkg-config@s|add_\(runtime_\)*dependency|add_development_dependency|' \
	-e '\@native-package-installer@s|add_\(runtime_\)*dependency|add_development_dependency|' \
	%{gem_name}.gemspec \
	Rakefile

sed -i \
	-e '2a require "rubygems"\ngem "test-unit"\n' \
	test/run-test.rb

# shebang issue
find sample/ test/ -name \*.rb | xargs chmod 0644
grep -rl '#![ ]*/usr' sample/ test/ | \
	xargs chmod 0755

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install

# Move C extension library to some private directory
pushd .%{gem_instdir}

# create glib-test-init.rb
cat > lib/glib-test-init.rb <<EOF
\$VERBOSE = true
begin
	require 'rubygems'
	gem 'test-unit'
rescue LoadError
end
require 'test/unit'
EOF

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/

# Cleanups
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
pushd .%{gem_instdir}/

rm -f \
	Rakefile \
	extconf.rb \
	*gemspec \
	version.rb \
	test/test-*.rb \
	%{nil}
# Move the directory
chmod 0644 test/*rb
mv test/ lib/glib2/

popd
popd

%check
pushd .%{gem_instdir}

# Kill unneeded make process
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd

ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb

popd

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%doc	%{gem_instdir}/[A-Z]*

%{gem_instdir}/lib/glib2.rb
%{gem_instdir}/lib/glib-mkenums.rb
%dir %{gem_instdir}/lib/glib2
%{gem_instdir}/lib/glib2/date-time.rb
%{gem_instdir}/lib/glib2/deprecatable.rb
%{gem_instdir}/lib/glib2/deprecated.rb
%{gem_instdir}/lib/glib2/regex.rb
%{gem_instdir}/lib/glib2/time-zone.rb
%{gem_instdir}/lib/glib2/variant.rb
%{gem_instdir}/lib/glib2/variant-type.rb
%{gem_instdir}/lib/glib2/value.rb
%{gem_instdir}/lib/glib2/version.rb

%{gem_extdir_mri}/
%{gem_spec}

%files	devel
# Using pkg-config and mkmf, let's move mkmf-gnome2.rb into -devel
# gnome2-raketask.rb uses rake-compiler, so also put this into -devel
# Also install gliglib-test-init.rb
%{gem_instdir}/lib/glib-test-init.rb
%{gem_instdir}/lib/gnome2-raketask.rb
%{gem_instdir}/lib/mkmf-gnome*.rb
%dir	%{gem_instdir}/lib/gnome*/
%dir	%{gem_instdir}/lib/gnome*/rake/
%{gem_instdir}/lib/gnome*/rake/*.rb

# Needs these for test suite for other package
%{gem_instdir}/lib/glib2/test/

%{header_dir}/rbgcompat.h
%{header_dir}/rbglib.h
%{header_dir}/rbglibdeprecated.h
%{header_dir}/rbglib2conversions.h
%{header_dir}/rbgobject.h
%{header_dir}/rbgutil.h
%{header_dir}/rbgutil_list.h
%{header_dir}/rbgutildeprecated.h
%{header_dir}/glib-enum-types.h
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
%autochangelog
