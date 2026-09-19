%global source0_hash 271d986f4ccb100381656f7b1e0731b0235052704d9262bbac88aabf1d144435

%global	gem_name	clutter

Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}
Summary:	Ruby binding of Clutter

%undefine        _changelog_trimtime

# SPDX confirmed
# LGPL-2.1-or-later: gemspec
# LGPL-2.1-only:	sample/box-layout.rb sample/grid-layout.rb
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
Source1:	COPYING.LIB.clutter

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	clutter
BuildRequires:	rubygem(cairo-gobject)
BuildRequires:	rubygem-glib2-devel
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem(pango)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
# Need X
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
Requires:	ruby(release)
Requires:	ruby(rubygems)
Requires:	clutter
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Ruby/Clutter is a Ruby binding of Clutter.

%package	doc
Summary:	Documentation for %{name}
License:	LGPL-2.1-or-later AND LGPL-2.1-only
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# clutter should be okay, pkgconfig(clutter-1.0) not strictly needed.
# hacking
sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|clutter-1.0|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

# Add license text
install -cpm 644 %{SOURCE1} ./COPYING.LIB
sed -i -e '/files =/s|\("Rakefile",\)|\1 "COPYING.LIB", |' \
	%{gem_name}-%{version}.gemspec

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
popd

%check
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
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'

# Tweak test source directory
sed -i.path \
	-e '\@^clutter_base =@s|^.*$|clutter_base = File.join(File.dirname(__FILE__), "..")|' \
	test/run-test.rb

mkdir tmp
touch tmp/gobject-introspection-test-utils.rb

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

# Need X
# For screen depth 24, see bug 904851
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
%if 0
	-e /dev/stderr \
%endif
	ruby -Ilib:tmp:test ./test/run-test.rb

mv test/run-test.rb{.path,}
rm -rf tmp/

popd

%files
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%dir	%{gem_instdir}/
%dir	%{gem_instdir}/lib/
%{gem_instdir}/lib/%{gem_name}.rb
%dir	%{gem_instdir}/lib/%{gem_name}
%{gem_instdir}/lib/%{gem_name}/*.rb

%exclude %{gem_cache}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files	doc
%doc	%{gem_docdir}
# Contains really executable sample scripts
%{gem_instdir}/sample/
%exclude	%{gem_instdir}/test/

%changelog
%autochangelog
