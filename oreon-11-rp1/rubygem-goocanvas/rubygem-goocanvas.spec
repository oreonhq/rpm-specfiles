%global source0_hash 85e45c9e026a81c98630d914caadaf1c5088cf110fba09105104542e6c17b69a
%global	gem_name	goocanvas
%global	glibminver	4.1.2
%global	gtkminver	4.1.2
%global	obsoleteevr	0.90.7-1.999
Summary:        Ruby binding of GooCanvas
Name:		rubygem-%{gem_name}
Version:	2.2.0
Release:        38%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	COPYING.LIB.rubygem-goocanvas
Source2:	COPYING.GPL.rubygem-goocanvas
Patch0:	goocanvas-2.2.0-sample-gi412.patch
Requires:	ruby(release)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  goocanvas2-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gobject-introspection-devel
BuildRequires:  rubygem-gtk3-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GooCanvas is a Ruby binding of GooCanvas.

%package	devel
Summary:	Ruby/GooCanvas development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%package	doc
Summary:	Documentation for %{name}
License:	LGPL-2.1-or-later AND GPL-2.0-or-later
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 2\.2\.0|>= 2.2.0|' %{gem_name}-%{version}.gemspec

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
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	ext/ \
	extconf.rb \
	*.gemspec \
	%{nil}
popd
for f in %{SOURCE1} %{SOURCE2}
do
	install -cpm 644 $f %{buildroot}%{gem_instdir}/$(basename $f | sed -e 's|\.%{name}||')
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n rubygem-goocanvas-devel -f %{oreon_filedir}/rubygem-goocanvas-devel.list
%files -n rubygem-goocanvas-doc -f %{oreon_filedir}/rubygem-goocanvas-doc.list

%changelog

%autochangelog
