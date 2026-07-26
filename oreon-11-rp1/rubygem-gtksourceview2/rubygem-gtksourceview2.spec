%global source0_hash fae6caa3c9713b29a4419d07e46d655f4be474312a3fcbf7c4a10362c431dfed

%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	gtksourceview2

%global	glibminver	3.0.8
%global	gtkminver	3.0.8
%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of gtksourceview-2.x
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	22%{?dist}
# gtksourceview2-3.4.3.gemspec	LGPL-2.1-or-later
# Other source	LGPL-2.1-or-later
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	gcc
BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-gtk2-devel >= %{gtkminver}
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	gtksourceview2-devel
## %%check
BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}

Obsoletes:		ruby-%{gem_name} < %{version}-%{release}
Provides:		ruby-%{gem_name} = %{version}-%{release}
Provides:		ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/GtkSourceView2 is a Ruby binding of gtksourceview-2.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GtkSourceView2 development environment
Requires:	%{name} = %{version}-%{release}
# Obsoletes / Provides
# ruby(%%{gem_name}-devel) Provides is for compatibility
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
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}.gemspec

# Fix wrong shebang
#grep -rl /usr/local/bin sample | \
#	xargs sed -i -e 's|/usr/local/bin|/usr/bin|'

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

# Fix test/run-test.rb
sed -i \
	-e 's|test/glib-test-init|glib-test-init|' \
	-e '/gtk-test-utils/d' \
	test/run-test.rb

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/

# Cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	ext/ \
	extconf.rb \
	Rakefile \
	test/ \
	*.gemspec \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}

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

export RUBYLIB=$(pwd)/lib:$(pwd)/test:%{buildroot}%{gem_extdir_mri}
xvfb-run \
	ruby ./test/run-test.rb

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%license	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/README.md

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_extdir_mri}/

%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
%autochangelog
