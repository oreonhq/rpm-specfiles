%global source0_hash de17f58b6761392bd2cbfa97a01bb8b9deae19d395ab7434505d4e45dded4b64
%global gem_name bundler_ext
Summary:        Load system gems via Bundler DSL
Name: rubygem-%{gem_name}
Version: 0.4.2
Release:        1%{?dist}
License: MIT
URL: https://github.com/bundlerext/bundler_ext
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(rails)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt)

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# https://github.com/ruby/rubygems/pull/9016
# source :rubygems is no longer accepted
sed -i spec/fixtures/Gemfile.in -e 's|source :rubygems|source "https://rubygems.org"|'

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bundler_ext-doc -f %{oreon_filedir}/rubygem-bundler_ext-doc.list

%changelog

%autochangelog
