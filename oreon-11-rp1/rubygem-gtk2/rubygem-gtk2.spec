%global source0_hash dfb18826fe1737cbc00ef641abe0f7c77f3646d14775e541d54a949ba3792a6c
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	gtk2
%global	glibminver	3.1.3
%global	pangominver	%{glibminver}
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of GTK+-2.x
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Patch0:	rubygem-gtk2-3.4.3-assign-nonzero-ID-to-relative-callback.patch
Patch1:	gtk2-3.4.3-rb_rescue-func-prototype.patch
Patch2:	gtk2-3.4.3-rb_define_method_arg_number.patch
Patch3:	gtk2-3.4.3-pointer-type-extra-cast-c99.patch
Patch4:	gtk2-3.4.3-c23-strict-function-prototype.patch
Patch5:	gtk2-3.4.3-c23-port-to-glib2_426.patch
Requires:	ruby(release)
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  gnome-icon-theme
BuildRequires:  gtk2-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(atk)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gobject-introspection-devel
BuildRequires:  rubygem-pango-devel
BuildRequires:  rubygems-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
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
xvfb-run \
	ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb \
	|| false
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gtk2-doc -f %{oreon_filedir}/rubygem-gtk2-doc.list
%files -n ruby-gtk2 -f %{oreon_filedir}/ruby-gtk2.list
%files -n rubygem-gtk2-devel -f %{oreon_filedir}/rubygem-gtk2-devel.list

%changelog

%autochangelog
