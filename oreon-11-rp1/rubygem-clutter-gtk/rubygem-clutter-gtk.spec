%global source0_hash 3192942848134f55b3e3283cb2428a23f148debcd637ce21812c1b1d4342324d

%global	gem_name	clutter-gtk

%undefine        _changelog_trimtime

Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}
Summary:	Ruby binding of Clutter-GTK

# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
# renamed to avoid namespace collision on sourcedir
Source1:	COPYING.LIB.clutter-gtk

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(clutter)
BuildRequires:	rubygem(clutter-gdk)
BuildRequires:	rubygem(gtk3)
BuildRequires:	rubygem-glib2-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	%{_bindir}/xvfb-run
# See bug 904851 and below
BuildRequires:	mesa-dri-drivers
BuildRequires:	clutter-gtk

Requires:		clutter-gtk

BuildArch:	noarch

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

# cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	dependency-check/ \
	test/
popd

%check
pushd .%{gem_instdir}

mkdir tmp
touch \
	tmp/gobject-introspection-test-utils.rb \
	tmp/clutter-test-utils.rb

# Tweak test source directory
sed -i \
	-e '\@clutter_gtk_test_base =@s|clutter_gtk_base|File.dirname(__FILE__), ".."|' \
	test/run-test.rb
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../clutter/test/|require "|'

# Clutter-CRITICAL **:Unable to initialize Clutter: 
# Unable to find suitable fbconfig for the GLX context: 
# Failed to find any compatible fbconfigs
#
# So use screen depth 24, see bug 904851
#
# https://github.com/ruby-gnome2/ruby-gnome2/issues/274
# Umm.. under non-chroot environment, the following passes.
# However in mock environ the following sometimes fails.
# http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/media-libs/clutter/clutter-1.18.4.ebuild?view=markup
# may suggest that this may be related to mesa driver issues,
# however I am not sure - disabled for now
#
#test -n "$XAUTHORITY" || exit 0

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

xvfb-run -s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb

rm -rf tmp/
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%exclude	%{gem_cache}

%{gem_libdir}
%{gem_spec}

%exclude	%{gem_instdir}/*gemspec
%exclude	%{gem_cache}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/sample/

%changelog
%autochangelog
