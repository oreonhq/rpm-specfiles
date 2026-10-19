%global source0_hash 13371dd58cda5137f31ed690c3b79320e1101f9da4234d8115ff4bc078b63e2e
%global	gem_name	gtksourceview3
%undefine        _changelog_trimtime
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby binding of gtksourceview-3.x
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.gtksourceview3
Requires:	gtksourceview3
BuildArch:		noarch
# oreon:deps
BuildRequires:  //bin/xvfb-run
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gtk3-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GtkSourceView3 is a Ruby binding of gtksourceview-3.x.

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

find . -name \*.rb -print0 | xargs -0 chmod 0644

# Relax ruby-gnome2 internal dependency
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|gtksourceview-3.0|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

sed -i -e 's|test/glib-test-init|glib-test-init|' \
	test/run-test.rb

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
	extconf.rb \
	ext/ \
	test/ \
	dependency-check/ \
	%{nil}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rm -rf tmp
mkdir tmp
touch tmp/gtk-test-utils.rb
RANDR_OPTS=""
RANDR_OPTS="-extension RANDR"
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gtk3/test/|require "|'
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:ext/%{gem_name}:tmp:test ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gtksourceview3-doc -f %{oreon_filedir}/rubygem-gtksourceview3-doc.list

%changelog

%autochangelog
