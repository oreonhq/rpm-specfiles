%global source0_hash dfb18826fe1737cbc00ef641abe0f7c77f3646d14775e541d54a949ba3792a6c

%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	gtk2

%global	glibminver	3.1.3
%global	pangominver	%{glibminver}
%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of GTK+-2.x
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	29%{?dist}
# gemspec	LGPL-2.1-or-later
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# Assign non-zero unique ID to each string (especially for id_relative_callbacks),
# especially for ruby 3.2
Patch0:	rubygem-gtk2-3.4.3-assign-nonzero-ID-to-relative-callback.patch
# Patches for C99 -Werror=incompatible-pointer-types
Patch1:	gtk2-3.4.3-rb_rescue-func-prototype.patch
Patch2:	gtk2-3.4.3-rb_define_method_arg_number.patch
Patch3:	gtk2-3.4.3-pointer-type-extra-cast-c99.patch
Patch4:	gtk2-3.4.3-c23-strict-function-prototype.patch
Patch5:	gtk2-3.4.3-c23-port-to-glib2_426.patch

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	rubygems-devel
BuildRequires:	rubygem-cairo-devel >= 1.2.5
BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem-pango-devel >= %{pangominver}
BuildRequires:	ruby-devel
BuildRequires:	gtk2-devel
BuildRequires:	rubygem(atk) >= %{glibminver}
BuildRequires:	rubygem(gdk_pixbuf2) >= %{glibminver}
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
BuildRequires:	rubygem-gobject-introspection-devel
# %%check
# Testsuite needs X
BuildRequires:	xorg-x11-server-Xvfb
# Icon for face-cool
BuildRequires:	gnome-icon-theme
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}

Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/GTK2 is a Ruby binding of GTK+-2.0.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	-n ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Requires:	%{name} = %{version}-%{release}
# Requires for corresponsing non-gem rpms
Requires:	ruby(atk) >= %{glibminver}
Requires:	ruby(gdk_pixbuf2) >= %{glibminver}
Requires:	ruby(glib2) >= %{glibminver}
Requires:	ruby(pango) >= %{glibminver}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description	-n ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%package	devel
Summary:	Ruby/GTK development environment
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-devel
Requires:	gtk2-devel
Requires:	rubygem-glib2-devel
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
# Will fix below later
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}-%{version}.gemspec

# Patches and etc
%patch -P0 -p1 -b .nonzero_id
%patch -P1 -p1 -b .rb_rescue_2args
%patch -P2 -p1 -b .method_arg_num
%patch -P3 -p1 -b .pointer-cast
%patch -P4 -p1 -b .c23
%patch -P5 -p1 -b .c23_newglib

# Fix wrong dir
grep -rl /usr/local/bin sample | \
	xargs sed -i -e 's|/usr/local/|/usr/|' || true

# Kill shebang
grep -rl '#!.*/usr/bin' sample lib | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

# rb_cData is deprecated, removed in ruby32
grep -rl rb_cData . | xargs sed -i -e 's|rb_cData|rb_cObject|'

%build
gem build ./%{gem_name}-%{version}.gemspec
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
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
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/

# Cleanups
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	ext/ \
	extconf.rb \
	*.gemspec \
	test/ \
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

# set GTK2_RC_FILES
cat > gtkrc <<EOF
gtk-theme-name = "gnome"
gtk-icon-theme-name = "gnome"
gtk-cursor-theme-name = "gnome"
gtk-button-images = 0
gtk-menu-images = 0
EOF
export GTK2_RC_FILES=$(pwd)/gtkrc

sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
# Adwaita themes broken on F-30?? Need investigating...
xvfb-run \
	ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb \
	|| false

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/
%dir	%{gem_instdir}/lib/%{gem_name}/

%license	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/README.md

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_instdir}/lib/%{gem_name}/base.rb
%{gem_extdir_mri}/

%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc
%{header_dir}/rbgdk.h
%{header_dir}/rbgdkconversions.h
%{header_dir}/rbgtk.h
%{header_dir}/rbgtkconversions.h
%{header_dir}/rbgtkmacros.h

%files	doc
%{gem_dir}/doc/%{gem_name}-%{version}
%{gem_instdir}/sample/

%changelog
%autochangelog
