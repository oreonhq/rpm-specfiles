%global source0_hash 93b53875b082face7d24bf54ec98634b1674e1b713f1884a666c8d762f3e558a
%global	header_dir	%{ruby_vendorarchdir}
%global	gem_name	rsvg2
%global	glibminver	3.0.8
%global	obsoleteevr	0.90.7-1.999
%undefine        _changelog_trimtime
Summary:        Ruby binding of librsvg-2.x
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	librsvg2
Provides:	rubygem(%{gem_name}) = %{version}
Obsoletes:	ruby-%{gem_name} <= %{version}-%{release}
Provides:	ruby-%{gem_name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}
Obsoletes:	rubygem-%{gem_name}-devel < %{version}
BuildArch:	noarch
# oreon:deps
BuildRequires:  librsvg2-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(cairo-gobject)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-notify)
BuildRequires:  rubygem-cairo-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/RSVG is a Ruby binding of librsvg.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/RSVG development environment
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-devel
Requires:	pango-devel
Requires:	rubygem-cairo-devel
Obsoletes:	ruby-rsvg-devel < %{obsoleteevr}
Provides:	ruby-rsvg-devel = %{version}-%{release}
Provides:	ruby(rsvg-devel) = %{version}-%{release}
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

# pkgconfig dependency is actually not needed (when using rpm
# dependency solver)
sed -i dependency-check/Rakefile \
	-e 's|dependency:check|nothing|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

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
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	dependency-check/ \
	test/ \
	%{nil}
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
ruby -Ilib:test:ext/%{gem_name} ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rsvg2-doc -f %{oreon_filedir}/rubygem-rsvg2-doc.list
%files -n rubygem-rsvg2-devel -f %{oreon_filedir}/rubygem-rsvg2-devel.list

%changelog

%autochangelog
