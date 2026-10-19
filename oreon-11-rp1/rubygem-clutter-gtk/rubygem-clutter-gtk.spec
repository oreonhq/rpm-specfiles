%global source0_hash 3192942848134f55b3e3283cb2428a23f148debcd637ce21812c1b1d4342324d
%global	gem_name	clutter-gtk
%undefine        _changelog_trimtime
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby binding of Clutter-GTK
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.clutter-gtk
Requires:		clutter-gtk
BuildArch:	noarch
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  clutter-gtk
BuildRequires:  mesa-dri-drivers
BuildRequires:  ruby(release)
BuildRequires:  rubygem(clutter)
BuildRequires:  rubygem(clutter-gdk)
BuildRequires:  rubygem(gtk3)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/ClutterGTK is a Ruby binding of Clutter-GTK.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Adjust rubygems-gnome2 requirement to be more flexible
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|clutter-gtk-1.0|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec
# Fix permission
find . -name \*.rb -print0 | xargs --null chmod 0644

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
install -cpm 644 %{SOURCE1} %{buildroot}%{gem_instdir}/COPYING.LIB
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	dependency-check/ \
	test/
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
mkdir tmp
touch \
	tmp/gobject-introspection-test-utils.rb \
	tmp/clutter-test-utils.rb
sed -i \
	-e '\@clutter_gtk_test_base =@s|clutter_gtk_base|File.dirname(__FILE__), ".."|' \
	test/run-test.rb
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../clutter/test/|require "|'
RANDR_OPTS=""
xvfb-run -s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb
rm -rf tmp/
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-clutter-gtk-doc -f %{oreon_filedir}/rubygem-clutter-gtk-doc.list

%changelog

%autochangelog
