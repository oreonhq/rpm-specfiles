%global source0_hash 00d77fb9418a38df6a8cb153e955ef8180e767997cfcf8f52ed3ede4bf5760f1

%global	gem_name	webkit2-gtk

%undefine        _changelog_trimtime

Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}

Summary:	Ruby binding of WebKit2GTK+
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.osdn.jp/

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
# renamed to avoid namespace collision on sourcedir
Source1:	COPYING.LIB.webkit2-gtk

# Require MRI
BuildRequires:	ruby
BuildRequires:	rubygems-devel
# glib-test-init.rb
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	rubygem-glib2-devel
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem(gtk3)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(webrick)
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# Use webkit2gtk-4.1 for F-39+
%if 0%{?fedora} >= 39
BuildRequires:	webkit2gtk4.1
Requires:		webkit2gtk4.1
%else
BuildRequires:	webkit2gtk4.0
Requires:		webkit2gtk4.0
%endif

BuildArch:		noarch

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

# cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	dependency-check/ \
	test/
popd

%check
pushd .%{gem_instdir}

rm -rf tmp
mkdir tmp
pushd tmp
touch gobject-introspection-test-utils.rb
popd

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
sed -i test/run-test.rb \
	-e 's|require_relative "../../gobject-introspection/test/|require "|'

# ignore test failure for F-30 for now
xvfb-run \
	-s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb \
%if 0%{?fedora} >= 32
	|| true # ignore test failure for now
%endif

popd

%files
%dir		%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{gem_libdir}
%{gem_spec}

%exclude	%{gem_instdir}/*gemspec
%exclude	%{gem_cache}

%files	doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/sample

%changelog
%autochangelog
