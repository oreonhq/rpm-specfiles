%global source0_hash 27f782c96087d080289e015c2b9d2f651d36df068c3e9dcd7cd43a03a7bc882a

%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	gdk3
%global	glib_min_ver	3.0.8

%undefine        _changelog_trimtime

# Planned for F-20+ only
Summary:	Ruby binding of GDK-3.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}

# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/gdk3/COPYING.LIB
# Renamed to avoid overwrite on SOURCE dir
#Source1:	COPYING.LIB.gdk3

# MRI only
Requires:	ruby
BuildRequires:	ruby

Requires:	ruby(rubygems) 
# FIXME it seems this is needed
Requires:	rubygem(atk)
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	rubygem-glib2-devel >= %{glib_min_ver}
BuildRequires:	rubygem-pango-devel
BuildRequires:	gtk3-devel
# %%check
BuildRequires:	rubygem(gdk_pixbuf2)
BuildRequires:	rubygem(gio2)
BuildRequires:	rubygem(cairo-gobject)
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
# FIXME it seems this is needed
BuildRequires:	rubygem(atk)
# X is needed
BuildRequires:	xorg-x11-server-Xvfb
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Obsoletes:		rubygem-gdk3-devel < 2.2.3
# BuildArch changed from 2.2.3
BuildArch:		noarch

%description
Ruby/GDK3 is a Ruby binding of GDK-3.x.

%package	devel
Summary:	Ruby/GLib development environment
Requires:	%{name}%{?isa} = %{version}-%{release}
Requires:	gtk3-devel%{?isa}
Requires:	ruby-devel%{?isa}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

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

#Patches

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
%if 0
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
%endif

# Cleanups
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -rf .%{gem_instdir}/dependency-check/
rm -f .%{gem_instdir}/extconf.rb
popd

%check
# ref: https://bugzilla.redhat.com/show_bug.cgi?id=2275913
# glycin on ppc64le is currently unusable
%if 0%{?fedora} >= 43
if ( arch | grep -q ppc64le ) ; then
	exit 0
fi
%endif

pushd .%{gem_instdir}

# kill unneeded make process
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd

sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
xvfb-run \
	-s '-screen 0 640x480x8 -extension RANDR' \
	$RANDR_OPTS \
	ruby -Ilib:test:ext/%{gem_name} ./test/run-test.rb

popd

%files
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%dir	%{gem_instdir}/
%dir	%{gem_instdir}/lib/
%{gem_instdir}/lib/%{gem_name}.rb
%dir	%{gem_instdir}/lib/%{gem_name}/
%{gem_instdir}/lib/%{gem_name}/*.rb

%exclude %{gem_cache}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files	doc
%doc	%{gem_docdir}/
%exclude	%{gem_instdir}/test/

%changelog
%autochangelog
