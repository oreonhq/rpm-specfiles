%global source0_hash a59135c6ce3e9e0c48d4685a77f225194adf84a0ffc1019dda1ab9a2bf6fd155
%global	gem_name	gdk4
%global	gem_ver	4.3.5
%global	gem_ver_escaped %(v=%{gem_ver}; echo ${v} | sed -e 's|\\.|\\\\.|g')
Name:		rubygem-%{gem_name}
Version:	4.3.5
Release:        1%{?dist}
Summary:        Ruby/GDK4 is a Ruby binding of GDK-4.x
License:	LGPL-2.1-or-later
URL:		https://ruby-gnome.github.io/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
Source2:	%{gem_name}-create-missing-test-files.sh
Requires:		gtk4
BuildArch:		noarch
# oreon:deps
BuildRequires:  //bin/xvfb-run
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(cairo-gobject)
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(pango)
BuildRequires:  rubygem(pkg-config)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/GDK4 is a Ruby binding of GDK-4.x.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

# Allow higher version of other ruby-gnome suite pkgs
sed -i -e 's|= %{gem_ver_escaped}|>= %{gem_ver}|' %{gem_name}-%{version}.gemspec

# Remove unneeded rake runtime dependency
sed -i %{gem_name}-%{version}.gemspec \
	-e '\@add_runtime_dependency.*rake@d'

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
sed -i .%{gem_spec} -e '\@s\.extensions =@d'
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	%{gem_name}.gemspec \
	Rakefile \
	dependency-check/ \
	test/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -a %{gem_name}/test .%{gem_instdir}
pushd .%{gem_instdir}
sed -i test/run-test.rb \
	-e '\@run-test@s|require_relative "../../|require "|'
xvfb-run \
	ruby -Ilib:test ./test/run-test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gdk4-doc -f %{oreon_filedir}/rubygem-gdk4-doc.list

%changelog

%autochangelog
