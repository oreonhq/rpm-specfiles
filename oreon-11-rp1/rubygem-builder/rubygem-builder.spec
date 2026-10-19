%global source0_hash 497918d2f9dca528fdca4b88d84e4ef4387256d984b8154e9d5d3fe5a9c8835f
%global gem_name builder
Name: rubygem-%{gem_name}
Version: 3.3.0
Release:        1%{?dist}
Summary:        Builders for MarkUp
License: MIT
URL: https://github.com/rails/builder
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Builder provides a number of builder objects that make creating structured
data simple to do. Currently the following builder objects are supported:
* XML Markup
* XML Events

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
  find -type f -name '*.rb' -print | xargs sed -i '/#!\/usr\/bin\/env/d'
popd
sed -i '/#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/rakelib/tags.rake
chmod a-x %{buildroot}%{gem_instdir}/rakelib/tags.rake
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-builder-doc -f %{oreon_filedir}/rubygem-builder-doc.list

%changelog

%autochangelog
