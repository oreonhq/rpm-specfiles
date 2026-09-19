%global source0_hash 850f26731863948002bc48ecf56c521b75e282043614b297146c9361a9793a0e

%global gem_name clutter-gstreamer

%undefine        _changelog_trimtime

Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}

Summary:	Ruby binding of Clutter-GStreamer
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
# renamed to avoid namespace collision on sourcedir
Source1:	COPYING.LIB.clutter-gstreamer

BuildRequires:	rubygems-devel
# %%check
BuildRequires:	rubygem(clutter)
BuildRequires:	rubygem(gdk_pixbuf2)
BuildRequires:	rubygem(gstreamer)
BuildRequires:	rubygem-glib2-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify) 
BuildRequires:	%{_bindir}/xvfb-run
# See bug 904851 and below
BuildRequires:	mesa-dri-drivers
# F-29+: switch to clutter-gst3 (bug 1578064)
%if 0%{?fedora} >= 29 || 0%{?rhel} > 8
BuildRequires:	clutter-gst3
Requires:	clutter-gst3
%else
BuildRequires:	clutter-gst2
Requires:	clutter-gst2
%endif

BuildArch:		noarch

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

%check
pushd .%{gem_instdir}

mkdir tmp
touch \
	tmp/gobject-introspection-test-utils.rb \
	tmp/clutter-test-utils.rb

# Clutter-CRITICAL **:Unable to initialize Clutter: 
# Unable to find suitable fbconfig for the GLX context: 
# Failed to find any compatible fbconfigs
#
# So use screen depth 24, see bug 904851

sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../clutter/test/|require "|'
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

%{gem_libdir}
%{gem_spec}

%exclude	%{gem_instdir}/*gemspec
%exclude	%{gem_cache}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/sample/

%changelog
%autochangelog
