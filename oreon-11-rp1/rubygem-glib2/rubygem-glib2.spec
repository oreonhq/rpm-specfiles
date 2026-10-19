%global source0_hash f5f2a0c012271c75ee552bfd86c2535331e2ae642390cd2fa3e3a94bfd275115
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	glib2
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of GLib-2.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch100:	rubygem-glib2-3.5.1-rubywrapper-pollutes-env.patch
Requires:	ruby(release)
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  //bin/ruby-mri
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(native-package-installer)
BuildRequires:  rubygem(pkg-config)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GLib2 is a Ruby binding of GLib-2.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GLib development environment
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	ruby-devel
Requires:	rubygem(pkg-config)
Requires:	rubygem(native-package-installer)
Requires:	rubygem(rake-compiler)
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Patches and etc
%patch -P100 -p1

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# Make pkg-config devel dependency (not runtime)
sed -i \
	-e '\@pkg-config@s|add_\(runtime_\)*dependency|add_development_dependency|' \
	-e '\@native-package-installer@s|add_\(runtime_\)*dependency|add_development_dependency|' \
	%{gem_name}.gemspec \
	Rakefile

sed -i \
	-e '2a require "rubygems"\ngem "test-unit"\n' \
	test/run-test.rb

# shebang issue
find sample/ test/ -name \*.rb | xargs chmod 0644
grep -rl '#![ ]*/usr' sample/ test/ | \
	xargs chmod 0755

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install
pushd .%{gem_instdir}
cat > lib/glib-test-init.rb <<EOF
\$VERBOSE = true
begin
	require 'rubygems'
	gem 'test-unit'
rescue LoadError
end
require 'test/unit'
EOF
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
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
pushd .%{gem_instdir}/
rm -f \
	Rakefile \
	extconf.rb \
	*gemspec \
	version.rb \
	test/test-*.rb \
	%{nil}
chmod 0644 test/*rb
mv test/ lib/glib2/
popd
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-glib2-doc -f %{oreon_filedir}/rubygem-glib2-doc.list
%files -n rubygem-glib2-devel -f %{oreon_filedir}/rubygem-glib2-devel.list

%changelog

%autochangelog
