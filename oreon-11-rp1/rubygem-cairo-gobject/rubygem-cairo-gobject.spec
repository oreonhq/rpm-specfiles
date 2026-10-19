%global source0_hash 3f15ede074ce75a22c5010a1b35ab7d5d4043be04bec6afd34ac63ea76102387
%global	gem_name	cairo-gobject
%global	gem_soname	cairo_gobject
%undefine        _changelog_trimtime
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby binding of cairo-gobject
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby
Requires:	ruby(rubygems)
Requires:	rubygem(cairo) 
Requires:	rubygem(glib2)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  cairo-gobject-devel
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/CairoGObject is a Ruby binding of cairo-gobject.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'
# ???
sed -i -e \
	'\@gobject-introspection-test-utils@d' \
	test/run-test.rb

%build

gem build %{gem_name}-%{version}.gemspec
export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror-implicit-function-declaration'"
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}
mkdir -p .%{header_dir}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i.make -e 's|which make|which nomake|' test/run-test.rb
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cairo-gobject-doc -f %{oreon_filedir}/rubygem-cairo-gobject-doc.list

%changelog

%autochangelog
