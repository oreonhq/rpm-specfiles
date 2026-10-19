%global source0_hash 27f782c96087d080289e015c2b9d2f651d36df068c3e9dcd7cd43a03a7bc882a
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	gdk3
%global	glib_min_ver	3.0.8
%undefine        _changelog_trimtime
Summary:        Ruby binding of GDK-3.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby
Requires:	ruby(rubygems) 
Requires:	rubygem(atk)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Obsoletes:		rubygem-gdk3-devel < 2.2.3
BuildArch:		noarch
# oreon:deps
BuildRequires:  gtk3-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem(atk)
BuildRequires:  rubygem(cairo-gobject)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(gio2)
BuildRequires:  rubygem(gobject-introspection)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-pango-devel
BuildRequires:  rubygems-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -rf .%{gem_instdir}/dependency-check/
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
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
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gdk3-devel -f %{oreon_filedir}/rubygem-gdk3-devel.list
%files -n rubygem-gdk3-doc -f %{oreon_filedir}/rubygem-gdk3-doc.list

%changelog

%autochangelog
