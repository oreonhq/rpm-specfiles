%global source0_hash a7e7549977548deb462e8c2294915ac5732e52f1f72e114b581b47c90394bc16

%global gem_name pry

%global slop_version 3.4.0

Name: rubygem-%{gem_name}
Version: 0.15.2
Release: 2%{?dist}
Summary: A runtime developer console and IRB alternative
License: MIT
URL: http://pry.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/pry/pry.git && cd pry
# git archive -v -o pry-0.15.2-spec.tar.gz v0.15.2 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Fix compatibility with Ruby 4.0 `source_location` method.
# https://github.com/pry/pry/pull/2357
Patch0: rubygem-pry-0.15.2-Fix-source-location-usage-to-support-Ruby-4-0.patch
Patch1: rubygem-pry-0.15.2-Fix-source-location-usage-to-support-Ruby-4-0-spec.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(coderay) => 1.1.0
BuildRequires: rubygem(irb)
BuildRequires: rubygem(method_source) => 0.8.1
BuildRequires: rubygem(rspec)
# https://github.com/pry/pry/pull/1498
Provides: bundled(rubygem-slop) = %{slop_version}
BuildArch: noarch

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

%patch 0 -p1

( cd %{builddir}
%patch 1 -p1
)

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
( cd .%{gem_instdir}
[ `ruby -Ilib -rpry/slop -e "puts Pry::Slop::VERSION"` == '%{slop_version}' ]

ln -s %{builddir}/spec spec

# Rakefile is used by editor test.
touch Rakefile

# Original test suite is run from non-versioned directory:
# https://github.com/pry/pry/blob/9d9ae4a0b0bd487bb41170c834b3fa417e161f23/spec/cli_spec.rb#L219
sed -i '/pry\/foo/ s/pry/pry-%{version}/' spec/cli_spec.rb

# `EDITOR` env varialbe is used by a few specs.
EDITOR=/usr/bin/vi rspec -rspec_helper spec
)

%files
%dir %{gem_instdir}
%{_bindir}/pry
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
