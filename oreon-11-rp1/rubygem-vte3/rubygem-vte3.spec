%global source0_hash 23cb9e5cebe6bfb5f000c8a5f196c08fa02668af6acabde85e38b61f8777120c

%global	gem_name	vte3
%global	glib_min_ver	3.0.8

%undefine        _changelog_trimtime

Summary:	Ruby binding of VTE
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}

# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/vte3/COPYING.LIB
# Renamed to avoid overwrite on SOURCE dir
Source1:	COPYING.LIB.vte3

BuildRequires:	vte291
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	rubygem-pango-devel
BuildRequires:	rubygem-gtk3
BuildRequires:	rubygem-glib2-devel >= %{glib_min_ver}
BuildRequires:	rubygem(test-unit)
BuildRequires:	%{_bindir}/xvfb-run
Requires:		vte291

Obsoletes:		rubygem-vte3-devel < 2.99
Provides:		rubygem-vte3-devel = 2.99

BuildArch:		noarch

%description
Ruby/VTE3 is a Ruby binding of VTE .

%package	devel
Summary:	Ruby/VTE3 development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name} .

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name} .

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# patches

# Relax the version dependency
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

# Add license text
install -cpm 644 %{SOURCE1} ./COPYING.LIB
FREEZE=""
if grep -q '"Rakefile"\.freeze' %{gem_name}-%{version}.gemspec
then
	FREEZE=".freeze"
fi

sed -i -e "/files =/s|\(\"Rakefile\"${FREEZE},\)|\1 \"COPYING.LIB\"${FREEZE}, |" \
	%{gem_name}-%{version}.gemspec
# vte3 should be okay, pkgconfig(vte-2.91) not strictly needed.
# hacking
sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|vte-2.91|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}-%{version}.gemspec

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror-implicit-function-declaration'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
popd

# Cleanups
pushd %{buildroot}
rm -rf \
	.%{gem_instdir}/Rakefile \
	.%{gem_instdir}/extconf.rb \
	.%{gem_instdir}/ext/
popd

%check
pushd .%{gem_instdir}
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

xvfb-run -s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb
popd

%files
%dir	%{gem_instdir}/
%license	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%dir	%{gem_instdir}/lib/
%{gem_instdir}/lib/%{gem_name}.rb
%dir	%{gem_instdir}/lib/%{gem_name}/
%{gem_instdir}/lib/%{gem_name}/*.rb

%exclude %{gem_cache}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files	doc
%doc	%{gem_docdir}/
%exclude	%{gem_instdir}/test

%changelog
%autochangelog
