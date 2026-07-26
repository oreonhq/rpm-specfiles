%global source0_hash 61245c5a14e25b1464c03c3804db81b8a347adb0429f357a62394bfa5a9f995a

%global	header_dir	%{ruby_vendorarchdir}

%global	gem_name	vte

%global	glibminver	3.0.8
%global	gtkminver	3.0.8
%global	obsoleteevr	0.90.7-1.999

%undefine        _changelog_trimtime

Summary:	Ruby binding of vte
Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	20%{?dist}

# from README.md
# SPDX confirmed
License:	LGPL-2.1-only
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	gcc

BuildRequires:	rubygem-glib2-devel >= %{glibminver}
BuildRequires:	rubygem-gtk2-devel >= %{gtkminver}
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	vte-devel
Provides:	rubygem(%{gem_name}) = %{version}

Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description
Ruby/VTE is a Ruby binding of VTE

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/VTE development environment
Requires:	%{name} = %{version}-%{release}
# Obsoletes / Provides
# ruby(%%{gem_name}-devel) Provides is for compatibility

Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}
Provides:	ruby(%{gem_name}-devel) = %{version}-%{release}

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

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
# move header files, C extension files to the correct directory
#mkdir -p .%{header_dir}
#mv .%{gem_instdir}/lib/*.h .%{header_dir}/

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
	*.gemspec \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}

%check
# Currently no testsuite available

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%license	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/[D-Z]*

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_instdir}/lib/%{gem_name}/
%{gem_extdir_mri}/

%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
%autochangelog
