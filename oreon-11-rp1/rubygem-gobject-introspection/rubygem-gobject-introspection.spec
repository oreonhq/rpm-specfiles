%global source0_hash ed6e8d43cb17b68c2900a0245fc1562f21623c724e4be6e3237dd43265e0bfed
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	gobject-introspection
%global	gem_so_name	gobject_introspection
%global	glib_min_ver	3.1.8
%undefine        _changelog_trimtime
Summary:        Ruby binding of GObjectIntrospection
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	ruby(rubygems) 
Requires:	ruby
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GObjectIntrospection is a Ruby binding of 
GObjectIntrospection.

%package	devel
Summary:	Ruby/GdkPixbuf2 development environment
Requires:	%{name}%{?isa} = %{version}-%{release}
Requires:	ruby-devel%{?isa}
Requires:	rubygem-glib2-devel%{?isa}
Requires:	gobject-introspection-devel%{?isa}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Patches

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# https://github.com/ruby-gnome/ruby-gnome/issues/1685
# GLib 2.84 deprecates g_type_class_ref

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror-implicit-function-declaration'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
sed -i test/run-test.rb -e ':loop; N; $!b loop; s|true,\n|true,|'
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gobject-introspection-devel -f %{oreon_filedir}/rubygem-gobject-introspection-devel.list
%files -n rubygem-gobject-introspection-doc -f %{oreon_filedir}/rubygem-gobject-introspection-doc.list

%changelog

%autochangelog
