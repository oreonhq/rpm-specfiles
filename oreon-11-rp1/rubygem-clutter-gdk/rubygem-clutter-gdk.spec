%global source0_hash 87d8f91b1bdb1b14eeea683e73829246de8e2325f32517bdf7f8330e2c2672a4

%global	gem_name	clutter-gdk

%undefine        _changelog_trimtime

Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:	1%{?dist}

Summary:	Ruby binding of GDK specific API of Clutter
# SPDX confirmed
# LGPL-2.1-or-later: gemspec
License:	LGPL-2.1-or-later
URL:		http://ruby-gnome2.osdn.jp/

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# pull in additional files from the upstream
#Source1:	https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/clutter-gdk/COPYING.LIB
#Source2:	https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/clutter-gdk/README.md

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
# No tests currently
#BuildRequires:	rubygem(clutter)
#BuildRequires:	rubygem(gdk3)
#BuildRequires:	clutter-gtk
Requires:		clutter-gtk

BuildArch:		noarch

%description
Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch

%description	doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 4\.3\.5|>= 4.3.5|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -f \
	Rakefile \
	%{nil}
popd

%check
# No check currently

%files
%dir	%{gem_instdir}
# Gem usually places license file below %%gem_instdir
%license	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/README.md

%{gem_libdir}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
