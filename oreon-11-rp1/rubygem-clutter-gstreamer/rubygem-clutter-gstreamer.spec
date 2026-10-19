%global source0_hash 850f26731863948002bc48ecf56c521b75e282043614b297146c9361a9793a0e
%global gem_name clutter-gstreamer
%undefine        _changelog_trimtime
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby binding of Clutter-GStreamer
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.clutter-gstreamer
%if 0%{?fedora} >= 29 || 0%{?rhel} > 8 || 0%{?oreon} >= 11
Requires:	clutter-gst3
%else
Requires:	clutter-gst2
%endif
BuildArch:		noarch
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  clutter-gst3
BuildRequires:  mesa-dri-drivers
BuildRequires:  rubygem(clutter)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(gstreamer)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/ClutterGStreamer is a Ruby binding of Clutter-GStreamer.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

find . -name \*.rb -print0 | xargs --null chmod 0644

# Adjust rubygems-gnome2 requirement to be more flexible
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|clutter-gst-3.0|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

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
	test/ \
	dependency-check/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
mkdir tmp
touch \
	tmp/gobject-introspection-test-utils.rb \
	tmp/clutter-test-utils.rb
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
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
%files -n rubygem-clutter-gstreamer-doc -f %{oreon_filedir}/rubygem-clutter-gstreamer-doc.list

%changelog

%autochangelog
