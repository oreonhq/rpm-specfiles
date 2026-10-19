%global source0_hash aad445d7ef28a7ecad28c766b29c9afa2d8ef9c233146334e88f349d93b5f1a6
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	poppler
%global	glibminver	3.0.8
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of poppler-glib
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:			poppler-glib
Provides:	rubygem(%{gem_name}) = %{version}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
Obsoletes:	rubygem-%{gem_name}-devel < %{version}
BuildArch:	noarch
# oreon:deps
BuildRequires:  poppler-glib
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(cairo-gobject)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(gio2)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/Poppler is a Ruby binding of poppler-glib.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/Poppler development environment
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ruby-%{gem_name}-devel < %{obsoleteevr}
Provides:	ruby-%{gem_name}-devel = %{version}-%{release}
%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# pkgconfig dependency is actually not needed (when using rpm
# dependency solver)
sed -i dependency-check/Rakefile \
	-e 's|dependency:check|nothing|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	dependency-check/ \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd .%{gem_instdir}
mkdir -p TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true make
export PATH=$(pwd):$PATH
popd
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
export RUBYLIB=$(pwd)/lib:$(pwd)/test:$(pwd)/ext/%{gem_name}
ruby ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-poppler-doc -f %{oreon_filedir}/rubygem-poppler-doc.list
%files -n rubygem-poppler-devel -f %{oreon_filedir}/rubygem-poppler-devel.list

%changelog

%autochangelog
