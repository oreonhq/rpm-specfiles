%global source0_hash 0acb9a20b719a6bf1f53fa1ac39a23b4b87bb271e34ab123bfacb7b25c8f8f8d
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	pango
%global	gem_name_gi pango
%global	gem_name_no_gi pango-no-gi
%global	glibminver	3.1.3
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of pango-1.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	pango-%{version}-test-missing-files.tar.gz
Source2:	pango-create-missing-test-files.sh
Requires:	ruby(release)
Requires:	rubygems
Provides:	rubygem(%{gem_name}) = %{version}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
Obsoletes:	rubygem-pango-no-gi < 3.4.3-3.999
Obsoletes:	rubygem-pango-no-gi-doc < 3.4.3-3.999
# oreon:deps
BuildRequires:  gcc
BuildRequires:  liberation-mono-fonts
BuildRequires:  pango-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(cairo-gobject)
BuildRequires:  rubygem(gobject-introspection)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-gobject-introspection-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/Pango is a Ruby binding of pango-1.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/pango development environment
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-devel
Requires:	pango-devel
Requires:	rubygem-cairo-devel
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
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# Fix wrong shebang

# Kill shebang

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
mkdir -p .%{header_dir}
mv .%{gem_extdir_mri}/*.h .%{header_dir}/
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/
pushd %{buildroot}
rm -rf .%{gem_instdir}/ext/
rm -f .%{gem_instdir}/extconf.rb
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
tar xf %{SOURCE1}
mkdir test || :
cp -a pango/test/* test
rm -rf ./TMPBINDIR
mkdir ./TMPBINDIR
pushd ./TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
LANG=C.UTF-8
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} ./test/run-test.rb \
%ifarch %ix86
	'--ignore-name=/test_rotate!*/' \
%endif
	%{nil}
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pango-doc -f %{oreon_filedir}/rubygem-pango-doc.list
%files -n rubygem-pango-devel -f %{oreon_filedir}/rubygem-pango-devel.list

%changelog

%autochangelog
