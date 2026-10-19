%global source0_hash 00d77fb9418a38df6a8cb153e955ef8180e767997cfcf8f52ed3ede4bf5760f1
%global	gem_name	webkit2-gtk
%undefine        _changelog_trimtime
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby binding of WebKit2GTK+
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.osdn.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.webkit2-gtk
Requires:		webkit2gtk4.0
BuildArch:		noarch
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  ruby
BuildRequires:  rubygem(gobject-introspection)
BuildRequires:  rubygem(gtk3)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
BuildRequires:  webkit2gtk4.0
# /oreon:deps
%description
Ruby/WebKit2GTK is a Ruby binding of WebKit2GTK+.

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

# pkgconfig dependency is actually not needed (when using rpm
# dependency solver)
sed -i dependency-check/Rakefile \
	-e 's|dependency:check|nothing|'
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
	dependency-check/ \
	test/
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rm -rf tmp
mkdir tmp
pushd tmp
touch gobject-introspection-test-utils.rb
popd
RANDR_OPTS=""
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb \
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-webkit2-gtk-doc -f %{oreon_filedir}/rubygem-webkit2-gtk-doc.list

%changelog

%autochangelog
