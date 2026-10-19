%global source0_hash eb2255ceeacc476ee9697ca0d0377f06149e9e4b8c389d9139b508f5b51ea662
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	gdk_pixbuf2
%global	glibminver	3.0.8
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of GdkPixbuf-2.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}
BuildArch:	noarch
Obsoletes:		ruby-%{gem_name} < %{version}-%{release}
Provides:		ruby-%{gem_name} = %{version}-%{release}
Provides:		ruby(%{gem_name}) = %{version}-%{release}
Requires:		gdk-pixbuf2
Requires:		rubygem(gobject-introspection)
Obsoletes:		ruby-gdkpixbuf2-devel < %{obsoleteevr}
Obsoletes:		rubygem-gdk_pixbuf2-devel < 3.0.9
# oreon:deps
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gdk-pixbuf2-modules
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(gio2)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

# Fix up Rakefile for "gnome2-raketask" requirement
sed -i -e "/require.*gnome2-raketask/s|^\(.*\)|begin\n  \1\nrescue LoadError\n  require 'rubygems'\n  require 'gnome2-raketask'\nend\n|" \
	Rakefile

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:ext/%{gem_name} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gdk_pixbuf2-doc -f %{oreon_filedir}/rubygem-gdk_pixbuf2-doc.list

%changelog

%autochangelog
