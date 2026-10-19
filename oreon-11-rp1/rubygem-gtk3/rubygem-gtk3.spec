%global source0_hash 0f7e2596544cdd024d557d2b51b7098e5ae8f815cbec22977e819c9f32508d99
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	gtk3
%global	glib_min_ver	3.0.8
%undefine        _changelog_trimtime
Summary:        Ruby/GTK3 is a Ruby binding of GTK+-3.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.gtk3
Source2:	gtk3-%{version}-test-missing-files.tar.gz
Source3:	gtk3-create-missing-test-files.sh
Requires:	ruby
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  adwaita-icon-theme
BuildRequires:  gcc
BuildRequires:  gnome-icon-theme
BuildRequires:  gtk3-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem(atk)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-gdk3
BuildRequires:  rubygem-gdk_pixbuf2
BuildRequires:  rubygem-gio2
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gobject-introspection-devel
BuildRequires:  rubygem-pango-devel
BuildRequires:  rubygems-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Ruby/GTK3 is a Ruby binding of GTK+-3.x.

%package	devel
Summary:	Ruby/GTK3 development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	gtk3-devel%{?_isa}
Requires:	rubygem-glib2-devel%{?_isa}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%package	doc
Summary:	Documentation for %{name}
License:	LGPL-2.1-or-later AND GFDL-1.3-no-invariants-or-later
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# Add license text
install -cpm 644 %{SOURCE1} ./COPYING.LIB
sed -i -e '/files =/s|\("Rakefile",\)|\1 "COPYING.LIB", |' \
	%{gem_name}-%{version}.gemspec

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror-implicit-function-declaration'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar xf %{SOURCE2}
cp -a gtk3/* .
cd ..
ln -sf %{gem_name}-%{version} %{gem_name}
cd -
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
cd test
RANDR_OPTS=""
xvfb-run \
	ruby -I../lib:.:%{buildroot}%{gem_extdir_mri} run-test.rb
cd ..
cd ..
unlink %{gem_name}
cd -
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gtk3-devel -f %{oreon_filedir}/rubygem-gtk3-devel.list
%files -n rubygem-gtk3-doc -f %{oreon_filedir}/rubygem-gtk3-doc.list

%changelog

%autochangelog
