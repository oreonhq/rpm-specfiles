%global source0_hash 271d986f4ccb100381656f7b1e0731b0235052704d9262bbac88aabf1d144435
%global	gem_name	clutter
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby binding of Clutter
%undefine        _changelog_trimtime
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.clutter
Requires:	ruby(release)
Requires:	ruby(rubygems)
Requires:	clutter
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  clutter
BuildRequires:  mesa-dri-drivers
BuildRequires:  ruby(release)
BuildRequires:  rubygem(cairo-gobject)
BuildRequires:  rubygem(gobject-introspection)
BuildRequires:  rubygem(pango)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
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
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'
sed -i.path \
	-e '\@^clutter_base =@s|^.*$|clutter_base = File.join(File.dirname(__FILE__), "..")|' \
	test/run-test.rb
mkdir tmp
touch tmp/gobject-introspection-test-utils.rb
RANDR_OPTS=""
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb
mv test/run-test.rb{.path,}
rm -rf tmp/
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-clutter-doc -f %{oreon_filedir}/rubygem-clutter-doc.list

%changelog

%autochangelog
