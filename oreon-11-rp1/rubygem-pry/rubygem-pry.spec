%global source1_hash 8920d0c8ce0e8b7e0ae3f85b205b08a3ee4761c9225641c914a6135d349bc88e
%global source0_hash 12d54b8640d3fa29c9211dd4ffb08f3fd8bf7a4fd9b5a73ce5b59c8709385b6b
%global gem_name pry
%global slop_version 3.4.0
Name: rubygem-%{gem_name}
Version: 0.15.2
Release:        1%{?dist}
Summary:        A runtime developer console and IRB alternative
License: MIT
URL: http://pry.github.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/pry/pry/archive/refs/tags/v0.15.2.tar.gz
Patch0: rubygem-pry-0.15.2-Fix-source-location-usage-to-support-Ruby-4-0.patch
Patch1: rubygem-pry-0.15.2-Fix-source-location-usage-to-support-Ruby-4-0-spec.patch
Provides: bundled(rubygem-slop) = %{slop_version}
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(coderay)
BuildRequires:  rubygem(irb)
BuildRequires:  rubygem(method_source)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Pry is a runtime developer console and IRB alternative with powerful
introspection capabilities. Pry aims to be more than an IRB replacement. It is
an attempt to bring REPL driven programming to the Ruby language.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1

( cd %{builddir}
%patch 1 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
[ `ruby -Ilib -rpry/slop -e "puts Pry::Slop::VERSION"` == '%{slop_version}' ]
ln -s %{builddir}/spec spec
touch Rakefile
sed -i '/pry\/foo/ s/pry/pry-%{version}/' spec/cli_spec.rb
EDITOR=/usr/bin/vi rspec -rspec_helper spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pry-doc -f %{oreon_filedir}/rubygem-pry-doc.list

%changelog

%autochangelog
