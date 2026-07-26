%global source0_hash 85e45c9e026a81c98630d914caadaf1c5088cf110fba09105104542e6c17b69a

%global	gem_name	goocanvas

%global	glibminver	4.1.2
%global	gtkminver	4.1.2
%global	obsoleteevr	0.90.7-1.999

Summary:	Ruby binding of GooCanvas
Name:		rubygem-%{gem_name}
Version:	2.2.0
Release:	38%{?dist}
# gemspec	LGPL-2.1-or-later
# some files under sample/		GPL-2.0-or-later
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Licenses
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
Source1:	COPYING.LIB.rubygem-goocanvas
# http://www.gnu.org/licenses/gpl-2.0.txt
Source2:	COPYING.GPL.rubygem-goocanvas
# Fix for sample with ruby-gi 4.1.2
Patch0:	goocanvas-2.2.0-sample-gi412.patch

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	rubygems-devel
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem-gobject-introspection-devel >= %{gtkminver}
BuildRequires:	rubygem-gtk3-devel >= %{gtkminver}
BuildRequires:	ruby-devel
BuildRequires:	goocanvas2-devel
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

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
# Samples are under GPL-2.0-or-later
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
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
#mkdir -p .%{header_dir}
#mv .%{gem_extdir_mri}/*.h .%{header_dir}/
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
	%{nil}
popd

# Licenses
for f in %{SOURCE1} %{SOURCE2}
do
	install -cpm 644 $f %{buildroot}%{gem_instdir}/$(basename $f | sed -e 's|\.%{name}||')
done

%check
# Currently no testsuite available

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%license	%{gem_instdir}/COPYING*
%doc	%{gem_instdir}/[D-Z]*

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_instdir}/lib/goo/
%{gem_extdir_mri}/

%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
%autochangelog
