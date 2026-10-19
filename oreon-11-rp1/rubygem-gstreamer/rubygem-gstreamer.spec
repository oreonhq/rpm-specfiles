%global source0_hash 615d414f88ff9dd071d4cb53e569040c2438dd36f6aeebc67925d4ef8d6eb075
%global	header_dir	%{ruby_vendorarchdir}
%global		gem_name		gstreamer
%global		gemsoname		gst
%global		glibminver		3.0.8
%global		obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of GStreamer
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
Obsoletes:	ruby-%{gem_name} < %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gobject-introspection-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GStreamer is a Ruby binding of GStreamer.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GStreamer development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
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
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gstreamer-doc -f %{oreon_filedir}/rubygem-gstreamer-doc.list
%files -n rubygem-gstreamer-devel -f %{oreon_filedir}/rubygem-gstreamer-devel.list

%changelog

%autochangelog
