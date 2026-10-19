%global source0_hash a64933f813aa6423fc93d6152bb413cabfb730c913b1b87600e41a36d7971b06
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	atk
%global	glibminver	3.1.3
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of ATK-1.0.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	rubygems
Requires:	rubygem(gobject-introspection)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
BuildArch:	noarch
Obsoletes:		ruby-%{gem_name} < %{version}-%{release}
Provides:		ruby-%{gem_name} = %{version}-%{release}
Provides:		ruby(%{gem_name}) = %{version}-%{release}
Obsoletes:		ruby-%{gem_name}-devel < %{obsoleteevr}
Obsoletes:		rubygem-%{gem_name}-devel < 3.1.2
# oreon:deps
BuildRequires:  atk-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(gobject-introspection)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/ATK is a Ruby binding of ATK-1.0.x or later.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/ATK development environment
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-devel
Requires:	rubygem-glib2-devel >= %{glibminver}
Requires:	atk-devel
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

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

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
find . -name \*.gem | xargs chmod 0644
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:ext/%{gem_name} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-atk-doc -f %{oreon_filedir}/rubygem-atk-doc.list
%files -n rubygem-atk-devel -f %{oreon_filedir}/rubygem-atk-devel.list

%changelog

%autochangelog
